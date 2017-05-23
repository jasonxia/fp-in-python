import data
from functools import reduce
from fn import F, _
from fn.func import curried

@curried
def output(quize, student):
    cal = F() >> (filter, lambda x: x[0] == x[1][0]) >> (lambda r: reduce(_ + _[1][1], r, 0))
    print(student.id, '\t', cal(zip(student.ans, quize)))

print('ID\tScore\n==================')
list(map(output(data.QUIZE), data.students))
