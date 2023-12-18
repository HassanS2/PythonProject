restaurants = {
    'deepFries': {'tables': [1, 2, 3], 'waiting': []},
    'ULB': {'tables': [1, 2, 3], 'waiting': []},
    'Wagyu': {'tables': [1, 2, 3], 'waiting': []},
    'Bunger Bouetek': {'tables': [1, 2, 3], 'waiting': []}
}

def reserve_table(restaurant):
    if restaurant in restaurants:
        if len(restaurants[restaurant]['tables']) > 0:
            table = restaurants[restaurant]['tables'].pop(0)
            print(f"You have reserved a table at {restaurant}. Table number: {table}")
            return table
        else:
            print(f"Sorry, there are no available tables at {restaurant} at the moment.")
    else:
        print("Invalid restaurant name.")

def release_table(restaurant, table):
    if restaurant in restaurants:
        if table in restaurants[restaurant]['tables']:
            print(f"Table {table} at {restaurant} is already available.")
        elif table in restaurants[restaurant]['waiting']:
            restaurants[restaurant]['waiting'].remove(table)
            print(f"Table {table} at {restaurant} has been released and is now available.")
        else:
            print(f"Table {table} does not belong to {restaurant}.")
    else:
        print("Invalid restaurant name.")

def check_waiting(restaurant):
    if restaurant in restaurants:
        if len(restaurants[restaurant]['waiting']) > 0:
            print(f"There are {len(restaurants[restaurant]['waiting'])} people waiting for a table at {restaurant}.")
            print("Waiting list:", restaurants[restaurant]['waiting'])
        else:
            print(f"No one is currently waiting for a table at {restaurant}.")
    else:
        print("Invalid restaurant name.")

def reservation1():
        restaurant_choice = input("Choose a restaurant (deepFries, ULB, Wagyu, Bunger Bouetek): ")


        if restaurant_choice in restaurants:
              reservation = reserve_table(restaurant_choice)
              check_waiting(restaurant_choice)
        else:
            print("Invalid restaurant name.")


reservation1()
reservation1()
reservation1()
reservation1()