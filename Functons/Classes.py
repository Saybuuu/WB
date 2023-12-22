class Cards:
    sales = 0

    def __init__(self, article, price=0, brand_name=None, product_name=None) -> object:
        self.article = article
        self.price = price
        self.brand_name = brand_name
        self.product_name = product_name

    def sold(self, quantity: int):
        self.sales += quantity
