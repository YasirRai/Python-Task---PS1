

class student:
    student_name = 'Abdul'
    marks = 74
    print("Student name before Modify function:", student_name)
    print("Student marks before Modify function: ", marks)


print('========================= MODIFY Function =====================================')
s = student()
s.student_name = 'Yasir'
print('Student name after Modify function:', s.student_name)
s.marks = 83
print('Student marks after Modify function:', s.marks)













class student:
    student_id = 1122               # Attributes of this Student class
    student_name = 'yasir'


s = student()
s.student_class = 'python class'        # Add NEW Attribute in Student class
print("The Value of  Student_id attribute is: ", s.student_id)
print("The Value of  Student_name attribute is: ", s.student_name)
print("Newly added Student_class attribute value is: ", s.student_class)

print("================= Deleting Attribute======")
s1 = student()
del s.student_name      # this will delete parameter
print("The Value of  Student_id attribute is: ", s.student_id)
print("Newly added Student_class attribute value is: ", s.student_class)
