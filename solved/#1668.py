#1668. Maximum Repeating Substring

def maxRepeating(self, sequence: str, word: str) -> int:
    counter = sequence.count(word)
    c_word = counter * word
    while c_word not in sequence:
        counter -= 1
        c_word = counter * word
    return counter

sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"
print(maxRepeating(0, sequence, word))
