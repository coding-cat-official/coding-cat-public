You're building a support tool for clerks in Small Claims Court, where everything runs fast, cheap, and without a jury. In these cases, accurate testimony alignment is critical. Clerks don’t have time to judge who’s lying, but they do need to *flag* when multiple witnesses independently report the same keywords. This can help a judge later identify corroboration—or call out inconsistencies.

The rules of the system are bureaucratic, not judicial. The algorithm:
- Doesn’t care about the full testimony, only the stenographer's keyword lists.
- Ignores repetition: if a word appears five times in one transcript and once in another, it still only counts once.
- Doesn’t impose order: keywords can appear in any sequence.

Legal notes:
- Remember, **innocence is presumed until proven guilty**.
- Some testimonies will be vague or useless—just noise.
- You're not the judge, just a data technician.

Your job is to compare **two transcripts** (represented as lists of keywords) and return the list of keywords that appear in **both**. Don’t add anything. Don’t remove anything. Just mark where stories match.

*Note: This is about *surface-level keyword overlap*, not sentiment analysis, truthfulness scoring, or narrative reconstruction. You’re not that advanced yet.*
