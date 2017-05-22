#!/usr/bin/python
'''
22.05.2017
Backpacker for it-talents code competition May 2017
AUTHOR: Kevin Gomez Buquerin
ALL RIGHTS RESERVED
'''

# Colors for prints
class ansi:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'

'''
Function: user_interaction_items
Paramters: none
Return: items - items provided by the user
This function gets the user input and puts every item into a list.
'''
def user_interaction_items():
    print("{}[+]{} List an item like this: {}WEIGHT,VALUE,'ITEMNAME'{}".format(ansi.GREEN, ansi.END, ansi.BLUE, ansi.END))
    print("{}[+]{} With {}ITEMNAME{} as the name of the item (string, with single quotes), {}WEIGHT{} as the weight of ONE item (number in g) and {}VALUE{} as the value of the corresponding item in EURO.".format(ansi.GREEN, ansi.END, ansi.BLUE, ansi.END, ansi.BLUE, ansi.END, ansi.BLUE, ansi.END))
    print("{}[+]{} Example: {}12,3,ball 20,10,smartphone{} ...".format(ansi.GREEN, ansi.END, ansi.YELLOW, ansi.END))
    print("\n")
    print("{}[+]{} Press {}ENTER{} if you are finished with entering items.".format(ansi.GREEN, ansi.END, ansi.BLUE, ansi.END))

    items = []
    while 1:
        try:
            user_input = input("{}[+]{} Please add a new item: ".format(ansi.GREEN, ansi.END))
        except:
            break
        print("{}[+]{} Item {}".format(ansi.GREEN, ansi.END, ansi.BLUE) + str(user_input) +  "{} successfully added!".format(ansi.END))
        print("\n")

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
    
    # define Weight, Value and Name of the items
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
Function: main
Paramters: none
Return: none
Main Function for the Python Script.
'''
if __name__ == "__main__":
    print("{}[*]{} Welcome to the backpacker.".format(ansi.BLUE, ansi.END))

    # check for valid user input
    while True:
        try:
            max_weight = input("{}[+]{} What's the maximal weight for your backpack? ".format(ansi.GREEN, ansi.END))

            # check if the user provided an integer
            if isinstance(max_weight, int):
                print("{}[+]{} A maximum weight of {}".format(ansi.GREEN, ansi.END, ansi.BLUE) + str(max_weight) + "{} for your backpack, successfully added!".format(ansi.END))
                break
            else:
                print("{}[-]{} Please provide a number for the maximum weight of your backpack. Try again!".format(ansi.RED, ansi.END))
                print("\n")
        except:
                print("{}[-]{} Please provide a number for the maximum weight of your backpack. Try again!".format(ansi.RED, ansi.END))
                print("\n")
    print("\n")
    
    # get the items from the user
    items = user_interaction_items()
    print("\n")

    print("{}[+]{} You added the followeing items: {}".format(ansi.GREEN, ansi.END, ansi.BLUE) + str(items) + "{}.".format(ansi.END))
    print("\n")

    print("{}[+]{} Start to calculate the perfect way to pack your backpack...".format(ansi.GREEN, ansi.END))
    items_list, items = backpack_logic(items, max_weight)
    
    print("{}[+]{} Pack the following items: {}".format(ansi.GREEN, ansi.END, ansi.BLUE) + str(items_list) + "{}.".format(ansi.END))
    calculated_weight = get_weight_sum(items_list, items)
    
    print("{}[+]{} The optimal weight for the provided values is: {}".format(ansi.GREEN, ansi.END, ansi.BLUE) + str(calculated_weight) + "{}.".format(ansi.END))
