import copy

master_string = input("master_string: ")

while True:
    master_string_copy = copy.deepcopy(master_string)
    user_input = input("Enter string: ")
    char_exist = []

    if not user_input:
        continue

    for char in user_input:
        if char in master_string_copy:
            char_exist.append(True)
            master_string_copy = master_string_copy.replace(char,"",1)
        else:
            char_exist.append(False)
            
    if False not in char_exist:
        master_string = copy.deepcopy(master_string_copy)
        print("Yes")
    else:
        print("False")
        
