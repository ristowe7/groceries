import sys

# Try and Except remove the KeyboardInterrupt error (hitting ctrl + c to break)
try:
    # building an empty list
    shopping_list = []
    # printing all available commands
    print('Available Commands:\n')
    print('SHOW - View your list')
    print('REMOVE - Remove item from list')
    print('DONE - Finish adding to list')
    print('HELP - View available commands\n')
    # the while loop runs until you break the program
    while True:
        # waiting for user input
        item = input('What would you like to add?\n').lower()
        if item in shopping_list:
            print('You already have that item.\n')
        elif item == 'show':
            print('Your current shopping list:')
            print('--------------------')
            for each in shopping_list:
                # for loop that goes through each index of the list
                print(each.capitalize())
            print('--------------------')
        elif item == 'remove':
            remove_item = input('remove which item?\n')
            # asks for an item to be removed
            # if the item exists in the list it is taken out
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print('\nRemoved ' + remove_item.capitalize() + '\n')
            else:
                print('That item isn\'t on your list.')
        elif item == 'help':
            print('Available Commands:\n')
            print('SHOW - View your list')
            print('REMOVE - Remove item from list')
            print('DONE - Finish adding to list')
            print('HELP - View available commands\n')
        elif item == 'done':
            print('Printing your shopping list...')
            print('--------------------')
            for each in shopping_list:
                print(each.capitalize())
            print('--------------------')
            # break exits the while loop
            break
        elif type(item) == str:
            shopping_list.append(item)
except KeyboardInterrupt:
    # Try and Except remove the KeyboardInterrupt error (hitting ctrl + c to break)
    print('Printing your shopping list...')
    print('--------------------')
    for each in shopping_list:
        print(each.capitalize())
    print('--------------------')
    sys.exit(0)
