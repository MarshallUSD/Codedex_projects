import time
import asyncio

meals = {'burger': 6, 'pizza': 8, 'osh': 5, 'lagman': 7, 'shashlik': 10, 'qozonkabob': 9, 'fish': 4}
salads = {'oliviye': 2, 'sezar': 3, 'achchiq-chuchuk': 4, 'grechka-salad': 5, 'salad-nicoise': 6}
deserts = {'ice-cream': 3, 'cake': 5, 'fruit-salad': 4, 'pudding': 6, 'brownie': 7}
orders = []

# using asyncio to cook meals

def show_menu():
    print("Menu: ")
    for i in meals.items():
        print(f"{i[0]}: minutes to cook {i[1]}")

def show_salads():
    print("Salads: ")
    for i in salads.items():
        print(f"{i[0]}: minutes to prepare {i[1]}")

def show_deserts():
    print("Deserts: ")
    for i in deserts.items():
        print(f"{i[0]}: minutes to prepare {i[1]}")

async def main():
    is_running = True  
    
    while is_running:
        show_menu()  
        choice = input("Would you like to eat food: Enter the food: ")
        
        if choice not in meals:
            print("We don't have this food")
        else:
            orders.append(choice)
        
        salad_choice = None
        if input("Would you like to have salad (yes/no): ") == 'yes':
            show_salads()  
            salad_choice = input("Enter the salad: ")
            if salad_choice not in salads:
                print("We don't have this salad")
            else:
                orders.append(salad_choice)
        
        desert_choice = None  
        if input("Would you like to have desert (yes/no): ") == 'yes':
            show_deserts()  
            desert_choice = input("Enter the desert: ")
            if desert_choice not in deserts:
                print("We don't have this desert")
            else:
                orders.append(desert_choice)
        
    
        if input("Would you like to add another order? (yes/no): ") != 'yes':
            is_running = False

async def cook_food(orders, delays):
    if not orders:
        print("No orders to cook")
    else:
        total_time = 0
        start_time=time.time()
        for i in orders:
            print(f"Cooking... {i}", end="\r")
            await asyncio.sleep(delays[i])
            total_time += delays[i]
            print(f"{i} is ready! ")
        print(f"All orders are ready! Total time: {total_time} minutes")
        print(f"Total elapsed time: {time.time()-start_time:.2f} minutes")
async def main_async():

    print("Welcome to our restaurant!")
    show_menu()
    show_salads()
    show_deserts()
    
    await main()  
    
    delays = {**meals, **salads, **deserts}
    await cook_food(orders, delays)

asyncio.run(main_async())