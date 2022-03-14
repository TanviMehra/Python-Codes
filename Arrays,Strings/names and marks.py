def students(student_list,target):
    marks_dict={}
    out=[]
    seen=set()
    for name,marks in student_list:
        value= target-marks
        if value in marks_dict and marks_dict[value] not in seen:
            seen.add(name)
            seen.add(marks_dict[value])
            out.append([marks_dict[value],name])
        marks_dict[marks]=name
    return (out)

student_list=[['ron',50],['harry',100],['nurato',150],
              ['diego',0],['tommy',50],['jerry',100],['shikha',90],
              ['tenten',60],['sasuke',110],['gara',114]]
print(students(student_list,150))