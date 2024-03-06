def factorial(num):
    a=1
    for i in num:
        a*=i
    return a
num=[1,2,3,4,5]
result=factorial(num)
print(result)