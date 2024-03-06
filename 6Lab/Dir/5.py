my_list = ['яблоко', 'банан', 'апельсин']
with open('file.txt', 'w') as file:
    for item in my_list:
        file.write(item + '\n')

print('file.txt')
