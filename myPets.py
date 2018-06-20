catNames = ['Thomas', 'Hilda', 'Eric', 'Chloe', 'Tyra']
print('Enter cat Name:')
name = input()
if name not in catNames:
    print('I do not have a cat named ' + name)
else:
        print(name + ' is my cat pet')
