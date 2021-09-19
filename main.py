import string

while True:
    user_inp = str(input("Enter Password: "))

    s1 = string.ascii_lowercase 
    s2 = string.ascii_uppercase 
    s3 = string.digits 
    s4 = string.punctuation 



    if s1[0:2] and s2[0:2] and s3[0:2] and s4[0:2] in user_inp:
        print("Password Strong!")
    elif len(user_inp) == 8 or len(user_inp) > 8:
        print("Password Strong!")    
    else:
        print("Password Weak!")   

