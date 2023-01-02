#9. Palindrome Number

def isPalindrome(self, x: int) -> bool:
    lst = list(map(str,str(x))) #[d for d in str(x)]
    return True if lst == lst[::-1] else False

x = 121
print(isPalindrome(0, x))