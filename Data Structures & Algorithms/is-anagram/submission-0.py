class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countChar = {}

        if len(s) != len(t):
            return False
        
        else:
            for char in s:
                if char in countChar:
                    countChar[char] += 1

                else:
                    countChar[char] = 1

            for char in t:
                if char in countChar:
                    countChar[char] -= 1
                    if countChar[char] < 0:
                        return False
                else:
                    return False

            return True