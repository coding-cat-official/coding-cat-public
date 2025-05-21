You're part of a content analysis team at a company that curates large volumes of user-submitted writing — blog posts, short stories, and personal journals. The company is experimenting with a new feature that automatically tags content based on stylistic patterns and linguistic quirks.

One request from the editorial team is to help identify unusually symmetrical writing, especially words or phrases that are the same forwards and backwards. They’ve given you a batch of strings and want a quick analysis to see how common these symmetrical patterns are across submissions.

Before the system can move to full-scale tagging, your job is to write a utility that scans through a list of textual entries and counts how many of them follow this mirrored pattern. Since formatting varies across submissions, you should disregard things like spacing and punctuation, and avoid being thrown off by inconsistent capitalization.

Your function should take in a list of strings and return the number of entries that fit the requested pattern. This count will be used to help estimate how often this stylistic device appears, which in turn will shape the tagging rules for future content.