grocery_list = []

def more_items():
	keep_going = raw_input("Do you have more items? ")
	if keep_going.upper() == 'YES' or keep_going.upper() == 'Y':
		next_items()
	elif keep_going.upper() == 'NO' or keep_going.upper() == 'N':
		print "Here is your grocery list: %r" % grocery_list

def next_items():
	next_item = raw_input("What is the next item? ")
	if next_item in grocery_list:
		print "Item is already on the list."
		print grocery_list
		more_items()
	elif next_item not in grocery_list:
		grocery_list.append(next_item)
		print grocery_list
		more_items()

def main():
	list_item = raw_input("Enter item for list: ")
	grocery_list.append(list_item)
	more_items()


if __name__ == '__main__':
	main()
# def returns():
# def remove(): 


