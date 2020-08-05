# shuffle_the_array.py


def shuffle(nums: list, n: int):
    a = []
    rv = []
    for _ in range(n):
        a.append(nums.pop(0))
    print(f'A: {a}')
    print(f'Nums: {nums}')
    for _ in range(n):
        rv.append(a.pop(0))
        rv.append(nums.pop(0))
    return rv


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = int(len(nums)/2)
    print(shuffle(nums, n))
    # [2,3,5,4,1,7]
