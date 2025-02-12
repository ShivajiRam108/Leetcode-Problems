#  Simple Code It Will Be Give 100% beats.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip().split()
        return len(s1[len(s1)-1])
            

#  Taking input from the user


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip().split()
        return len(s1[-1])  # Simplified indexing


s = input("Enter a string: ")
solution = Solution()
result = solution.lengthOfLastWord(s)
print("Length of the last word:", result)
