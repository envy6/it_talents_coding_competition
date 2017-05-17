#!/usr/bin/python
# 05.05.2017
# Backpacker for it-talents code competition May 2017
# AUTHOR: Kevin Gomez Buquerin
# ALL RIGHTS RESERVED

# gets the user input
def user_interaction_items():
    print("[+] List an item like this: ITEMNAME:WEIGHT,VALUE ITEMNAME:WEIGHT,VALUE")
    print("[+] With ITEMNAME as the name of the item (string), WEIGHT as the weight of ONE item \
          (number in kg) and VALUE as the value of the corresponding item in EURO.")
    user_input = input("[+] Please list all the items in the provided form: ")
    return user_input

# checks user input
def user_input_checker(user_input_dict):
    flag = 0        # flag to determine if the user input was provided correctly; 0=false 1=true

# converts the user input into a dict
def user_input_handler(user_input):
    backpack_dict = {}
    user_input_splt = user_input.split()

    for item in user_input_splt:
        item_splt = item.split(":")
        backpack_dict[item_splt[0]] = item_splt[1]

    return backpack_dict

def  backpack_logic(backpack_items, max_weight):
    def get_best_value(i, j):
        if i == 0:
            return 0
        value, weight = backpack_items[i - 1]
        if weight > j:
            return get_best_value(i - 1, j)
        else:
            return max(get_best_value(i - 1, j),
                       get_best_value(i - 1, j - weight) + value)

    j = max_weight
    result = []
    for i in range(len(backpack_items), 0, -1):
        if get_best_value(i, j) != get_best_value(i - 1, j):
            result.append(backpack_items[i - 1])
            j -= backpack_items[i - 1][1]
    result.reverse()
    return get_best_value(len(backpack_items), max_weight), result

if __name__ == "__main__":
    # start here
    print("[*] Welcome to the backpacker.")
    # max_weight = input("[+] What's the maximal weight for your backpack? ")
    max_weight = 50  # debug value
    print("[-] Maximal weight for the backpack set to " + str(max_weight) + ".")

    # items = user_interaction_items()
    items = 'ab:12,34 cd:56,78'
    print("[d] Userinput: " + items + "...")

    items_dict = user_input_handler(items)
    print("[d] Dict: " + str(items_dict) + "...")

    backpack_items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2),(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
    a = backpack_logic(backpack_items, max_weight)
    print("[d] Logic calc: " + str(a))
