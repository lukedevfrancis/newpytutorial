from School import Student
from School import Course


s1 = Student("John", 19, 95)
s2 = Student("Max", 19, 75)
s3 = Student("Sam", 19, 65)


course = Course("Computer Science", 2)
course.add_student(s1)
course.add_student(s2)

print(course.get_avg_grade())
