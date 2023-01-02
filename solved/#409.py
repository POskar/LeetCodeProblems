#409. Longest Palindrome

import collections


def longestPalindrome(self, s):
    if len(s) <= 1:
        return len(s)
    s_c = collections.Counter(s)
    count, odds = 0, 0
    for ch, freq in s_c.items():
        if freq % 2 != 0:
            odds += 1
        count += freq
        
    return count-odds+1 if odds != 0 else count

s = "abccccdd"
print(longestPalindrome(0, s))
