name, mark1, mark2, mark3 = input().split(",")
mark = [float(mark1.strip()),float(mark3.strip()),float(mark3.strip())]

total = sum(mark)
percent = (total/300)*100
percentage = round(percent,1)

if percentage >= 75:
    grade = 'A'
elif percentage >= 60 and percentage < 75:
    grade = 'B'
elif percentage >=40 and percentage < 60:
    grade = 'C'
elif percentage < 40:
    grade = 'F'

print (f"{name} \nTotal: {int(total)}/300 \nPercentage: {percentage}% \nGrade: {grade}")