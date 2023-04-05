#importing required library
#Tabulate is used to print tabular data in nicely formatted tables.
from tabulate import tabulate

#========The beginning of the class==========


class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """
    Initializes the class with the given parameters.

    Parameters:
    country (str): The country of the shoe.
    code (str): The code of the shoe.
    product (str): The name of the shoe.
    cost (float): The cost of the shoe.
    quantity (int): The quantity of the shoe.
    """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """
    Returns the cost of the shoe.
    """
        return self.cost
       
    def get_quantity(self):
        """
    Returns the quantity of the shoe.
    """
        return self.quantity
       
    def __str__(self):
        """
    Returns the string representation of the shoe object.
    """
        return f'{self.code} - {self.product} ({self.country})'
        
#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============

def read_shoes_data():
    """
Reads data from the 'inventory.txt' file and stores it in the shoe_list.
Raises:
    FileNotFoundError: If the file is not found.
    ValueError: If there is invalid data in the file.
"""
    try:
        with open('inventory.txt', 'r') as file:
            # skip the first line
            next(file)
            for line in file:
                data = line.strip().split(',')
                country, code, product, cost, quantity = data
                cost, quantity = float(cost), int(quantity)
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    except FileNotFoundError:
        print('File not found!')
        print()
    except ValueError:
        print('Invalid data in the file!')
        print()
    
    
def capture_shoes():
    """
Captures the details of the shoe from the user and adds it to the shoe_list.
"""
    country = input('Enter the country of origin: ')
    code = input('Enter the shoe code: ')
    product = input('Enter the shoe product name: ')
    cost = float(input('Enter the cost of the shoe: '))
    quantity = int(input('Enter the quantity of shoes: '))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print('Shoe added successfully!')
    print()
   
def view_all():
    """
Displays all the shoe details in a tabular format.
"""
    data = [[shoe.code, shoe.product, shoe.country, shoe.cost, shoe.quantity] for shoe in shoe_list]
    headers = ['Code', 'Product', 'Country', 'Cost', 'Quantity']
    print(tabulate(data, headers=headers, tablefmt='fancy_grid'))
    print()
    
def re_stock():
    """
Displays the shoe with the lowest quantity and allows the user to add more quantity to it.
Updates the quantity in the 'inventory.txt' file.
"""
    shoe = min(shoe_list, key=lambda x: x.quantity)
    print(f'{shoe} needs to be re-stocked.')
    print()
    choice = input('Do you want to add more shoes to the stock? (Y/N)').upper()
    if choice == 'Y':
        quantity = int(input(f'Enter the quantity of {shoe.product} to add: '))
        shoe.quantity += quantity
        with open('inventory.txt', 'a') as file:
            file.write(f'\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}')
        print('Stock updated successfully!')
        print()
    
def seach_shoe():
    """
Searches for a shoe with the given code and displays its details.
"""
    code = input('Enter the shoe code to search: ')
    for shoe in shoe_list:
        if shoe.code == code:
            print(f'Shoe details: {shoe}')
            print()
            return
    print('Shoe not found!')
    print()

def value_per_item():
    """
Displays the value of each shoe based on its cost and quantity.
"""
    data = [[shoe.product, shoe.cost, shoe.quantity, shoe.cost*shoe.quantity] for shoe in shoe_list]
    headers = ['Product', 'Cost', 'Quantity', 'Value']
    print(tabulate(data, headers=headers, tablefmt='fancy_grid'))
    print()
    

def highest_qty():
    """
Displays the shoe with the highest quantity.
"""
    shoe = max(shoe_list, key=lambda x: x.quantity)
    print(f'The product with highest quantity is {shoe}')
    print()
    

#==========Main Menu=============
# Getting the user's choice
while True:
    print("********* MAIN MENU ********")
    print('1. Read Shoes Data From File')
    print('2. Capture Shoes')
    print('3. View All Shoes')
    print('4. Re-stock Shoes')
    print('5. Search Shoe')
    print('6. Value Per Item')
    print('7. Product With Highest Quantity')
    print('8. Exit')

    choice = input('Enter your choice (1-8): ')

    # Executing the corresponding function based on the user's choice
    if choice == '1':
        read_shoes_data()
    elif choice == '2':
        capture_shoes()
    elif choice == '3':
        view_all()
    elif choice == '4':
        re_stock()
    elif choice == '5':
        seach_shoe()
    elif choice == '6':
        value_per_item()
    elif choice == '7':
        highest_qty()
    elif choice == '8':
        print('Thank you for using the Nike Shoe Inventory System. Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.')