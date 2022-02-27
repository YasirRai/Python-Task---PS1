# 1 Ask user to enter his email that should have .com in the end
data = input('email address ')
print(data.endswith('.com'))

# 2 User conversation

print ('Hello!', input('user name ').title())
print('I hope you are fine, let me know how can i help you ! ')
x= (input('User data  '))
if x == 'thanks':
    print('Okay! Good to see you , stay connected')
else:
    print('We will resolve your problem')

# 3 http://www.( user url ) and then convert it into user url.com
print('http://www.', input('url').__add__('.com'))

# 4  passwrd that should contains number, alphabets

pswrd = input('enter your password')
pswrd = pswrd.isalpha() and pswrd.isdigit()
print('your password is ', pswrd)
