#!/usr/bin/env python3
"""Bounded, dependency-free WP-024 L0/L1 reference checker; not a TLC replacement."""
from __future__ import annotations
import argparse, csv, itertools, json, math
from collections import Counter, deque
from pathlib import Path

def quorum_exhaustive():
    rows=[]
    for f in range(1,5):
        n,q=3*f+1,2*f+1
        sets=list(itertools.combinations(range(n),q))
        dist=Counter(); minimum=n
        for i,a in enumerate(sets):
            sa=set(a)
            for b in sets[i+1:]:
                k=len(sa.intersection(b)); dist[k]+=1; minimum=min(minimum,k)
        theoretical=2*q-n
        assert minimum==theoretical
        designated=set(range(theoretical)); example=None
        for i,a in enumerate(sets):
            sa=set(a)
            for b in sets[i+1:]:
                inter=sa.intersection(b)
                if len(inter)==theoretical and inter==designated:
                    example=(a,b,tuple(sorted(inter))); break
            if example: break
        assert example
        rows.append({
          "n":n,"f":f,"q":q,"quorum_sets":len(sets),
          "distinct_unordered_quorum_pairs":math.comb(len(sets),2),
          "minimum_intersection_observed":minimum,
          "minimum_intersection_formula":theoretical,
          "pairs_at_minimum_intersection":dist[theoretical],
          "intersection_distribution":";".join(f"{k}:{v}" for k,v in sorted(dist.items())),
          "max_double_signers_without_conflict_under_assumptions":theoretical-1,
          "state_erasure_recoveries_needed_after_f_byzantine":theoretical-f,
          "example_quorum_A":" ".join(f"W{x+1}" for x in example[0]),
          "example_quorum_B":" ".join(f"W{x+1}" for x in example[1]),
          "shared_double_signer_set":" ".join(f"W{x+1}" for x in example[2]),
          "result":"PASS"})
    return rows

def explicit_state_model(durable_before_release,recovery_mode,n=4,byzantine=frozenset({0}),quorum=3):
    # state=(durable choice, pending choice, status, A signer bitmask, B signer bitmask)
    # choice 0=NONE, 1=A, 2=B; status 0=ACTIVE, 1=DOWN, 2=QUARANTINED
    assert recovery_mode in {"RESET_ACTIVE","RESET_QUARANTINE","PRESERVE"}
    initial=((0,)*n,(0,)*n,(0,)*n,0,0)
    def conflict(s): return s[3].bit_count()>=quorum and s[4].bit_count()>=quorum
    def next_states(s):
        durable,pending,status,siga,sigb=s
        for w in range(n):
            if status[w]==0:
                for v in (1,2):
                    if pending[w]==0 and (w in byzantine or durable[w] in (0,v)):
                        d,p=list(durable),list(pending)
                        if durable_before_release and w not in byzantine: d[w]=v
                        p[w]=v
                        yield (tuple(d),tuple(p),status,siga,sigb),f"Prepare(W{w+1},{'A' if v==1 else 'B'})"
                p,st=list(pending),list(status); p[w],st[w]=0,1
                yield (durable,tuple(p),tuple(st),siga,sigb),f"Crash(W{w+1})"
            if status[w]==0 and pending[w] in (1,2):
                v=pending[w]; na=siga|(1<<w) if v==1 else siga; nb=sigb|(1<<w) if v==2 else sigb
                p=list(pending)
                if durable_before_release or w in byzantine: p[w]=0
                yield (durable,tuple(p),status,na,nb),f"Release(W{w+1},{'A' if v==1 else 'B'})"
            if status[w]==0 and not durable_before_release and w not in byzantine and pending[w] in (1,2):
                v=pending[w]; mask=siga if v==1 else sigb
                if mask&(1<<w):
                    d,p=list(durable),list(pending); d[w],p[w]=v,0
                    yield (tuple(d),tuple(p),status,siga,sigb),f"CommitAfterRelease(W{w+1},{'A' if v==1 else 'B'})"
            if status[w]==1:
                d,p,st=list(durable),list(pending),list(status); p[w]=0
                if recovery_mode=="RESET_ACTIVE": d[w],st[w]=0,0
                elif recovery_mode=="RESET_QUARANTINE": d[w],st[w]=0,2
                else: st[w]=0
                yield (tuple(d),tuple(p),tuple(st),siga,sigb),f"Recover({recovery_mode},W{w+1})"
    queue=deque([initial]); prev={initial:None}; action_to={}; terminal=None
    while queue:
        s=queue.popleft()
        if conflict(s): terminal=s; break
        for ns,action in next_states(s):
            if ns not in prev:
                prev[ns]=s; action_to[ns]=action; queue.append(ns)
                if len(prev)>500000: raise RuntimeError("state cap exceeded")
    path=[]
    if terminal is not None:
        cur=terminal
        while prev[cur] is not None: path.append(action_to[cur]); cur=prev[cur]
        path.reverse()
    return {"durable_before_release":durable_before_release,"recovery_mode":recovery_mode,
      "n":n,"byzantine_witnesses":[f"W{x+1}" for x in sorted(byzantine)],"quorum":quorum,
      "result":"COUNTEREXAMPLE" if terminal is not None else "NO_COUNTEREXAMPLE",
      "states_explored":len(prev),"counterexample_length":len(path),"counterexample":path}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--outdir",default="validation"); args=ap.parse_args()
    out=Path(args.outdir); out.mkdir(parents=True,exist_ok=True)
    l0=quorum_exhaustive()
    with (out/"WP024_L0_QUORUM_EXHAUSTIVE.csv").open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=list(l0[0])); w.writeheader(); w.writerows(l0)
    l1=[explicit_state_model(False,"RESET_ACTIVE"),explicit_state_model(True,"RESET_ACTIVE"),
        explicit_state_model(True,"RESET_QUARANTINE"),explicit_state_model(True,"PRESERVE")]
    expected=["COUNTEREXAMPLE","COUNTEREXAMPLE","NO_COUNTEREXAMPLE","NO_COUNTEREXAMPLE"]
    assert [x["result"] for x in l1]==expected
    summary=[
      {k:v for k,v in item.items() if k!="counterexample"} for item in l1]
    payload={"title":"Agent Ecology WP-024 L0/L1 bounded reference verification","date":"2026-11-15",
      "engine":"Python explicit-state breadth-first reference checker; not TLC",
      "scope":["L0 exhaustively enumerates all distinct unordered quorum pairs for n=4,7,10,13 and q=2f+1.",
      "L1 explores a finite single-origin, two-conflicting-checkpoint Witness state model with n=4, Byzantine={W1}, q=3.",
      "The model abstracts cryptographic validity, Merkle proofs, membership changes, correlated domains, network timing, and real storage semantics."],
      "l0":l0,"l1":summary,
      "interpretation":["For the fixed-member quorum model, the observed minimum intersection equals 2q-n=f+1 for all four parameter sets.",
      "With f Byzantine identities, one additional correct identity whose anti-double-sign state is erased while the original identity/key remains active can occupy the entire minimum intersection in a conflicting-certificate construction.",
      "Persist-before-release alone is insufficient if recovery can erase the durable state and reactivate the same identity.",
      "The bounded model found no conflicting quorum when state is preserved across recovery or an unproven state-erasing recovery is quarantined; this is not a proof for arbitrary protocols or implementations."],
      "tlc_status":"NOT_RUN","production_status":"NOT_AUTHORIZED"}
    (out/"WP024_L1_RECOVERY_MODEL_RESULTS.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    lines=["WP-024 L1 bounded explicit-state counterexample traces","Engine: Python BFS reference model; NOT a TLC result.",
      "Model: n=4, Byzantine={W1}, q=3; two conflicting checkpoint labels A and B.",""]
    for i,r in enumerate(l1,1):
        lines.append(f"[{i}] DurableBeforeRelease={r['durable_before_release']} RecoveryMode={r['recovery_mode']} => {r['result']} ({r['states_explored']} states)")
        lines.extend("  "+step for step in r["counterexample"]) if r["counterexample"] else lines.append("  No counterexample found in the bounded state space.")
        lines.append("")
    (out/"WP024_L1_UNSAFE_COUNTEREXAMPLE.txt").write_text("\n".join(lines),encoding="utf-8")
    print(json.dumps({"l0":[{k:r[k] for k in ("n","f","q","quorum_sets","distinct_unordered_quorum_pairs","minimum_intersection_observed","pairs_at_minimum_intersection")} for r in l0],
      "l1":[{k:r[k] for k in ("durable_before_release","recovery_mode","result","states_explored","counterexample_length")} for r in l1]},ensure_ascii=False,indent=2))

if __name__=="__main__": main()
