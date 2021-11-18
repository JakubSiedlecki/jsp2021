import re
for num in range(100, 401): 
    if re.search(r'^[02468]+$', str(num)):
        print(str(num) + " ")