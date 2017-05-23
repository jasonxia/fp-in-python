import data

def cal(students, quize):
    for student in students:
        sid = student.id
        score = 0
        for i in range(len(quize)):
            if quize[i][0] == student.ans[i]:
                score += quize[i][1]
        print(sid, '\t', score)

print('ID\tScore\n==================')
cal(data.students, data.QUIZE)
