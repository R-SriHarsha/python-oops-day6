#write a python program
#a shopping mall having 5% discount for men and 7% for women and there is individual item discount for each
#item they purchased %for 3*no of items purchased
dm=0.05
dwm=0.07
n=int(input("no of items:"))
l=[]
de=0
for i in range(n):
    item=input("item:")
    cost=int(input("price:"))
    l.append(cost)
    d=cost*3*n/100
    de+=cost*3*n/100
    print("discount:",d)
    print("discount amount:",cost-d)
totalcost=sum(l)
print("total price:",totalcost)
totalcost-=de
print("discount amount:",totalcost)
td=0
g=input("gender:")
if g=="m":
    print("men:5% discount")
    td=totalcost*dm
elif g=="f":
    print("women:7% discount")
    td=totalcost*dwm
print("total discount:",td)
print("**********************")
print("total bill:Rs",totalcost-td,"/-")


    
    
