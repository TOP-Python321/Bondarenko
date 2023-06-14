def strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
        
        
    has_lower = False
    has_upper = False
    has_digit = False
    
    for char in password:
        if char.islower():
            has_lower = True
            
        elif char.isupper():
            has_upper = True
        
        elif char.isdigit():
            has_digit = True
           
    if not (has_lower and has_upper and has_digit):
        return False
        
    
    has_other = False 
    for char in password:
        if not char.isalnum():
            has_other = True
            break
            
    if not has_other:
        return False
        
    result = True
    
    return result
    


print(strong_password(input("")))


# aP3:kD_l3
# True

# password
# False
