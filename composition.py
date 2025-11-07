# creating multiple classes to perform payment

class PayByCash():
    def process_payment(self):
        return "Processing payment by Cash"

class PayByCard():
    def process_payment(self):
        return "Processing payment by Card"

class Order():

    def __init__(self, title):
        self.title = title



    def pay():
        pay = any_payment_method()
        return f'Item is paying by {pay}'
    
    def __init__(self, title, payment_method):
        self.title = title
        self.payment_method = payment_method()
    def pay(self):
        return f'Item: {self.title}, {self.payment_method.process_payment()}'
  

order1=Order('Book', PayByCard)
order2=Order('Pen', PayByCash)        
print(order1.pay())
print(order2.pay())