import products, store


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = store.Store(product_list)

def start(store_obj):
    usr_inp = input("1. List all products in store \n2. Show total amount in store\n3. Make an order\n4. Quit\n: ")


start(best_buy)