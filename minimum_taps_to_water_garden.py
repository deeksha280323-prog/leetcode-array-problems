class Solution:
    def minTaps(self, n, ranges):
        maxReach = [0] * (n + 1)

        for i in range(len(ranges)):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            maxReach[left] = max(maxReach[left], right)

        taps = 0
        curr_end = 0
        farthest = 0

        for i in range(n + 1):
            if i > farthest:
                return -1
            if i > curr_end:
                taps += 1
                curr_end = farthest
            farthest = max(farthest, maxReach[i])

        return taps
