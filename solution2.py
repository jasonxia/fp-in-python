import data
from functools import reduce

# This solution used global variable data.quize, which is not pure FP
def cal(student):
    filtered = filter(lambda x: x[0] == x[1][0], zip(student.ans, data.QUIZE))
    # [('A', ('A', 3)), ('D', ('D', 1)), ...]

    reduced = reduce(lambda x, y: x + y[1][1], filtered, 0)
    print(student.id, '\t', reduced)

print('ID\tScore\n==================')  
list(map(cal, data.students))
