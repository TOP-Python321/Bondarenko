first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

if second_list == [] or second_list == first_list:
    print("да")
else:
    for i in range(len(first_list) - len(second_list) + 1):
        if first_list[i:i+len(second_list)] == second_list:
            print("да")
            break
    else:
        print("нет")
        
# 1 2 4 5
# 4 5
# да

# 1 2 5 4
# 4 5
# нет

