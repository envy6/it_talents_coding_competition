#!/usr/bin/python
'''
17.05.2017
Backpacker for it-talents code competition May 2017
AUTHOR: Kevin Gomez Buquerin
ALL RIGHTS RESERVED
'''

# gets the user input
def user_interaction_items():
    print("[+] List an item like this: WEIGHT,VALUE,'ITEMNAME'")
    print("[+] With ITEMNAME as the name of the item (string, with single quotes), WEIGHT as the weight of ONE item (number in kg) and VALUE as the value of the corresponding item in EURO.")
    print("[+] Press ENTER if you are finished with entering items.")
    items = []
    i = 0
    while 1:
        i += 1
        try:
            user_input = input("[+] Please add a new item: ")
        except:
            break
        print("[+] Item " + str(user_input) +  " successfully added!")
        items.append(user_input)
    return items

# checks user input
def user_input_checker(user_input_dict):
    flag = 0        # flag to determine if the user input was provided correctly; 0=false 1=true

def backpack_logic(items, max_weight):
    def itemWeight(item): return item[0]
    def itemValue(item): return item[1]
    def itemName(item): return item[2]

    items_dict = {}
    for n_items in range(len(items)+1):
        for n_weight in range(max_weight+1):
            if n_items == 0:
                items_dict[n_items, n_weight] = 0
            elif itemWeight(items[n_items-1]) > n_weight:
                items_dict[n_items, n_weight] = items_dict[n_items-1, n_weight]
            else:
                items_dict[n_items, n_weight] = max(items_dict[n_items-1, n_weight], items_dict[n_items-1, n_weight-itemWeight(items[n_items-1])] + itemValue(items[n_items-1]))

    items_list = []
    n_items = len(items)
    n_weight = max_weight
    while n_items > 0:
        if items_dict[n_items, n_weight] == items_dict[n_items-1, n_weight]:
            n_items -= 1
        else:
            n_items -= 1
            items_list.append(itemName(items[n_items]))
            n_weight -= itemWeight(items[n_items])
    
    items_list.reverse()
    return items_list

if __name__ == "__main__":
    print("[*] Welcome to the backpacker.")
    # max_weight = input("[+] What's the maximal weight for your backpack? ")
    max_weight = 50  # debug value
    print("[+] Maximal weight for the backpack set to " + str(max_weight) + ".")

    items = user_interaction_items()
    print("[+] You added the followeing items: " + str(items) + ".")

    print("[+] Start to calculate the perfect way to pack your backpack!")
    result = backpack_logic(items, max_weight)
    print("[+] Pack the following items: " + str(result) + ".")
    # TODO: return the calculated weight too!
    # TODO: color the console output
