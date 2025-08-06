class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 
        for i in range(len(s)):
            cur_len = 0 
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break 
                seen.add(s[j])
                cur_len += 1 
            max_len = max(max_len , cur_len)
        return max_len
x = Solution()
print(x.lengthOfLongestSubstring("abcabcbb"))  #  3
print(x.lengthOfLongestSubstring( "bbbbb"))  # 1
print(x.lengthOfLongestSubstring("pwwkew"))  # 3 