# time: n, space: 1
class Solution:
    def anagram(self, s, t):
        count = [0] * 256
        for c in s:
            count[ord(c)] += 1
        for c in t:
            count[ord(c)] -= 1
        return all(_ == 0 for _ in count)


# time: nlgn, space: 1 assume sorting algorithm is in place
class Solution2:
    def anagram(self, s, t):
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    import Test

    Test.test((Solution().anagram, Solution2().anagram), [
        (('abcd', 'dcab'), True),
    ])
