def find_other_CKs(attribute, dependency_dict):
    # print("in")
    output_list = []
    for key_temp in attribute:
        for key in dependency_dict:
            for value in dependency_dict[key]:
                if value == key_temp:
                    # print('ys')
                    attribute = key + attribute[1:]
                    output_list.append(attribute)

    return output_list


def check_candidate(key, fixed_all_key_list_, dependency_dict, out_list = []):
    # print("in_")
    # print(key)
    if len(fixed_all_key_list_) == len(out_list):
        # print("in")
        # print("outlist")
        # print(out_list)
        return True


    else:
        # print('no')
        if key not in out_list:
            out_list.append(key)
            # print("N1")

        if key in dependency_dict:
            for attribute in dependency_dict[key]:
                #attribute = dependency_dict[key][0]
                if attribute not in out_list:
                    out_list.append(attribute)
                    return check_candidate(attribute, fixed_all_key_list_, dependency_dict, out_list)


        else:
            if len(fixed_all_key_list_) == len(out_list):
                #print("in")
                return True
            else:
                # print("out list")
                # print(out_list)
                return False




file_input = open("input.txt", "r")
# print(file.read())
line_dict = dict()
dependency_dict = dict()  ##### dependencies added.
All_key_list = []
dependency_list = []
fixed_all_key_list = []
fixed_prime_attribute_list = []
dependent_attribute_list = []
alpha_list = []

### Separating Lines into a dictionary
line_num = 0
for line in file_input:
    line_dict[line_num] = line
    line_num += 1

file_input.close()
### Storing all dependencies in a python List
char_ind = 0
dependency = ""
while char_ind < len(line_dict[1]):
    char = line_dict[1][char_ind]
    char_ind += 1

    if char == "," or char == '\n':
        dependency_list.append(dependency)
        dependency = ""
    elif char == " ":
        continue
    else:
        dependency += char


### Storing all dependencies in a python Dictionary according to the dependee attributes as key values
for dependency in dependency_list:
    ok = 0
    dependee_attribute = ""
    dependent_attribute = ""
    for char in dependency:
        if 65 <= ord(char) <= 90:
            if ok == 0:
                dependee_attribute += char
            else:
                dependent_attribute += char
        else:
            ok = 1
    
    if dependee_attribute in dependency_dict:
        dependency_dict[dependee_attribute].append(dependent_attribute)
    else:
        dependency_dict[dependee_attribute] = [dependent_attribute]
#     print(dependee_attribute)
    
# if dependee_attribute in dependency_dict:
#     dependency_dict[dependee_attribute].append(dependent_attribute)
# else:
#     dependency_dict[dependee_attribute] = [dependent_attribute]

# print(dependency_list)
# print(dependency_dict)

### Finding the dependent attributes(D.A.) storing in dependent_attribute_list 
for attribute in dependency_dict:
    for dependent_attribute in dependency_dict[attribute]:
        if dependent_attribute not in dependent_attribute_list:
            dependent_attribute_list.append(dependent_attribute)

# print(dependent_attribute_list)

ok=0

# Add all attributes in All_key_list
dependee_attribute = ""
# print(line_dict[0])
for key in line_dict[0]:
    if key == "(" or key == 'R':
        ok = 1
        continue

    if 65 <= ord(key) <= 90 and ok == 1:
        dependee_attribute += key 
    else:
        if dependee_attribute not in All_key_list:
            All_key_list.append(dependee_attribute)
            dependee_attribute = ""

    if key == ")":
        break


for key in All_key_list:
    fixed_all_key_list.append(key)
# print("all key list")
# print(All_key_list)
# Chek FIRST CK
for attribute in dependency_dict:
    if attribute not in fixed_prime_attribute_list and attribute in All_key_list:
        fixed_prime_attribute_list.append(attribute)
        # print(fixed_prime_attribute_list)
        for dependent_attribute in dependency_dict[attribute]:
            if dependent_attribute in All_key_list:
                All_key_list.remove(dependent_attribute)


# print("fixed_primie_attribute_list")
# print(fixed_prime_attribute_list)
modified_prime_attribute_list = []
# print(fixed_all_key_list)
### Checking its subsets whether they ar C.K's
for key in fixed_prime_attribute_list:
    if check_candidate(key, fixed_all_key_list, dependency_dict, []) == True:
        modified_prime_attribute_list.append(key)
    else:
        # print("no")
        pass    

if modified_prime_attribute_list == []:
    modified_prime_attribute_list = fixed_prime_attribute_list.copy()
# print(dependency_dict)
# print(All_key_list)
# print("modified_prime_attribute_list")
# print(modified_prime_attribute_list)


##### Check Alpha
for attribute in modified_prime_attribute_list:
    if attribute in dependent_attribute_list:
        alpha_list.append(attribute)

# print("alpah list")
# print(alpha_list)


### Find other CK's
new_modified_prime_attribute_list = modified_prime_attribute_list.copy()
if alpha_list == []:
    # print(new_modified_prime_attribute_list)
    pass

else:
    for key in modified_prime_attribute_list:
        output = find_other_CKs(key, dependency_dict)
        for attribute in output:
            new_modified_prime_attribute_list.append(attribute)
    # print(new_modified_prime_attribute_list)


file_output = open("output.txt", "w")
ck_num = 1
file_output.write(f"There are total {len(new_modified_prime_attribute_list)} possible CKs. They are given below: \n\n")
for ck in new_modified_prime_attribute_list:
    file_output.write(f"CK{ck_num}: {ck} \n")
    ck_num += 1

file_output.close()
