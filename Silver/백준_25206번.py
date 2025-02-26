N = 20
#과목 평점과 학점 대응
alphabet = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
mark = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
grade_char = dict(zip(alphabet, mark))
#딕셔너리 찍는게 귀찮을까 이게 귀찮을까까
#학점 * 과목평점 / 학점의 총합
sum_grade, sum_credit = 0, 0
for i in range(N):
    subject, credit, grade = input().split()
    if grade != 'P':
        credit = float(credit)
        sum_grade += grade_char[grade]*credit
        sum_credit += credit
gpa = sum_grade / sum_credit
print(gpa)
