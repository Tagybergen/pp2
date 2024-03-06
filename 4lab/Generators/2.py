def even(a):
    for i in range(0,a+1):
        if i%2==0:
            yield i
a=int(input())
even_n=even(a)
even_list=list(even_n)
print(*even_list,sep=",")
