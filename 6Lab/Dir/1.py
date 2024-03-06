import os

def display_directory_contents(path):
    print()
    for item in os.listdir(path):
        print(item)

path = input("Введите путь к каталогу или файлу: ")

if os.path.exists(path):
    display_directory_contents(path)
else:
    print("Указанный путь не существует.")
