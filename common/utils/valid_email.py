import re

def is_valid_email(email: str) -> bool:

    valid_emails = ['.com.br', '.com', '.gov.br', '.org']

    result = (re.findall(r'(?=('+'|'.join(valid_emails)+r'))', email))

    return True if len(result) >= 1 else False 
