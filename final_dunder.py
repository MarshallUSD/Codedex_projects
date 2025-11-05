class Product:
    def __init__(self, sku, name, cost_price, selling_price, stock_quantity):
        self.sku = sku
        self.name = name
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.stock_quantity = stock_quantity


    def __repr__(self):
        return (f"Product(sku={self.sku!r}, name={self.name!r}, "
                f"cost_price={self.cost_price!r}, selling_price={self.selling_price!r}, "
                f"stock_quantity={self.stock_quantity!r})") 
    

    def __str__(self):
        return (f"Product {self.name} (SKU: {self.sku}) - "
                f"Selling Price: ${self.selling_price:.2f}, "
                f"Stock Quantity: {self.stock_quantity}")
    
    def __eq__(self,other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.sku == other.sku and
                self.name == other.name and
                self.cost_price == other.cost_price and
                self.selling_price == other.selling_price and
                self.stock_quantity == other.stock_quantity)


    def __gt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.selling_price - self.cost_price) > (other.selling_price - other.cost_price)
    
    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.selling_price - self.cost_price) < (other.selling_price - other.cost_price)
    
    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        if self.sku != other.sku:
            print("Warning : Adding stock of different products.")
            return NotImplemented
        return Product(
            sku=self.sku,
            name=self.name,
            cost_price=self.cost_price,
            selling_price=self.selling_price,
            stock_quantity=self.stock_quantity + other.stock_quantity
        )
    
    def __getitem__(self, index):
        attri=['sku', 'name', 'cost_price', 'selling_price', 'stock_quantity']
        if index <0 or index >= len(attri):
            print("Index out of range")
            return NotImplemented
        return getattr(self, attri[index])
     


mause=Product("SKU123", "Wireless Mouse", 15.00, 25.00, 100)
keyboard=Product("SKU124", "Mechanical Keyboard", 45.00, 70.00, 50)
print(repr(mause))
print(str(mause))
print(mause == keyboard)
print(mause > keyboard) 
another_mouse=Product("SKU123", "Wireless Mouse", 15.00, 25.00, 50)
combined_mouse=mause + another_mouse
print(str(combined_mouse))
print(combined_mouse[1])  # Accessing the 'name' attribute using indexing    