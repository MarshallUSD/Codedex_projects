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

class SalesOrder:
    def __init__(self, order_id, customer_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.products = []

    def __len__(self):
        return len(self.products)

    def __contains__(self, product):
        return product in self.products
    
    # implementing += operator to add products to the order
    def __iadd__(self, product):
        self.products.append(product)
        return self

    def __bool__(self):
        return len(self.products)>0


order1= SalesOrder(order_id=777, customer_id=789)
print(bool(order1))  # False
product1= Product(sku="A101", name="Widget", cost_price=10.00, selling_price=15.00, stock_quantity=5)
order1 += product1
print(bool(order1))  # True


#TASK 3: BUSINESS ANALYSIS & REFLECTION (20 points)
#Write a brief business memo addressing:
#1. Business Justification (15 points)
 #  - Explain how these dunder methods provide business intelligence value
  # - Provide specific examples of business questions each method helps answer:
   #  - `__gt__`/`__lt__` (profitability comparison)
    # - `__add__` (inventory management)
     #- `__getitem__` (performance metrics)
#2. Technical Trade-off Analysis (5 points)
 #  - Identify one potential business downside of using SKU for `__eq__`
  # - Consider scenarios where product information changes but SKU remains same

#IMPLEMENTATION NOTES
#- Create both classes in a single Python file
#- Ensure methods handle edge cases (empty data, invalid operations)
#- Include error handling where specified
#- Write clean, documented code suitable for business environment

#SUBMISSION REQUIREMENTS
#1. Python File: `YourName_BusinessDunders.py`
#   - Complete implementation of both classes
 ## - Clean, professional-style code
#2. Business Memo
#   - Included as comments at top of Python file
 #  - Clear, concise business reasoning
  # - Professional writing style

# Business Memo
# To: Business Stakeholders
# From: [Your Name]
# Subject: Business Justification for Implementing Dunder Methods in Product and SalesOrder Classes
# Date: [Today's Date]
# 1. Business Justification
# The implementation of dunder methods in the Product and SalesOrder classes provides significant business intelligence value by enabling more intuitive and efficient operations on product data.
# - `__gt__`/`__lt__`: These methods allow for direct comparison
# of product profitability. For example, a business question such as "Which product yields higher profit margins?" can be answered directly by comparing two Product instances using these methods.
# - `__add__`: This method facilitates inventory management by allowing the aggregation of stock quantities for identical products. A common business question like "What is the total stock available for a specific SKU?" can be efficiently addressed by adding two Product instances with the same SKU.
# - `__getitem__`: This method provides a straightforward way to access specific product attributes using indexing. For instance, a business question such as "What is the selling price of a product?" can be answered by accessing the appropriate index of a Product instance.
# 2. Technical Trade-off Analysis
# While using SKU for the `__eq__` method provides a unique identifier for products,
# a potential downside is that product information may change over time (e.g., name, price) while the SKU remains the same. This could lead to scenarios where two products are considered equal based solely on SKU, despite having different attributes, potentially causing confusion in inventory and sales analysis.

