def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Start Game")
        print("2. Options")
        print("3. Credits")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Starting the game...")
            # Call your game start function here
        elif choice == "2":
            print("Opening options...")
            # Call your options menu function here
        elif choice == "3":
            print("Showing credits...")
            # Show credits
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()