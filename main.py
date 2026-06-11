from expx import EXPX

def main():
    expx = EXPX("", "", "1.0")
    
    expx.init()
    print(f"Initialization: {expx.response}")
    
    if expx.is_initialized:
        print(f"Variables loaded: {len(expx.variables)}")
        
        while True:
            print("\nEXPX Authentication System")
            print("1. Login")
            print("2. Register")
            print("3. Get Variable")
            print("4. Refresh Variables")
            print("5. Check Status")
            print("6. Exit")
            
            choice = input("\nSelect option: ")
            
            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                
                result = expx.login(username, password)
                if result.success:
                    print(f"Login successful! Welcome {result.user.username}")
                    print(f"Subscription: {result.user.subscription}")
                    print(f"Expiry: {result.user.expiry}")
                else:
                    print(f"Login failed: {result.message}")
                    
            elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
                license_key = input("License Key: ")
                
                result = expx.register(username, password, license_key)
                if result.success:
                    print("Registration successful!")
                else:
                    print(f"Registration failed: {result.message}")
                    
            elif choice == "3":
                var_name = input("Variable name: ")
                value = expx.get_variable(var_name)
                if value:
                    print(f"Value: {value}")
                else:
                    print(f"Failed: {expx.response}")
                    
            elif choice == "4":
                if expx.refresh_variables():
                    print("Variables refreshed successfully")
                else:
                    print(f"Failed: {expx.response}")
                    
            elif choice == "5":
                print(f"Initialized: {expx.is_initialized}")
                print(f"Logged in: {expx.is_logged_in}")
                print(f"App active: {expx.is_application_active}")
                print(f"Version correct: {expx.is_version_correct}")
                print(f"Server version: {expx.server_version}")
                if expx.is_logged_in and expx.user:
                    print(f"User: {expx.user.username}")
                    print(f"Subscription: {expx.user.subscription}")
                    
            elif choice == "6":
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice")

if __name__ == "__main__":
    main()

