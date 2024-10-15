import csv

def print_food_items():
    try:
        with open('foodData.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            print("Current Food Items:")
            for row in reader:
                print(f"{row['food_item']}: available at {row['location']}.")
    except FileNotFoundError:
        print("No food items available.")

def main():
    while True:
        print_food_items()
        # Implement reservation functionality if desired
        
        continue_input = input("Do you want to continue viewing? (Y/N) ")
        if continue_input.lower() != "y":
            break

if __name__ == "__main__":
    main()
