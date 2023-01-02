#1790. Check if One String Swap Can Make Strings Equal

def areAlmostEqual(self, s1: str, s2: str) -> bool:
    bad = []
    if s1 == s2:
        return True
    
    for i in range(0,len(s1)):
        if s1[i] != s2[i]:
            bad.append(i)
    
    if len(bad) != 2:
        return False

    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

s1, s2 = "caa", "aaz"
print(areAlmostEqual(0, s1, s2))