---------------- MODULE WitnessRecovery ----------------
EXTENDS Naturals, FiniteSets, TLC

CONSTANTS Witnesses, Byzantine, Quorum,
          DurableBeforeRelease, RecoveryMode

NoValue == "NONE"
Values == {"A", "B"}
Statuses == {"ACTIVE", "DOWN", "QUARANTINED"}

ASSUME
  /\ Witnesses # {}
  /\ Byzantine \subseteq Witnesses
  /\ Quorum \in 1..Cardinality(Witnesses)
  /\ DurableBeforeRelease \in BOOLEAN
  /\ RecoveryMode \in {"RESET_ACTIVE", "RESET_QUARANTINE", "PRESERVE"}

VARIABLES durable, pending, status, signatures
vars == <<durable, pending, status, signatures>>

Init ==
  /\ durable = [w \in Witnesses |-> NoValue]
  /\ pending = [w \in Witnesses |-> NoValue]
  /\ status = [w \in Witnesses |-> "ACTIVE"]
  /\ signatures = {}

TypeOK ==
  /\ durable \in [Witnesses -> (Values \cup {NoValue})]
  /\ pending \in [Witnesses -> (Values \cup {NoValue})]
  /\ status \in [Witnesses -> Statuses]
  /\ signatures \subseteq (Witnesses \X Values)

Prepare(w, v) ==
  /\ w \in Witnesses
  /\ v \in Values
  /\ status[w] = "ACTIVE"
  /\ pending[w] = NoValue
  /\ (w \in Byzantine \/ durable[w] \in {NoValue, v})
  /\ pending' = [pending EXCEPT ![w] = v]
  /\ IF DurableBeforeRelease /\ w \notin Byzantine
        THEN durable' = [durable EXCEPT ![w] = v]
        ELSE UNCHANGED durable
  /\ UNCHANGED <<status, signatures>>

Release(w, v) ==
  /\ w \in Witnesses
  /\ v \in Values
  /\ status[w] = "ACTIVE"
  /\ pending[w] = v
  /\ signatures' = signatures \cup {<<w, v>>}
  /\ IF DurableBeforeRelease \/ w \in Byzantine
        THEN pending' = [pending EXCEPT ![w] = NoValue]
        ELSE UNCHANGED pending
  /\ UNCHANGED <<durable, status>>

CommitAfterRelease(w, v) ==
  /\ w \in Witnesses \ Byzantine
  /\ v \in Values
  /\ ~DurableBeforeRelease
  /\ status[w] = "ACTIVE"
  /\ pending[w] = v
  /\ <<w, v>> \in signatures
  /\ durable' = [durable EXCEPT ![w] = v]
  /\ pending' = [pending EXCEPT ![w] = NoValue]
  /\ UNCHANGED <<status, signatures>>

Crash(w) ==
  /\ w \in Witnesses
  /\ status[w] = "ACTIVE"
  /\ status' = [status EXCEPT ![w] = "DOWN"]
  /\ pending' = [pending EXCEPT ![w] = NoValue]
  /\ UNCHANGED <<durable, signatures>>

Recover(w) ==
  /\ w \in Witnesses
  /\ status[w] = "DOWN"
  /\ CASE
       RecoveryMode = "RESET_ACTIVE" ->
         /\ durable' = [durable EXCEPT ![w] = NoValue]
         /\ status' = [status EXCEPT ![w] = "ACTIVE"]
     [] RecoveryMode = "RESET_QUARANTINE" ->
         /\ durable' = [durable EXCEPT ![w] = NoValue]
         /\ status' = [status EXCEPT ![w] = "QUARANTINED"]
     [] OTHER ->
         /\ UNCHANGED durable
         /\ status' = [status EXCEPT ![w] = "ACTIVE"]
  /\ pending' = [pending EXCEPT ![w] = NoValue]
  /\ UNCHANGED signatures

Next ==
  \/ \E w \in Witnesses, v \in Values : Prepare(w, v)
  \/ \E w \in Witnesses, v \in Values : Release(w, v)
  \/ \E w \in Witnesses, v \in Values : CommitAfterRelease(w, v)
  \/ \E w \in Witnesses : Crash(w)
  \/ \E w \in Witnesses : Recover(w)

Signers(v) == {w \in Witnesses : <<w, v>> \in signatures}
QuorumFor(v) == Cardinality(Signers(v)) >= Quorum

NoConflictingQuorums ==
  ~(QuorumFor("A") /\ QuorumFor("B"))

HonestNonEquivocation ==
  \A w \in (Witnesses \ Byzantine) :
    Cardinality({v \in Values : <<w, v>> \in signatures}) <= 1

Spec == Init /\ [][Next]_vars

=============================================================================
