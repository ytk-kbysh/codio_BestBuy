import products, store


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = store.Store(product_list)

def start(store_obj):
    usr_inp = 1

    while usr_inp != 4:
        try:
            usr_inp = int(input(
                "   Store Menu \n"
                "   ---------- \n"
                "1. List all products in store \n"
                "2. Show total amount in store\n"
                    "3. Make an order\n"
                "4. Quit\n"
                "Please choose a number: "))
        except ValueError as e:
            print(e, "\nPlease input a number.")

        print("------\n")
    
        if usr_inp == 1:
            i = 1
            for item in best_buy.get_all_products():
                print(f"{i}. {item}")
                i +=1
        elif usr_inp == 2:
            print("Total of ", best_buy.get_total_quantity(), "items in store")
        elif usr_inp == 3:
            shopping_list = []
            i = 1
            for item in best_buy.get_all_products():
                print(f"{i}. {item}")
                i +=1
            usr_inp2 = 1
            usr_qty = 0
            while usr_inp2 != "":
                try:
                    usr_inp2 = input(
                    "When you want to finish order, enter empty text.\n"
                    "Which product # do you want?")
                    if usr_inp2 == "":
                        break
                except ValueError as e:
                    print(e, "\nPlease input a number.")
                try:
                    usr_qty = int(input("What amount do you want?"))
                    print("Product added to list!")
                except ValueError as e:
                    print(e, "\nPlease input a number.") 
                shopping_list.append(((product_list[int(usr_inp2)-1], usr_qty)))

            print("Order made! Total payment: $",best_buy.order(shopping_list))
        
        print("------\n")


start(best_buy)