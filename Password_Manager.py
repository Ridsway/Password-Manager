# class LoginSystem:
#     def __init__(self):
#         self.users = {}
#         self.logged_in_user = None

#     def register(self, username, password):
#         """Register a new user"""
#         if username in self.users:
#             print("Username already exists. Please choose a different username.")
#         else:
#             self.users[username] = password
#             print("User registered successfully.")

#     def login(self, username, password):
#         """Login to the system"""
#         if username in self.users and self.users[username] == password:
#             self.logged_in_user = username
#             print("Login successful.")
#         else:
#             print("Invalid username or password.")

#     def logout(self):
#         """Logout from the system"""
#         if self.logged_in_user:
#             self.logged_in_user = None
#             print("Logout successful.")
#         else:
#             print("You are not logged in.")

#     def display_menu(self):
#         """Display the main menu"""
#         print("\nLogin System Menu:")
#         print("1. Register")
#         print("2. Login")
#         print("3. Logout")
#         print("4. Exit")

# def main():
#     login_system = LoginSystem()
#     while True:
#         login_system.display_menu()
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             username = input("Enter username: ")
#             password = input("Enter password: ")
#             login_system.register(username, password)
#         elif choice == "2":
#             username = input("Enter username: ")
#             password = input("Enter password: ")
#             login_system.login(username, password)
#         elif choice == "3":
#             login_system.logout()
#         elif choice == "4":
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

users = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}
def username():
    username = input("Enter your username: ")
password = input("Enter your password: ")

def login():
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")
#test