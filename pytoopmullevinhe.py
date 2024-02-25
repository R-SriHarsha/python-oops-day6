class parent:
    def __init__(self,data1):
        self.data1=data1
        print("data :",data1)
class a(parent):
    def __init__(self,data1,data2):
        super().__init__(self.data1)
        self.data2=data2
        print("data :",data2) 

class b(a):
    def __init__(self,data1,data2,data3):
        super().__init__(self.data1,self.data2)
        self.data3=data3
        print("data :",data2) 


class c(b):
    def __init__(self,data1,data2,data3,data4):
        
        self.data1=data1
        self.data2=data2
        self.data3=data3
        super().__init__(data1,data2,data3,data4)
        self.data4=data4
        print("data :",data4) 

m,n,o,p=map(str,input().split())

obj=c(m,n,o,p)
        
