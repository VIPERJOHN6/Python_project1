class Hospital():

    def __init__(self, name, location):
            self.name = name
            self.location = location
            print("\n Welcome to Bowen")
    
    def register(self):
        gmail = input("Email: ")
        full_name = input("Username: ")
        password = input("Password: ")
        verify_password = input("Confirm password: ")

        if any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password):
            print("Successfully created an account")
        else:
            print("Wrong password or passwords do not match.")


    def login(self):
        Email = input("Enter your email: ")
        password = input("Enter your Password")
        if Email.islower() and any(c.isalpha() for c in Email) and any(c.isdigit() for c in Email):
            print(Email)
        else:
            print("Incorrect email format.")
        
        if any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password):
            print("Successfully created an account")
        else:
            print("Wrong password or passwords do not match.")

        
    
    def menu(self):
        while True:
            print("\n choose an option")
            print("\n 1.Login")
            print("\n 2.Register an account")

            option = input("Enter an option (1-2): ")

            if option == "1":
                print(">>>>>>>> BOWEN< <<<<<")
                self.login()
            elif option == "2":
                print(">>>>>>>> BOWEN< <<<<<")
                self.register()
            
            break

hospital = Hospital("Bowen Hospital", "Iwo")
hospital.menu()


