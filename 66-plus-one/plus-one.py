class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
     num = int(''.join(map(str, digits))) + 1
     rs = [int(d) for d in str(num)]
     return rs