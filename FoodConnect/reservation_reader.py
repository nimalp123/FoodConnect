import csv

def read_csv(file_name):
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"No data available from {file_name}.")
        return []

def list_reservations():
    reservations = read_csv('reservations.csv')
    print("\nReservations Made:")
    for reservation in reservations:
        print(f"{reservation['customer_name']} ({reservation['customer_phone']}) reserved {reservation['food_item_name']} from {reservation['restaurant_name']} at {reservation['restaurant_location']} for pickup at {reservation['pickup_time']}.")

def list_restaurants_and_food():
    food_data = read_csv('foodData.csv')
    print("\nParticipating Restaurants and Available Food Items:")
    restaurants = {}
    for item in food_data:
        restaurant = item['restaurant_name']
        if restaurant in restaurants:
            restaurants[restaurant].add(item['food_item'])
        else:
            restaurants[restaurant] = {item['food_item']}
    
    for restaurant, foods in restaurants.items():
        print(f"{restaurant} offers: {', '.join(foods)}")

def list_participants():
    reservations = read_csv('reservations.csv')
    print("\nParticipants (Name and Phone Number):")
    participants = {(res['customer_name'], res['customer_phone']) for res in reservations}
    for name, phone in participants:
        print(f"{name} ({phone})")

def list_reserved_food_details():
    reservations = read_csv('reservations.csv')
    print("\nReserved Food Items Details (Food Name, Restaurant Name, Restaurant Location, Pickup Time):")
    for res in reservations:
        print(f"{res['food_item_name']} from {res['restaurant_name']} at {res['restaurant_location']} for pickup at {res['pickup_time']}.")

def main():
    list_reservations()
    list_restaurants_and_food()
    list_participants()
    list_reserved_food_details()

if __name__ == "__main__":
    main()
