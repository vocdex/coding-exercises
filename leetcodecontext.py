"""
You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new strings.

Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.
"""
import math
def rearrangeCharacters(s, target):
    """
    Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.
    """
    if len(s)<len(target):
        return 0

    count_in_s = [s.count(i) for i in target]
    count_in_target = [target.count(i) for i in target]
    counts=([i / j for i, j in zip(count_in_s, count_in_target)])

    return math.floor(min(counts))

print(rearrangeCharacters("ilovecodingonleetcode", "code"))
print(rearrangeCharacters("codecodecodecode", "code"))
print(rearrangeCharacters("codecodecodecode", "codecode"))
print(rearrangeCharacters("aabccc", "aaa"))
