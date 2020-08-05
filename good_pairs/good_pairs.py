# good_pairs.py


def numIdenticalPairs(nums) -> int:
    rv = 0
    for i, x in enumerate(nums):
        for a, y in enumerate(nums):
            if x == y and a < i:
                rv += 1
    return rv


if __name__ == '__main__':
    numbers = [1, 2, 3, 1, 1, 3]
    print(numIdenticalPairs(numbers))
