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



#  all mathametical problems doing at a time
num = int(input())
temp = 0
mul = 1
count = 0
min1 = 10
max1 = 0
sum1 = 0
while(num>0):
    temp  = num % 10
    if(temp>0):
        mul *= temp
    sum1 += temp
    count +=1
    if (min1>temp):
        min1 = temp
    if (max1 < temp):
        max1 = temp
    num = num //10
        
print("mul: ",mul)
print("count: ",count)
print("min: ",min1)
print("max: ",max1)
print("sum: ",sum1)
    
