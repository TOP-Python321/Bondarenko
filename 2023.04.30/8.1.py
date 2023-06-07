files = input().strip().split("; ")

name_counts = {}
for file in files:
    parts = file.split(".")
    name = ".".join(parts[:-1])
    ext = "." + parts[-1] if len(parts) > 1 else ""
    
    if name not in name_counts:
        name_counts[name] = 1
        new_name = file
    else:
        count = name_counts[name]
        new_name = f"{name}_{count}{ext}"
        name_counts[name] += 1
    
print(new_name)



