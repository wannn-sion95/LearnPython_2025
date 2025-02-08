import re 

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"

    if re.match(pattern, email):
        return "Email valid dan cocok dengan sistem"
    else:
        return "Email tidak valid dengan sistem"

print(validate_email(input("Masukkan nama email: ")))
    
