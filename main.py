import string



while True:
    user_inp = input("Enter Password: ")
    s1 = string.ascii_lowercase #the string module funtion that gives us all the lower case letters
    s2 = string.ascii_uppercase # the string module funtion that gives us the uppercase letters
    s3 = string.digits # the string module function that gives us all the digits
    s4 = string.punctuation # the function of string module that returns punctuations 
    if s1[0:5] or s2[0:5] or s3[0:5] or s4[0:5] in user_inp:
        print("Password Strong!")
    else:
        print("Password Weak!")    
