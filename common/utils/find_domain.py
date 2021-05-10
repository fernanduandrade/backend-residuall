import re 

def find_domain(email: str) -> str:
    return re.findall('(?<=@)[^.]+(?=\.)',email)[0]