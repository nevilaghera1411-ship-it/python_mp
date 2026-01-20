# 3. Write a program to enter marks of 4 subjects and display result (result shall include total, percentage and grade)

sub1 = float(input("Enter marks of subject 1: "))
sub2 = float(input("Enter marks of subject 2: "))
sub3 = float(input("Enter marks of subject 3: "))
sub4 = float(input("Enter marks of subject 4: "))

total = sub1 + sub2 + sub3 + sub4
percentage = total / 4

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 45:
    grade = "C"
elif percentage >= 33:
    grade = "D"
else:
    grade = "Fail"

print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
