source_file = "source.txt"
destination_file = "destination.txt"

with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
    destination.write(source.read())
