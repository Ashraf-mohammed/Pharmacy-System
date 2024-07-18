import Menu_Form

menu_choice = 0

while menu_choice != 6:
    print('##### Pharmacy Inventory System ####')
    print()
    print('-----------------------------')
    print("|Enter 1 for Pharmacy menu  |")
    print('----------------------------')
    print('|Enter 2 for Customer menu  |')
    print('----------------------------')
    print('|Enter 3 for Supplier menu  |')
    print('----------------------------') 
    print('|Enter 4 for Report menu    |')
    print('----------------------------')
    print('|Enter 5 for Invoicing      |')
    print('----------------------------')
    print('|Enter 6 to Exit program    |')
    print('-----------------------------')
    
    try:
        menu_choice = int(input("Enter your choice: "))
        match menu_choice:
            case 1:
                Menu_Form.medicine_menu()
            case 2:
                Menu_Form.customer_menu()()
            case 3:
                Menu_Form.supplier_menu()
            case 4:
                print("Hello from Report menu")
            case 5:
                print("Hello from Invoicing")
            case 6:
                exi = input("Are you sure you want to exit? Yes/No: ")
                if exi.lower() == 'yes':
                    break
                else:
                    menu_choice = 0 
            case _:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a valid number.")
