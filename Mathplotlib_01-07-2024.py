import matplotlib.pyplot as plt


#PIECHART


'''d=["cat","dog","elephant","giraffe"]
c=[23,1,4,5]
plt.pie(c,labels=d,autopct="%.12f%%")
plt.show()'''



'''a=["gautham","joe","jeeva","jis"]
d=[95,3,5,1]
e=[0,0,0.4,0]
plt.pie(d,labels=a,autopct="%.1f%%",shadow=True,startangle=90,explode=e )
plt.show()'''


'''plt.title('Pie')
a=["gautham","joe","jeeva","jis"]
d=[95,3,5,1]
e=[0,0,0.4,0]
plt.pie(d,labels=a,autopct="%.1f%%",shadow=True,startangle=90,explode=e )
plt.tight_layout
plt.show()'''


# LINECHART


'''x=[1,2,3,4]
y=[8,5,7,3]
plt.plot(x,y,color="red")
plt.title("LINE CHART")
plt.xlabel("x")
plt.ylabel("y")
plt.show()'''




'''import numpy as np
x=np.array([1,2,3,4,5])
y=x**2
plt.plot(x,y,color="blue")
plt.show()'''



'''x=[1,2,3,4,5]
y=[4,6,7,5,3]
#plt.plot(x,y,linestyle=":",marker="*")

#x1=[1,2,3,4]
#y1=[8,5,7,3]
#plt.plot(x1,y1,linestyle="-",marker="p")

#plt.show()'''





'''age=[20,21,22,23,24]
salary=[100,150,200,250,350]
plt.plot(age,salary,label="all devs",marker="x")


age1=[20,21,22,23,24]
salary1=[110,140,500,650,850]
plt.plot(age1,salary1,label="all python",marker="o")



plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()'''




#BARCHART


'''x=[1,2,3,4,5]
y=[3,4,5,3,2]
plt.bar(x,y,color="green",label="Foreign")

y1=[4,6,7,5,3]
plt.plot(x,y1,linestyle="-",marker="*")

plt.ylabel("x")
plt.xlabel("y")
plt.legend()
plt.show()'''

x=[1,2,3,4,5]
y=[3,4,5,3,2]
plt.bar(x,y,color="green")

y1=[4,6,7,5,3]
plt.bar(x,y1,color="red")

plt.ylabel("x")
plt.xlabel("y")
plt.legend()
plt.show()