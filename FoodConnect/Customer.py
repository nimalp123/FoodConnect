import csv

def print_food_items():
    try:
        with open('foodData.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            print("Available Food Items:")
            for row in reader:
                print(f"{row['food_item']} from {row['restaurant_name']} at {row['location']}.")
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
                    make_reservation(row['restaurant_name'], row['location'], food_item, user_name, user_phone, pickup_time)
                    reservation_made = True
                else:
                    food_items.append(row)
    except FileNotFoundError:
        print("No food items available.")
        return

    with open('foodData.csv', 'w', newline='') as csvfile:
        fieldnames = ['restaurant_name', 'location', 'food_item']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(food_items)

    if not reservation_made:
        print(f"{food_item} is not available for reservation.")

def make_reservation(restaurant_name, location, food_item, user_name, user_phone, pickup_time):
    with open('reservations.csv', mode='a', newline='') as csvfile:
        fieldnames = ['restaurant_name', 'restaurant_location', 'food_item_name', 'customer_name', 'customer_phone', 'pickup_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:  # Check if file is empty to write header
            writer.writeheader()

        writer.writerow({
            'restaurant_name': restaurant_name,
            'restaurant_location': location,
            'food_item_name': food_item,
            'customer_name': user_name,
            'customer_phone': user_phone,
            'pickup_time': pickup_time
        })
        print(f"{food_item} reserved by {user_name} for pickup at {pickup_time}.")

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
