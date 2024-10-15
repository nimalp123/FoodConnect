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


# Example usage
restaurant1 = Restaurant("Restaurant A", "123 Main St")
restaurant1.postFood("Entree")
restaurant1.postFood("Vegetarian Entree")
restaurant1.postFood("Vegetarian -")
restaurant1.postFood("Appetizer")
restaurant1.postFood("Vegetarian Appetizer")
restaurant1.postFood("Soup")
restaurant1.postFood("Vegetarian Soup")
restaurant1.postFood("Salad")
restaurant1.postFood("Vegetarian Salad")
restaurant1.postFood("Kid's Meal")
restaurant1.postFood("Vegetarian Kid's Meal")

restaurant1.reserve("Entree", "John Doe", "123-456-7890", "12:30 PM")
restaurant1.reserve("Vegetarian Entree", "Jane Smith", "987-654-3210", "1:30 PM")

# restaurant1.print_food_items()