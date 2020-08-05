class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        return [v + extraCandies >= max(candies) for v in candies]


if __name__ == '__main__':
    candies = [4,2,1,1,2]
    extraCandies = 1
    a = Solution()
    rv = a.kidsWithCandies(candies, extraCandies)
    print(rv)
