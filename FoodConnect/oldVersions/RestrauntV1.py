import csv

class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def postFood(self, food_item):
        found = False
        food_items = []
        try:
            with open('foodData.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['food_item'] == food_item and row['location'] == self.location:
                        found = True
                    food_items.append(row)
        except FileNotFoundError:
            pass  # File not found is okay on the first run

        if found:
            print(f"{food_item} is already posted by {self.name} at {self.location}.")
        else:
            food_items.append({'food_item': food_item, 'location': self.location})
            with open('foodData.csv', 'w', newline='') as csvfile:
                fieldnames = ['food_item', 'location']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(food_items)
            print(f"{food_item} posted by {self.name} at {self.location}.")

def main():
    restaurant_name = input("Enter your restaurant name: ")
    restaurant_location = input("Enter your restaurant location: ")
    restaurant = Restaurant(restaurant_name, restaurant_location)
    
    while True:
        food_item = input("Enter the food item you want to post: ")
        restaurant.postFood(food_item)
        
        continue_input = input("Do you want to continue? (Y/N) ")
        if continue_input.lower() != "y":
            break

if __name__ == "__main__":
    main()
