# Created by Aashish Adhikari at 3:43 PM 1/6/2021

'''
Time Complexity:
TC1 of creating cumul = O (max element of input)
TC2 of fillim cumul array = O (n) where n is the length of the input array
TC3 of for loop at the end  = O (max element)

TC = max (TC1, TC2, TC3)

Space Complexity: O(Max element)



'''

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        # find the max
        maximum = max(nums)

        # create a cumulative array for each element in nums
        cumul = [0 for idx in range(0, maximum + 1)]

        # fill in the cumulative sum of each element in the corresponding index
        for idx in range(0, len(nums)):
            elem = nums[idx]
            cumul[elem] += elem


        # Instead of a dp table
        #         dp = [[0, 0] for idx in range(0, len(cumul))]

        #         dp[0][1] = cumul[0]

        #         for idx in range(1, len(dp)):

        #             dp[idx][0] = max(dp[idx-1][0], dp[idx-1][1])
        #             dp[idx][1] = dp[idx-1][0] + cumul[idx]

        #         return max(dp[-1][0], dp[-1][1])


        # Use variables

        skip, take = 0, 0
        for idx in range(1, len(cumul)):
            temp = skip
            skip = max(skip, take)
            take = temp + cumul[idx]

        return max(skip, take)
