# E-Mail Slicer
import re

def email_slicer(email):
    email_sliced = email.split('@')
    username = email_sliced[0].lower()
    domain = email_sliced[1]
    
    return f"Your Email: {email} when sliced we get, Username: {username} and Domain: {domain}."                               

def verify_email_format(email):
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

    if valid is not None:
        slice = email_slicer(email)
        return slice
    else:
        print(valid)
        return "Invalid Email Address."
    
email = input("Enter a valid email address: ")
print(verify_email_format(email))