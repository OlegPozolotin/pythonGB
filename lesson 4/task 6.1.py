import itertools

def list_repeater(lst, repeat_count):
    count = 0
    for item in itertools.cycle(lst):
        yield item
        count += 1
        if count == len(lst) * repeat_count:
            break

my_list = [1, 2, 3]
repeat_count = 3

for item in list_repeater(my_list, repeat_count):
    print(item)

