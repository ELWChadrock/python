class User:
    name = 'John Doe'
    email = 'johndoe@doe.com'
    password = 'blahblah'
    account = 0

class student(User):
    student_id = '456'
    major = 'english'

class teacher(User):
    teacher_id = '237'
    teacher_email = 'teachman@teacher.com'


user1 = User()
student1 = student()
teacher1 = teacher()

print(user1.name)
print(student1.name)
print(teacher1.teacher_id)
