#!/usr/bin/python
'''
17.05.2017
Backpacker for it-talents code competition May 2017
AUTHOR: Kevin Gomez Buquerin
ALL RIGHTS RESERVED
'''

'''
Function: user_interaction_items
Paramters: none
Return: items - items provided by the user
This function gets the user input and puts every item into a list.
'''
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

'''
Function: backpack_logic
Parameters: items - items provided by the user
            max_weight - max weight for the backpack
Result: items_list - list with the items for the backpack
        items - list with all the items provided by the user
This function solves the Knapsack problem. 
Check out: https://en.wikipedia.org/wiki/Knapsack_problem
'''
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
    return items_list, items

'''
Function: get_weight_sum
Parameters: items_list - list with the calcualted items for the backpack
            items - list with all the items provided by the user
Return: res - integer with the max weight for the provided values
The function calculates the optimal weight from the items in the backpack.
'''
def get_weight_sum(items_list, items):
    res = 0
    for i in range(0,len(items)):
        if items[i][2] in items_list:
            res += items[i][0]
    return res

'''
Function: input_checker
Parameters: prov_input - provided input to check validity
            check - what should be checked
Return: 
The function checks if a provied input is valid, depending on the flag. 
'''
def input_checker(prov_input, check):
    rtn = False
    if check == "int":
        if type(prov_input) is int:
            rtn = True
        else:
            print("[-] Provided value is incorrect! Type is not int.")
            rtn = False

if __name__ == "__main__":
    print("[*] Welcome to the backpacker.")
    max_weight = input("[+] What's the maximal weight for your backpack? "))
    # TODO check for integeger input
    #max_weight = 50  # debug value
    print("[+] Maximal weight for the backpack is set to " + str(max_weight) + ".")

    items = user_interaction_items()
    print("[+] You added the followeing items: " + str(items) + ".")

    print("[+] Start to calculate the perfect way to pack your backpack!")
    items_list, items = backpack_logic(items, max_weight)
    print("[+] Pack the following items: " + str(items_list) + ".")
    calculated_weight = get_weight_sum(items_list, items)
    print("[+] The optimal weight for the provided values is: " + str(calculated_weight) + ".")

    # TODO color the console output
