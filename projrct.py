menu = {
    'Pizza':50,
    'Pasta':70,
    'Burger':49,
    'Salad':80,
    'Coffee':60,
}
print("Welcome to Python Restaurant")
print("Pizza: Rs50\nPasta: Rs70\nBurger: Rs49\nSalad: Rs80\nCofffee:Rs60")
order_total=0
item_1=input('Enter the name of item you want to order = ')
if item_1 in menu:
    order_total+=menu[item_1]
    print(f'You item {item_1} has been added to your order')
else:
    print(f"oredered item{item_1} is not available yet!")
another_order=input('Do you want to add another item? (yes/No)')
if another_order== "yes":
    item_2 = input('Enter thr name of second item =')
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f'Item{item_2} has been added to order')
    else:
        print(f"Ordered item {item_2} is not available!")
print(f"The total amount of item is to pay {order_total} ")
