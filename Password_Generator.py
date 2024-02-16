import secrets

PasswordLength = input("Input Desired Password Length (Minimum 10 Characters): ")

# Whole function block is blank, when code is initially runs, because it is loaded in memory. 
    #Line 16 or below runs first, then function. 
# "length" is an arbitrary character, contains no values, it is blank intially. 

def generate_password(length):
    password = secrets.token_hex(int(PasswordLength)) # Generate a secure random string of alpha numeric characters
                                                      #  the "PasswordLength" value immediatley fills in all "length" with the user input.
    password = secrets.token_hex(length // 2)         # rounds down to the nearest whole number
        # Return the first `length` characters of the password
    return password 

randompassword = generate_password(int(PasswordLength)) #int removes decimals if any, and converts to int, to pass to "length". 
print(randompassword) 