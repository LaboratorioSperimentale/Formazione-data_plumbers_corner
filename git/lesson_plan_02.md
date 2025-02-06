# Task for today

1. Do you remember about Alice?
   Last time we wrote a simple script (`process_text.py`) that would:
	* read a filename from command line
	* read its content and count frequencies of words
	* save word frequency list in a tab-separated file

- Any doubts?
- Can we make something better? e.g., remove something from frequencies like symbols etc
- what if we start from the actual text?

1. Transform in a git repository

2. Upload on github!
   1. which files?
   2. documentation?
   3. README > markdown
   4. license?
   5. report on pipeline

3. Task for today (and maybe next time):
   * in `pipeline/srts` folder you will find subtitles for various movies
   * we want to compare frequencies in the original text and in subtitles and ultimately build a table like the one below:


| word  | text | movie1 | movie2 | movie3 | ... |
| ---   | ---  | ----   | ---    | ---    | --- |
| word1 | 10   |  15    | 67     | 23     | ... |
| word2 | 200  | 34     | 10     | 1      | ... |