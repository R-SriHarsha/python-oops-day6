class A:
    def __init__(self,data1,data2,data3):
        print("data1:",data1)
        self.data1=data1
        
class B(A):
    def __init__(self,data1,data2,data3):
        print("data2:",data2)
        
        self.data2=data2
        
class C(A):
    def __init__(self,data1,data2,data3):
        print("data3:",data3)
        
        self.data3=data3
a,b,c=map(str,input().split())
obj1=A(c,b,a)
obj2=B(c,b

       )
obj3=C(c,b,a)
