import random
def get_names(nums:int=2)->list[str]:
    with open('names.txt',encoding='utf-8',mode='r') as file:
        names_str = file.read()
    names:list[str] = names_str.split(sep='\n')
    names = random.choices(names,k=nums)
    return names

#nums = int(input('請輸入學生數量(最多10位):'))
#student_names = get_names(nums=nums)
#for name in student_names:
#    print(name)


def generate_student(names):
    students=[]
    for name in names:
        chinese = random.randint(0,100)
        english = random.randint(0,100)
        math = random.randint(0,100)
        stu = {"name":name,"chinese":chinese,"english":english,"math":math}
        students.append(stu)
    return students

nums = int(input('請輸入學生數量(最多10位):'))
student_names = get_names(nums=nums)
students = generate_student(names=student_names)
print(students)
