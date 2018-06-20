while True:
    print('Please Enter Your Age:')
    age = input()
    if age.isdecimal():
        break
    print('please Enter a number for your age')

while True:
    print('Please Enter Your Password:')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers')