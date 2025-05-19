class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

        #  (Or)
        
        # res = s.split()
        # rev = ''
        # for i in res:
        #     rev = " ".join(res[::-1])
        # return rev