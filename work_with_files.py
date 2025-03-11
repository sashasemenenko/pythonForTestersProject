# file = open('text.txt', 'r')
# print(file.read())
# file.close()

# file = open('text2.txt', 'w')
# file.write("Hello, Python! It's Oleksandr here.")
# file.close()

try:
    with open('text3.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("The file text2.txt does not exist.")

with open('/Users/semenenko/Documents/Development/pythonForTestersProject/files/text.txt', 'r') as file:
    print(file.read())

