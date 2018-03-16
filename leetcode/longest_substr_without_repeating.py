"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        map_ = dict()
        count = 0
        max_count = 0

        for i in xrange(1, n+ 1):
            if s[i - 1] not in map_ or map_[s[i - 1]] < i - count:
                map_[s[i - 1]] = i
                count += 1
            else:
                count = (i - map_[s[i - 1]])
                map_[s[i - 1]] = i

            max_count = max(max_count, count)

        return max_count
