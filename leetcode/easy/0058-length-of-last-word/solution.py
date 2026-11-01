class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = s.strip().split()
        return len(st[-1]) if st else o