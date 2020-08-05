class Solution:
    def singleNumber(self, nums) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key



if __name__ == '__main__':
    nums = [4,1,2,1,2]
    a = Solution()
    rv = a.singleNumber(nums)
    print(rv)
