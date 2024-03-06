import os
def test(path):
    if os.path.exists(path):
        print(f"The path exists.")
        file = os.path.basename(path)
        dir = os.path.dirname(path)
        print(f"Filename: {file}")
        print(f"Directory: {dir}")
    else:
        print("The path does not exist.")

path = input()
test(path)