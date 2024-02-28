
import csv

apartments = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('jurmala.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartments.append(row)

# remove header row
apartments.pop(0)

# print(apartments)

while True:
    print("1. Get apartments by sequence number")
    print("2. Top 10 by highest price")
    print("3. Top 10 by lowest price")
    print("4. 20 items, cheaper than price")
    print("5. 20 items, expensive than price")
    print("6. -- Filter of your choice --")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # https://www.w3schools.com/python/python_lists_access.asp
        number = int(input("write the apartsment number: "))
        print(apartments[number])
        pass
    elif choice == '2':
        # https://www.w3schools.com/python/python_lists_sort.asp
        def sort_price(apartments):
            return int(apartments[-1])
        apartments.sort(key = sort_price, reverse = True)
        print(apartments[:11])
       
    
        pass
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        def sort_price(apartment):
            return int(apartment[-1])
        apartments.sort(key = sort_price)
        print(apartments[:11])
        pass
    elif choice == '4':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        newlist = []
        our_choice = int(input("Please, write your limit: "))
        for apartment in apartments:
            if int(apartment[-1]) <= our_choice:
                newlist.append(apartment)
        print(newlist)
        pass
    elif choice == '5':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        newlist = []
        our_choice = int(input("Please, write your limit: "))
        for apartment in apartments:
            if int(apartment[-1]) >= our_choice:
                newlist.append(apartment)
        print(newlist)
        pass

    elif choice == '6':
        newlist = []
        our_choice = int(input("Please, write your limit: "))
        mode = input("Please, write what you need: higher(h) or lower(l): ")
        for apartment in apartments:
            if mode == "h":
                if int(apartment[-1]) >= our_choice:
                    newlist.append(apartment)
            if mode == "l":
                if int(apartment[-1]) <= our_choice:
                    newlist.append(apartment)
        rint(newlist)
        pass
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 7")

    print("==========================")


