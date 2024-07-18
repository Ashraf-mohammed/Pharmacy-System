import Medicine
import Supplier
import Customer

def medicine_menu():
    menu_choice = 0
    while menu_choice != 5:
        
        Medicine.show_menu()
        try:
            menu_choice = int(input("Enter your choice: "))
            match menu_choice:
                case 1:
                    Medicine.add_medicine()
                case 2:
                    Medicine.search_medicine()
                case 3:
                    Medicine.update_medicine()
                case 4:
                    Medicine.med_info()
                case 5:
                    exi = input("Are you sure you want to exit? Yes/No: ")
                    if exi.lower() == 'yes':
                        break
                    else:
                        menu_choice = 0 
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def supplier_menu():
    menu_choice = 0
    while menu_choice != 4:
        
        Supplier.show_info()
        try:
            menu_choice = int(input("Enter your choice: "))
            match menu_choice:
                case 1:
                    Supplier.search_supplier()
                case 2:
                    Supplier.add_supplier()
                case 3:
                    Supplier.update_supplier()
                case 4:
                    exi = input("Are you sure you want to exit? Yes/No: ")
                    if exi.lower() == 'yes':
                        break
                    else:
                        menu_choice = 0 
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def customer_menu():
    menu_choice = 0
    while menu_choice != 4:
        
        Customer.show_info()
        try:
            menu_choice = int(input("Enter your choice: "))
            match menu_choice:
                case 1:
                    Customer.search_customer()
                case 2:
                    Customer.add_customer()
                case 3:
                    Customer.update_customer()
                case 4:
                    exi = input("Are you sure you want to exit? Yes/No: ")
                    if exi.lower() == 'yes':
                        break
                    else:
                        menu_choice = 0 
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

