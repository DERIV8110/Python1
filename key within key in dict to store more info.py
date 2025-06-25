emp={"john":{"age":24,"salary":20000},"diya":{"age":35,"salary":50000}}
 #   key     value                    key     value

for name in emp:
    print("emplyee",name,":")
    print("age:",str(emp[name]["age"]))   #employee age is printed from employee name key
    print("salary:",str(emp[name]["salary"]))    #employee salary is printed from employee name key