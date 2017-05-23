import random
from collections import namedtuple

Student = namedtuple('Student', ['id', 'ans'])

N_Questions = 25
N_Students = 20

def gen_random_list(opts, n):
    return [random.choice(opts) for i in range(n)]

answers = gen_random_list('ABCD', N_Questions)
scores = gen_random_list(range(1, 6), N_Questions)

QUIZE = list(zip(answers, scores))

students = [
        Student(_id, gen_random_list('ABCD', N_Questions))
        for _id in range(1, N_Students+1)
        ]

print(QUIZE)
print(students)
