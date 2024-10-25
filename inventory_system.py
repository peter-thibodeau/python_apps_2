print('INVENTORY MANAGEMENT SYSTEM')

items = []

def add_item():
    """ Add a new item by creating and filling a new dictionary in the items list """
    dict = {}
    name = input("Enter the item name: ")

    for i in range(len(items)): # does that item already exist?
        if items[i]['NAME'] == name:
            print('Error: that item already exists.')
            return ''
        
    dict['NAME'] = name
    price = input("Enter the price of the item: ")
    dict['Price'] = price
    quantity = input("Enter the quantity of the item: ")
    dict['Quantity'] = quantity
    category = input("Enter the category of the item: ")
    dict['Category'] = category
    return dict

def view_inventory(indx):
    """ Display all items """
    if len(items) > 0:
        for indx, item in enumerate(items):
            for key, value in item.items():
                print(f"{key}: {value}")  # print dictionaries in items list
    else:
        print('Inventory is empty, press 1 to add an item.')

def remove_item(name_to_remove):
    for i in range(len(items)):
        if items[i]['NAME'] == name_to_remove:
            del items[i]
            break

def search_by_category(category_to_search):
    """ Find dictionary(s) in items list where category matches the search value """
    results = []
    for i in items:
        if i.get("Category") == category_to_search:
            results.append(i)
    print(f"Dictionaries where '{"Category"}' is '{category_to_search}':")
    for j in results:
        print(j)

# 1. add an item to inventory to start the program
print('To begin, enter an item into inventory')
item = add_item()
items.append(item)

while True:  # menu
    # get input
    menu = input(
        '\nMENU\nEnter:\n 1 to add another item\n 2 to update an item detail\n 3 to view inventory\n 4 to remove an item\n 5 to search by category\n 6 to quit ')
    try: # verify input is correct
        r = int(menu)
    except:
        print('Error! enter numbers 1 through 6 only')
        quit()

    # menu processing
    if menu == '1': # add item
        item = add_item()
        items.append(item)
    elif menu == '2': # update item
        pass
    elif menu == '3': # view inventory
        view_inventory(0)
    elif menu == '4': # remove item
        name_to_remove = input('Enter the name of the item you want to remove: ')
        remove_item(name_to_remove)
    elif menu == '5': # search by category
        category_to_search = input('Enter category to search: ')
        search_by_category(category_to_search)
    elif menu == '6': # quit program
        print('Goodbye')
        quit()