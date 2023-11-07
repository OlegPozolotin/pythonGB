from functools import reduce
import operator

numbers = [x for x in range(100, 1001) if x % 2 == 0]

result = reduce(operator.mul, numbers)

print(result)
