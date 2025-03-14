# Solutions:

## Slide 14
1. Match:
   1. A word of at least two alphabetical tokens followed by colon
      1. \b\w{2,}:
   2. A word of at most eight alphabetical tokens followed by colon, possibly separated by whitespace
      1. \b\w{1,8} ?:
   3. Words starting with capital `P` at the beginning of the line
      1. ^P\w*\b
   4. Lines containing at most 3 words and ending with a question mark
      1. ^\w*\s?\w*\s?\w*\?$
   5. The name of a pdf file with its extension (hint: what caracters can be part of a filename? Ignore whitespaces)
      1. \b\w+\.pdf\b
   6. IP addresses: (for example, `192.178.0.21`. If you want to overcomplicate things, IP addresses can have values between `0.0.0.0` and `255.255.255.255`)
      1. \b\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?\b
      2. \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b
      3. Issue: how can we prevent it from matching
   7. A number (integer or float)
      1. \b\d+,?\d*
   8. Dates (espressed as DD/MM/YYYY or DD month YYYY)
      1. \d
   9.  Only valid roman numbers between 1 and 10 (try to make is as compact as possible!)
   10. A word containing two or more contiguous `n`s (e.g., `anno`, `cannone`...)
   11. A word containing at least two `n`s, not necessarily contiguous (e.g., `nano`, `panettone`...)

2. Replace:
   1. Integers with the string `@NUM_INT` and floats with the string `@NUM_DEC`
   2. Remove spaces at the beginning or end of line