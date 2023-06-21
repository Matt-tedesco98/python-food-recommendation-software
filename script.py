from linked_list import LinkedList
from welcome import *
from restaurantData import *

print_welcome()


# insert restaurant data into linked list
def insert_food_types():
    food_type_list = LinkedList()
    for food_type in types:
        food_type_list.insert_beginning(food_type)
    return food_type_list


# insert restaurant data into Linked List
def insert_restaurant_data():
    restaurant_data_list = LinkedList()
    for food_types in types:
        restaurant_sub_list = LinkedList()
        for restaurant in restaurant_data:
            if restaurant[0] == food_types:
                restaurant_sub_list.insert_beginning(restaurant)
        restaurant_data_list.insert_beginning(restaurant_sub_list)
    return restaurant_data_list


my_food_list = insert_food_types()
my_restaurant_list = insert_restaurant_data()

# user interaction
inputted_food_type = ""
while len(inputted_food_type) == 0:
    user_input = str(input(
        "\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if "
        "it's here.\n")).lower()

    # Search for users input in food types
    matched_food_type = []
    type_list_head = my_food_list.get_head_node()
    while type_list_head is not None:
        if str(type_list_head.get_value()).startswith(user_input):
            matched_food_type.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()
    for food in matched_food_type:
        print(food)

    # Check if only one type of restaurant was found
    if len(matched_food_type) == 1:
        select_type = str(input("\nThe only matching type for the specified input is " + matched_food_type[
            0] + ". \nDo you want to look at " +
                                matched_food_type[0] + " restaurants? Enter y for yes and n for no\n")).lower()
        # restaurant selector
        if select_type == "y":
            selected_food_type = matched_food_type[0]
            print("Selected Food Type: " + selected_food_type)
            restaurant_list_head = my_restaurant_list.get_head_node()
            while restaurant_list_head.get_next_node() is not None:
                sublist_head = restaurant_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_food_type:
                    while sublist_head.get_next_node() is not None:
                        print("--------------------------")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Price: " + sublist_head.get_value()[2] + "/5")
                        print("Rating: " + sublist_head.get_value()[3] + "/5")
                        print("Address: " + sublist_head.get_value()[4])
                        print("--------------------------\n")
                        sublist_head = sublist_head.get_next_node()
                restaurant_list_head = restaurant_list_head.get_next_node()
            # Ask user if they would like to search for other types of restaurants
            repeat_loop = str(input("\nDo you want to find other restaurants? Enter y for yes and n for no.\n")).lower()
            if repeat_loop == 'y':
                selected_food_type = ""
