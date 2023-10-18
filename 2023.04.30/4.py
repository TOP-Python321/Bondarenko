data = {}

while True:
    try:
        line = input().strip()
        if not line:
            break
        num, value = line.split()
        data[value] = num
    except ValueError:
        pass
        
        
key = input().strip()
if key in data:
    print(data[key])
else:
    print("! value error !")
    
    
# 115 DATA_ELEMENT

# DATA_ELEMENT
# 115



# 22525 NON_DATA_ELEMENT

# DATA_ELEMENT
# ! value error !

