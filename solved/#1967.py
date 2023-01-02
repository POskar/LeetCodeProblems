#1967. Number of Strings That Appear as Substrings in Word

from typing import List


def numOfStrings(self, patterns: List[str], word: str) -> int:
    counter = 0
    for pattern in patterns:
        if word.find(pattern) != -1:
            counter += 1

    return counter

patterns, word = ["a","abc","bc","d"], "abc"
print(numOfStrings(0, patterns, word))