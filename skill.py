with open ('example.txt', 'w') as file:
    file.write('new one \n')


with open ('example.txt', 'r') as file:
    content =  file.read()
    print(content)
