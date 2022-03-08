import sqlite3

class connect_sql:
    def __init__(self):
        self.connection = sqlite3.connect("InteractSQL\datasql.db")
        self.dataBase = self.connection.cursor()

    def display_all(self):
        '''
        display all items
        '''
        for row in self.dataBase.execute('SELECT * FROM inventory ORDER BY id'):
            print('\nID: {}'.format(row[0]))
            print('Name: {}'.format(row[1]))
            print('Quantity: {}'.format(row[2]))
            print('Price: ${:.2f}\n'.format(row[3]))


    def find_item(self):
        '''
        finds items by ID or name
        '''

        # display menu
        search_cat = ""
        print("Enter how you want to search the item")
        print("Search by:")
        print("1. ID")
        print("2. Product Name")
        user_input = 0

        # get user input, check for errors
        while(user_input == 0):
            try:
                user_input = int(input("\nEnter a number: "))
                if user_input < 1 or user_input > 2:
                    user_input = "a"
                    user_input = int(user_input)
            except:
                print("ERROR invalid input\n")
                user_input = 0

        # assign a value
        if user_input == 1:
            search_cat = "id"
        elif user_input == 2:
            search_cat = "product"

        # ask for ID or name
        search_string = input("Enter {}: ".format(search_cat))

        # looks for item
        if user_input == 1:
            t = (int(search_string), )
        elif user_input == 2:
            t = (search_string.lower(), )
        self.dataBase.execute("SELECT * FROM inventory WHERE {} = ?".format(search_cat), t)
        results = self.dataBase.fetchone()

        # displays to user
        if results == None:
            print("\n\n***product not found***\n\n")
        else:
            print('\n\nID: {}'.format(results[0]))
            print('Name: {}'.format(results[1]))
            print('Quantity: {}'.format(results[2]))
            print('Price: ${:.2f}\n\n'.format(results[3]))


    def manage_inv(self):
        """
        manage inventory menu
        """
        choice = 0
        print('\n1. Add Item')
        print('2. Edit Item')
        print('3. delete Item')
        try:
            choice = int(input("Enter number: "))
        except:
            print("***invalid choice***")
            choice = 0

        # run function
        if choice == 1:
            self.add_item()
        elif choice == 2:
            self.edit_item()
        elif choice == 3:
            self.delete_item()
    

    def add_item(self):
        '''
        Added Item
        '''

        # create product ID
        self.dataBase.execute('SELECT id FROM inventory')
        results = self.dataBase.fetchall()
        id = len(results) - 1
        id = int(results[id][0])
        id = id + 1

        # aske for product data to be added
        name = input('Name: ')
        name = name.lower()
        quantity = int(input('Quantity: '))
        price = float(input('Price: '))
        values = (id, name, quantity, price)

        # check if product is in table
        t = (name, )
        self.dataBase.execute('SELECT * FROM inventory WHERE product = ?', t)
        results = self.dataBase.fetchone()
        if results == None:
            # add item
            self.dataBase.execute('INSERT INTO inventory VALUES (?,?,?,?)', values)
            print('\nAdded Item Successfully\n')
        else:
            print('\nItem already exists\n')


    def edit_item(self):
        '''
        Edit Item
        '''
        name = input("Enter Product Name to Edit: ")
        name = name.lower()

        # check if product is in table
        t = (name, )
        self.dataBase.execute('SELECT * FROM inventory WHERE product = ?', t)
        results = self.dataBase.fetchone()
        if results == None:
            print('\nItem Does Not Exists\n')
        else:
            # add item and error check
            try:
                quantity = int(input('Enter Quantity(NA if no change): '))
            except:
                quantity = results[2]

            try:
                price = float(input('Enter Price(NA if no change): '))
                print()
            except:
                price = results[3]
            
            # update Items
            values = (quantity, price, name)
            self.dataBase.execute('UPDATE inventory SET qty = ?, price = ? WHERE product = ?', values)
            print('\nUpdated Item Successfully\n')


    def delete_item(self):
        '''
        delete items
        '''
        name = input("Enter Product Name to Delete: ")
        name = name.lower()

        # check if product is in table
        t = (name, )
        self.dataBase.execute("SELECT * FROM inventory WHERE product = ?", t)
        results = self.dataBase.fetchone()
        if results == None:
            print('\nItem Does Not Exists\n')
        else:
            self.dataBase.execute("DELETE FROM inventory WHERE product = ?", t)
        
    def save(self):
        self.connection.commit()

    def exit(self):
        answer = input("would you like to save changes? (y/n): ")
        if answer.lower() != "n":
            self.connection.commit()
            print('Saved!')
        self.connection.close()
        print('Thankyou Goodbye!')