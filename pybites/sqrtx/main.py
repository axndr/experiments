import math


def b_search(x: int) -> int:
    r = x
    while r * r > x:
        print(f'R: {r}')
        r = (r + x / r) // 2
    else:
        print(f'R: {int(r)}')
    return int(r)


if __name__ == '__main__':
    numbers = [0, 7, 8, 155, 1000, 1001]
    for i in numbers:
        answer = b_search(i)
        print(answer)
        print('-----------------')
