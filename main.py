from krav_maga_scenarios import push_from_behind,scenario_wrist_grab, knife_to_throat_from_side

def main():
    while True:
        print("\nChoose a scenario to practice:")
        print("1. Push from behind")
        print("2. scenario_wrist_grab")
        print("3. Knife to throat from side")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            push_from_behind()
        if choice == "2":
            scenario_wrist_grab()
        if choice == "3":
            knife_to_throat_from_side()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()