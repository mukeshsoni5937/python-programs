class myClass:
    def __init__(self):
        self.my_att = "Hello"  
obj = myClass()
print(obj.__dict__)
print(obj.__class__)
print(obj.__str__())

{'my_att': 'Hello'}
<class '__main__.myClass'>
<__main__.myClass object at 0x000001E8F2D19B50>