import sys
grade_mark={'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
credit_sum=0
credit_sbj=0
for i in range(20):
    grade=list(sys.stdin.readline().split())
    if grade[2]!='P':
        credit_sum += float(grade[1])
        credit_sbj += (float(grade[1]) * grade_mark[grade[2]])

print(credit_sbj/credit_sum)