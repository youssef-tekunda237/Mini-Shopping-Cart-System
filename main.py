from shoppingCart import shoppingCart
from product import simpleProduct  # <-- Use simpleProduct
from order import order 
from payment import stripeProcessor

def main():
    print("Welcome to the Mini Shopping Cart System!")
    cart = shoppingCart()
    # Default to no discount and Stripe

    while True:
        print("\nMenu:")
        print("1. Add product")
        print("2. Remove product")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Product name: ")
            price = float(input("Product price: "))
            prod = simpleProduct(name, price)  # <-- Use simpleProduct
            qty = int(input("Quantity: "))
            cart.add_item(prod, qty)
            

        elif choice == '2':
            name = input("Product name: ")
            qty = int(input("Quantity to remove: "))
            try:
                cart.remove_item(name, qty)  # Pass name, not dummy product
                print(f"Removed {qty} x {name}")
            except KeyError:
                print("Product not found in cart.")

        elif choice == '3':
            cart.view_cart()

        elif choice == '4':
            print("Checkout processing...")
            order_obj = order(cart, stripeProcessor())
            order_obj.checkout()
            print(order_obj)
            break

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == '__main__':
    main()
