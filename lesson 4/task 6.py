import itertools


def integer_generator(start, end):
    for num in itertools.count(start):
        if num > end:
            break
        yield num


start_num = 3
end_num = 10

for num in integer_generator(start_num, end_num):
    print(num)
