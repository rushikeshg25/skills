---
name: easy-understanding
description: Write clear technical explanations and instructions using an ASD-STE100-inspired controlled style. Use proactively when explaining a technical concept, documenting a procedure, or simplifying dense technical prose. Also use for requests for STE, ASD-STE100, or simplified technical English. Preserve a requested voice; do not apply automatically to creative writing, quotations, or casual conversation.
metadata:
  author: rushikesh
---

# Easy Understanding

Make technical writing easy to understand on the first reading. Use the discipline of ASD-STE100 without presenting an approximation as formal compliance.

## Choose the strength

- **Default: practical STE.** Treat “80% of the way to ASD-STE100” as a preference for readable, direct prose, not a measurable score. Apply the rules below with natural transitions and necessary technical vocabulary.
- **Strict STE requested:** use the applicable edition's rules and approved dictionary if available. Preserve permitted technical names and verbs. If these references are unavailable, produce a best-effort rewrite and state that formal compliance is unverified. Do not invent dictionary approvals or certify conformance from memory.

Use the requested output format. This skill changes the writing, not the scope of the task or the destination of the result.

## Write the explanation

1. Identify the reader's question or action. Lead with the answer or the intended result. Infer the reader's level from context; define unfamiliar terms on first use.
2. Keep one main idea per sentence. Prefer short sentences, usually about 15–20 words, but do not split a condition from the action it controls just to meet a count. This is a practical target, not a statement of the complete standard.
3. Use one term for one meaning. Prefer common words and concrete verbs. Keep required domain terms, identifiers, units, and interface labels exact.
4. Name the actor and use active voice when the actor matters. For instructions, use an imperative verb. Put conditions before actions: “If the indicator is red, stop the pump.”
5. Use numbered steps for ordered actions. Give each step one main action and put prerequisites or warnings before the affected step. Keep explanatory context outside the action when that improves scanning.
6. Make references explicit. Replace ambiguous “it,” “this,” or “they” with the object name. Split long noun clusters and avoid idioms, ornamental synonyms, and unexplained abbreviations.
7. Preserve logic and certainty. Keep negation, exceptions, sequence, quantities, and distinctions such as “must,” “should,” “may,” and “can.” Do not turn correlation into causation or an estimate into a fact.

## Match the shape to the reader's task

For a factual question, give the answer and the necessary qualification. For a mechanism, explain the input, the important state change, and the output; use one small example before adding edge cases. For a procedure, state prerequisites, ordered actions, and the observable result. Do not turn a short answer into a tutorial.

Keep executable commands, API names, configuration keys, quoted text, and numeric precision intact when rewriting prose. Explain them beside the original when necessary. If a command is wrong, identify the correction separately instead of silently changing its behavior during a style edit.

Keep each condition with the action it governs. For example, “Retry only if the request is idempotent and the failure is transient” requires both conditions. Splitting this into independent advice must not make either condition optional.

When the source is ambiguous, preserve the uncertainty or ask the one question that resolves the meaning. Simpler wording must not select a technical interpretation the source does not establish.

## Check meaning before style

Compare the rewrite with the source or evidence. Can the reader identify who does what, under which conditions, and with what result? Check that simplification did not remove a necessary qualification or add an unsupported claim.

Return the explanation or rewrite itself. Add a terminology note only when it helps the reader. Explain compliance limits when strict compliance was requested; do not attach a style report to ordinary answers.

## Example

Before: “In the event that replication lag exceeds 30 seconds, operators should refrain from initiating failover unless the primary is unavailable.”

After: “If replication lag exceeds 30 seconds, you should not start failover unless the primary is unavailable.”

The recommendation, threshold, and exception remain intact. Shortening this to “Do not fail over when replication is slow” would lose these distinctions.
