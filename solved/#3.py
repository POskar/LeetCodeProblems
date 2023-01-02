#3. Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(self, s: str) -> int:
    chars = []
    max = 0
    length = 0
    for char in s:
        if char in chars:
            chars = chars[chars.index(char)+1::]
            chars.append(char)
            length = len(chars)
        else:
            chars.append(char)
            length += 1
            if length > max:
                max = length

    return max


s = "dvdf"
print(lengthOfLongestSubstring(0, s))