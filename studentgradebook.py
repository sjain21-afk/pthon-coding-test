student_grades={
    "allice" :85,
    "bob":92,
    "charlie":78,
    "Diana":95,
    "ethan":86

}


totalscore=0
for student in student_grades:
    totalscore+=student_grades[student]


classaverage=totalscore/len(student_grades)
print("class average is ", classaverage)


topstudent=max(student_grades)
lowstudent=min(student_grades)
print("tthe top score was",topstudent)
print("tthe bottom score was",lowstudent)



searchname=input("enter a students name to look up:")
result=student_grades.get(searchname,"not found in the student list")
print(result)