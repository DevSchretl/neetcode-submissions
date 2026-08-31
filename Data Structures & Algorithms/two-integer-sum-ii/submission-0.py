class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(numbers)):
            if target - numbers[i] not in seen:
                seen[numbers[i]] = i
            else:
                return [seen[target - numbers[i]]+1, i+1]
        