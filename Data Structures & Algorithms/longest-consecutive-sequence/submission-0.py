class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0

        for n in nums:
            #check if there is a left neighbour
            if (n - 1) not in numSet: #if not then its the start of a sequence
                newSequenceLength = 0 
                while (n + newSequenceLength) in numSet: # check if there is a right neighbour
                    newSequenceLength += 1 #if there is then update sequence length
                longestSequence = max(newSequenceLength, longestSequence) # update if the new sequence is longer

        return longestSequence

