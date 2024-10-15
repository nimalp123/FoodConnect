import csv

class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def postFood(self, food_item):
        with open('foodData.csv', mode='a', newline='') as csvfile:
            fieldnames = ['restaurant_name', 'location', 'food_item']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:  # Check if file is empty to write header
                writer.writeheader()

            writer.writerow({'restaurant_name': self.name, 'location': self.location, 'food_item': food_item})
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
