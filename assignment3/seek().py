# Python code to explain the concept of seek() method in file handling
with open("record.txt","w") as f:
    f.write("Python is a programming language that is interpreted, object-oriented, and considered to be high-level.")

with open('record.txt', 'r') as file:
    content = file.read(10)
    print('First 10 characters:', content)

    file.seek(0)
    print('File pointer moved to the beginning.')
    
    content = file.read(5)
    print('First 5 characters after seek:', content)

    file.seek(24)
    print('File pointer moved to position 15.')

    content = file.read(5)
    print('5 characters from position 15:', content)
