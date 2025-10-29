import time
import asyncio

menu = {'osh': 4, 'lagman': 6, 'shashlik': 10, 'qozonkabob': 8}
salats = {'oliviye': 2, 'sezar': 3, 'achchiq-chuchuk': 4}
orders = []

def show_menu():
    print("Menu:")
    for item, time in menu.items():
        print(f"{item}: {time} minutes to cook")

def show_salads():
    print("Salads:")
    for item, time in salats.items():
        print(f"{item}: {time} minutes to prepare")

def place_order(orders):
    food = input("Would you like to eat food: Enter the food: ")
    if food not in menu:
        print("We don't have this food")
        return orders
    
    orders.append(food)
    
    salad_choice = input("Would you like to have salad? (yes/no): ")
    if salad_choice.lower() == 'yes':
        salad = input("Enter the salad: ")
        if salad not in salats:
            print("We don't have this salad")
        else:
            orders.append(salad)
    
    return orders

async def cook_single_item(item_name, delay):
    """Bitta taomni pishirish"""
    print(f"🔄 Cooking {item_name}...")
    await asyncio.sleep(delay)
    return f"✅ {item_name} is ready! (took {delay} minutes)"

async def cook_food_optimized(orders, delays):
    """Taomlarni optimallashtirilgan tartibda pishirish - qisqa vaqtlilar birinchi"""
    if not orders:
        print("No orders to cook")
        return
    
    print(f"\n🧑‍🍳 Starting to cook {len(orders)} items...")
    print("📊 Optimization: Cooking shorter items first for better efficiency")
    
    # Taomlarni vaqt bo'yicha saralash (qisqa vaqtlilar birinchi)
    sorted_orders = sorted(orders, key=lambda x: delays.get(x, 0))
    
    print(f"📋 Cooking order: {', '.join(sorted_orders)}")
    start_time = time.time()
    
    # Saralangan taomlarni parallel pishirish
    tasks = []
    for item in sorted_orders:
        if item in delays:
            task = asyncio.create_task(cook_single_item(item, delays[item]))
            tasks.append(task)
    
    # Natijalarni tayyor bo'lish tartibida chiqarish
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        current_time = time.time() - start_time
        print(f"{result} | Time: {current_time:.1f}m")
    
    total_time = time.time() - start_time
    print(f"\n🎉 All orders are ready! Total time: {total_time:.1f} minutes")
    
    # Optimallashtirish samaradorligi
    original_time = sum(delays[item] for item in orders)
    print(f"💡 Time saved through optimization: {original_time - total_time:.1f} minutes")

async def main():
    show_menu()
    show_salads()
    place_order(orders)
    
    if orders:
        delays = {**menu, **salats}
        await cook_food_optimized(orders, delays)
    else:
        print("No orders placed.")

asyncio.run(main())