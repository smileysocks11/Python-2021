def get_login_name(first, last, idnumber):
    
    first1 = generate_login()
    last1 = generate_login()
    idnumber1 = generate_login()
    
    first1 = first[:2]
    last1 = last[:2]
    idnumber1 = idnumber[-3:]
    
    login = first1 + last1 + idnumber1
    
    return login

# ---------------------------------------------------------------------

def valid_password(password):
    
    upper = False
    lower = False
    numeric = False
    is_valid = False

    for character in password:
        if character.isupper():
            upper = True
        if character.islower():
            lower = True
        if character.isnumeric():
            numeric = True
            
    if len(password) >= 7:
        if upper == True:
            if lower == True:
                    if numeric == True:
                        is_valid = True
                        
    return is_valid
    
# ---------------------------------------------------------------------