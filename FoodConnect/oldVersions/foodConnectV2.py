class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.food_items = {}

    def postFood(self, food_item):
        if food_item not in self.food_items:
            self.food_items[food_item] = [self.location]
            print(f"{food_item} posted by {self.name} at {self.location}.")
        else:
            self.food_items[food_item].append(self.location)
            print(f"{food_item} posted again by {self.name} at {self.location}.")

    def reserve(self, food_item, user_name, user_phone, pickup_time):
        if food_item not in self.food_items:
            print(f"{food_item} is not available.")
        else:
            if len(self.food_items[food_item]) == 0:
                print(f"{food_item} is not available.")
            else:
                location = self.food_items[food_item].pop(0)
                reservation = {
                    'user_name': user_name,
                    'user_phone': user_phone,
                    'pickup_time': pickup_time,
                    'location': location
                }
                self.food_items[food_item] = self.food_items.get(food_item, [])
                print(f"{food_item} reserved by {user_name}.")

    def print_food_items(self):
        print(f"{self.name} at {self.location}:")
        for food_item, locations in self.food_items.items():
            if len(locations) == 0:
                print(f"{food_item}: not available.")
            else:
                for location in locations:
                    print(f"{food_item}: available at {location}.")


def main():
    restaurant_name = input("Enter your restaurant name: ")
    restaurant_location = input("Enter your restaurant location: ")
    restaurant = Restaurant(restaurant_name, restaurant_location)

    while True:
        user_input = input("Are you a restaurant or a customer? (R/C) ")
        if user_input.lower() == "r":
            food_item = input("Enter the food item you want to post: ")
            restaurant.postFood(food_item)
        elif user_input.lower() == "c":
            food_item = input("Enter the food item you want to reserve: ")
            user_name = input("Enter your name: ")
            user_phone = input("Enter your phone number: ")
            pickup_time = input("Enter your pickup time: ")
            restaurant.reserve(food_item, user_name, user_phone, pickup_time)
        else:
            print("Invalid input. Please enter either R or C.")

        continue_input = input("Do you want to continue? (Y/N) ")
        if continue_input.lower() != "y":
            break

    restaurant.print_food_items()


if __name__ == "__main__":
    main()