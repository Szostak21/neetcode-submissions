class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        maxWindow, l, mostFreq  = 0, 0, 0

        for r in range(len(s)):
            cint = ord(s[r]) - ord("A")
            counts[cint] += 1
            mostFreq = max(mostFreq, counts[cint])

            while (r - l + 1) - mostFreq > k:
                counts[ord(s[l]) - ord("A")] -= 1
                l += 1
                mostFreq = max(mostFreq, counts[cint])

            maxWindow = max(maxWindow, r - l + 1)

        return maxWindow

