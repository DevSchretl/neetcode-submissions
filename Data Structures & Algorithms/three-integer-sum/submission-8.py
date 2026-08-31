class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triples = set()
        seen = {}

        nums.sort()

        for i in range(len(nums)):
            
            if nums[i] == nums[i-1] and i != 0:
                continue

            target = -nums[i]

            for j in range(i, len(nums)):

                if i != j:
                    
                    if target - nums[j] in seen:
                        triples.add(tuple([nums[i], nums[j], target - nums[j]]))
                        seen.pop(target - nums[j])
                    else:
                        seen[nums[j]] = j
            
            seen = {}

        nodupes = []

        
        return [list(i) for i in triples]