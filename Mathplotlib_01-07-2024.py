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


'''import numpy as np
x =[1,2,3,4,5]
x_indexes=np.arange(len(x))
width=0.25

y=[3,4,5,3,2]
plt.bar(x_indexes-width,y,color="green")

y1=[4,6,7,5,3]
plt.bar(x_indexes,y1,color="red")

plt.ylabel("x")
plt.xlabel("y")
plt.legend()
plt.show()'''




#SCATTERPLOT


'''girl=[78,50,39,59,60]
boy=[48,75,64,57,54]
range=[10,30,50,60,100]
plt.scatter(range,girl,marker="^",label="girl")
plt.scatter(range,boy,label="boy")
plt.grid(True,linestyle="--")
plt.legend()
plt.show()'''



'''import numpy as np
a=np.random.uniform(0,6,200)
plt.hist(a,5)
plt.show()'''


'''import numpy as np
a=np.random.normal(10,1,200)
plt.hist(a,200)
plt.show()'''



'''x = [1, 1, 2, 3, 3, 5, 7, 8, 9, 10,
     10, 11, 11, 13, 13, 15, 16, 17, 18, 18,
     18, 19, 20, 21, 21, 23, 24, 24, 25, 25,
     25, 25, 26, 26, 26, 27, 27, 27, 27, 27,
     29, 30, 30, 31, 33, 34, 34, 34, 35, 36,
     36, 37, 37, 38, 38, 39, 40, 41, 41, 42,
     43, 44, 45, 45, 46, 47, 48, 48, 49, 50,
     51, 52, 53, 54, 55, 55, 56, 57, 58, 60,
     61, 63, 64, 65, 66, 68, 70, 71, 72, 74,
     75, 77, 81, 83, 84, 87, 89, 90, 90, 91
     ]
plt.style.use("ggplot")
plt.hist(x, bins=10,edgecolor="white")
plt.show()'''





#AREA PLOT

'''import numpy as np
x=range(1,6)
y=[1,4,6,8,4]

plt.fill_between(x,y,color="blue",alpha=0.5)
plt.show()
'''


'''import numpy as np
x=range(1,6)
y=[1,4,6,8,4]

plt.fill_between(x,y,color="blue",alpha=0.5)
plt.plot(x,y,color="darkblue")
plt.show()'''




#BOXPLOT


import numpy as np
'''data=np.random.normal(loc=0,scale=1,size=100)
plt.boxplot(data)'''


'''data1 = np.random.normal(loc=0, scale=1, size=100)
data2 = np.random.normal(loc=2, scale=1.5, size=100)
plt.boxplot([data1, data2],notch=True,patch_artist=True,
            boxprops=dict(facecolor="red",linestyle="--"),
            medianprops=dict(color="green"))
plt.show()'''