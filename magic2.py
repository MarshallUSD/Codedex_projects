"""""
class Magic:
    def __init__(self, a, b):
        self.a = a  
        self.b = b  

    def __add__(self, other):
        new_a = self.a * other.b + self.b * other.a
        new_b = self.b * other.b
        return Magic(new_a, new_b)

    def __sub__(self, other):
        new_a = self.a * other.b - self.b * other.a
        new_b = self.b * other.b
        return Magic(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Magic(new_a, new_b)

    def __truediv__(self, other):
        new_a = self.a * other.b
        new_b = self.b * other.a
        return Magic(new_a, new_b)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __repr__(self):
        return f"{self.a}/{self.b}"



x = Magic(1, 2)   # 1/2
y = Magic(3, 4)   # 3/4

print("x + y =", x + y)   
print("x - y =", x - y)   
print("x * y =", x * y)  
print("x / y =", x / y)  
print("x == y:", x == y)

"""""
"""""
#to do __len__,__getitem__,__contains__

class Mylist:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):

        return self.items[index]

    def __contains__(self, item):
        return item in self.items
    
list1=Mylist([1,2,3,4,5])
print(len(list1))
print(list1[1:])
print(3 in list1)    
            """
"""
class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count +=1
        print(f"Counter is called {self.count} times")
        return self.count
    
counter=Counter()

counter()
counter()
counter()
counter()
counter()

"""
from datetime import datetime

class Cart:
    def __init__(self):
        self.items = []  

    
    def __len__(self):
        return len(self.items)

    
    def __delitem__(self, index):
        if 0 <= index < len(self.items):
            item = self.items[index]
            del self.items[index]
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{current_time}] Deleted item at index {index}: {item}")
        else:
            raise IndexError("Index out of range")

    
    def add(self, item):
        self.items.append(item)

    def __str__(self):
        return f"Cart({self.items})"


cart = Cart()
cart.add("Apple")
cart.add("Banana")
cart.add("Milk")

print(len(cart))       

del cart[1]    

print(len(cart))        

del cart[0]             

print(cart)            

