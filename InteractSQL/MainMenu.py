from InteractSQL.Connect_SQL import connect_sql

class MainDis(connect_sql):
    def __init__(self):
        super().__init__()
        self.user_input = int

    def main_menu(self):
        while(self.user_input != 5):
            self.user_input = 0
            while(self.user_input == 0):
                print("\n1. Display all inventory items")
                print("2. search inventory items")
                print("3. manage intentory")
                print("4. Save Changes")
                print("5. Quit")
                try:
                    self.user_input = int(input("\nenter number: "))
                    if self.user_input < 1 or self.user_input > 5:
                        self.user_input = "a"
                        self.user_input = int(self.user_input)
                except:
                    print("ERROR invalid input\n")
                    self.user_input = 0
            self.run_choice_input()


    def run_choice_input(self):
        if self.user_input == 1:
            self.display_all()
        elif self.user_input == 2:
            self.find_item()
        elif self.user_input == 3:
            self.manage_inv()
        elif self.user_input == 4:
            self.save()
        else:
            self.exit()
        