#392. Is Subsequence

def isSubsequence(self, s: str, t: str) -> bool:
        for val in s:
            if not t.__contains__(val):
                return False

        return True

def isSubsequence(self, s, t):
    t = iter(t)
    return all(c in t for c in s)


s = "abc"
t = "ahbgdc"
print(isSubsequence(0, s, t))