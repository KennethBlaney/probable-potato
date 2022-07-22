#%%
import re
from collections import Counter

#%%
def word_frequency(string):
    string = re.sub("\W+'", ' ', string)
    string = re.split(r" ", string)
    print(Counter(string).most_common())


#%%
#word_frequency("This module provides regular expression matching operations similar to those found in Perl. Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that is, you cannot match a Unicode string with a byte pattern or vice-versa; similarly, when asking for a substitution, the replacement string must be of the same type as both the pattern and the search string. Regular expressions use the backslash character ('\') to indicate special forms or to allow special characters to be used without invoking their special meaning. This collides with Python’s usage of the same character for the same purpose in string literals; for example, to match a literal backslash, one might have to write '\\\\' as the pattern string, because the regular expression must be \\, and each backslash must be expressed as \\ inside a regular Python string literal. Also, please note that any invalid escape sequences in Python’s usage of the backslash in string literals now generate a Deprecation Warning and in the future this will become a SyntaxError. This behaviour will happen even if it is a valid escape sequence for a regular expression")

#%% 
if __name__ == "__main__":

    word_frequency("Let's Go Brooklyn!")

# %%
