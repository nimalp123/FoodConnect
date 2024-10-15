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

def reserve_food_item(food_item, user_name, user_phone, pickup_time):
    food_items = []
    reservation_made = False
    try:
        with open('foodData.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['food_item'] == food_item and not reservation_made:
                    print(f"{food_item} reserved by {user_name}.")
                    reservation_made = True
                    # Normally, you'd save reservation details to a separate file or system
                else:
                    food_items.append(row)
    except FileNotFoundError:
        print("No food items available.")
        return

    with open('foodData.csv', 'w', newline='') as csvfile:
        fieldnames = ['food_item', 'location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(food_items)

    if not reservation_made:
        print(f"{food_item} is not available for reservation.")

def main():
    while True:
        print_food_items()
        food_item = input("Enter the food item you want to reserve: ")
        user_name = input("Enter your name: ")
        user_phone = input("Enter your phone number: ")
        pickup_time = input("Enter your pickup time: ")
        reserve_food_item(food_item, user_name, user_phone, pickup_time)
        
        continue_input = input("Do you want to continue? (Y/N) ")
        if continue_input.lower() != "y":
            break

if __name__ == "__main__":
    main()
