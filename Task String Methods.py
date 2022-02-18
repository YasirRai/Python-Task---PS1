
# TASK 1 Ask user to enter his email that should have .com in the end
email = input('Enter Email ')
print("Your Email Address ", email)
print(email.endswith('.com'))

#Task 2

print('Hello!', input("Enter Your Name").title())
print("I hope You are Fine, let me know how can i help you !")
x = input("What is Problem")
x1 = 'thanks'
x2 = 'no thanks'
x3 = 'i dont need any help'
user = x == x1 or x == x2 or x == x3
print(user, "Okay! Good to see you , stay connected")

#task 3 ask user to enter his URL that should starts with http://www.( user url ) and then convert it into user url.com

url = input("Enter Your Websites ")      # Ask User to Enter URL
y = 'http://www.'                       # It Should start with
z = '.com'                               # URL will convert
print("Website is ", url + z)
print(url.startswith(y))              # result about start-with or Not


#Task 04   ask user to set your passwrd that should contain number , alphabets
password = input("Enter Password ")      # Ask from User
p1 = password.isdigit()                 # password should have digits
p2= password.isalpha()                  # Password Should Have alphabets
p3 = p1 == p2

print("Your Password is", password)
print(p3)