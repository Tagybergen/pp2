def check_all_true(tuple_values):
    return all(tuple_values)

tuple1=(True,True,True)
tuple2=(True,False,True)
tuple3=(False,False,False)
result1=check_all_true(tuple1)
result2=check_all_true(tuple2)
result3=check_all_true(tuple3)
print("All elements in tuple1 are True", result1)
print("All elements in tuple2 are True", result2)
print("All elements in tuple3 are True", result3)