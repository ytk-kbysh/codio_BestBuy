import products

class Store:

    def __init__(self, product_list) -> None:
        self.product_list = product_list


    def add_product(self, product):
        self.product_list.append(product)


    def remove_product(self, product):
        self.product_list.remove(product)


    def get_total_quantity(self) -> int:
        total = 0
        for product in self.product_list:
            total += product.get_quantity()
        return total
    

    def get_all_products(self) ->list: #spec "->list[Product]" gives error, so I removed "[Product]"
        all_products = []
        for product in self.product_list:
            if product.is_active() == 1:
                all_products.append(product.show())
        return all_products


    def order(self, shopping_list) -> float:
        order = 0
        for item in shopping_list:
            order += item[0].buy(item[1])
        return order
