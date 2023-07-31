def validate_password(password)
   
  if len(password) < 8:
    return False
  
  if not any(c.isupper() for c in password):
    return False
  
  if not any(c.islower() for c in password):
    return False
  
  if not any(c.isdigit() for c in password):
    return False
 
  if any(c == " " for c in password):
    return False
 
  return True
