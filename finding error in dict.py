dic1={"age":25,'name':"xyz","salary":23450.5}
val=dic1["age"]
if val in dic1.values():      #error rectified>> if val in dic1: to if val in dic1.values():
    print("exists")
else:
    print("dne")