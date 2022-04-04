# Function that accepts a string and calculate the number of upper case letters and lower case letters
def string():
    words = input("Enter your Data")
    lowercase = 0
    uppercase = 0
    for i in words:
        if i.islower():
            lowercase = lowercase + 1           # Calculate the Lowercase words
        elif i.isupper():
            uppercase = uppercase + 1           # Calculate the Uppercase words
    print("Number of lowercase characters is:", lowercase)
    print("Number of uppercase characters is:", uppercase)


string()
