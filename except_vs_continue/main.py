def continue_func(x: int):
    for x in range(10):
        if x == 10:
            continue
        print(10)
    for x in range(10):
        if x == 10:
            continue
        print(10)

def break_func(x: int):
    for x in range(10):
        if x == 10:
            break
        print(10)

if __name__ == '__main__':
    for x in range(15):
        try:
            assert x == 10
            print(f'{x} == 10')
        except AssertionError as error:
            print(f'{x} != 10')