class sm:
    def __init__(self,data):
        self.data=data
    def stlengt(self,data):
        print("length:",len(data))
class a:
    def __init__(self,data):
        self.data=data
    def strloer(self,data):
        print(self.data.lower())
class b:
    def __init__(self,data):
        self.data=data
    def strupur(self,data):
        print(self.data.upper())
class p(sm,a,b):
    def __init__(self,data):
        self.data=data
        self.stlengt(data)
        self.strloer(data)
        self.strupur(data)
        print("done")
        
obj=p(input())
