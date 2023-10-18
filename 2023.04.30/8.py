files = input().strip()

files_list = [f.strip() for f in files.split(";")]

counter = {}
for file_name in files_list:
    if file_name not in counter:
        counter[file_name] = 1
    else:
        counter[file_name] += 1
        
        
renamed_files = []

for file_name in files_list:
    if counter[file_name] == 1:
        renamed_files.append(file_name)
    else:
        suffix = "_" + str(counter[file_name])
        new_file_name = file_name.split(".")[0] + suffix + "." + file_name.split(".")[-1]
        counter[file_name] -= 1
        renamed_files.append(new_file_name)
        

for file_name in sorted(renamed_files):
    print(file_name)
    
    

