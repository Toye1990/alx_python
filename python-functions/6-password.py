def validate_password(password):
    #check password length
    passwordlength = len(password)
    if(passwordlength >= 8):
        return True
    for i in password:
        if(i.isupper()):
            return True
        elif (i.islower()):
            return True
        elif (i.isdigit):
            return True
        else:
            return False
    
    
print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))


