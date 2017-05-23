import data
from functools import reduce
from fn.func import curried

@curried
def cal(quize, student):
    # filtered = filter(lambda x: x[0] == x[1][0], zip(student.ans, quize))
    # reduced = reduce(lambda x, y: x + y[1][1], filtered, 0)
    reduced = reduce(lambda x, y: x + y[1][1], filter(lambda x: x[0] == x[1][0], zip(student.ans, quize)), 0)
    print(student.id, '\t', reduced)

print('ID\tScore\n==================')
list(map(cal(data.QUIZE), data.students))
