import numpy as np

#a=np.array([123,2,323,234,523])


#a=np.array([[5,4,3],[39,50,40]])


#a=np.array([[1,2,3,4,5],[5,5,5,4,3],[6,7,5,3,4]])


#a=np.array([[1,2,3],[4,5,6]], dtype=np.float32)


#a=np.ones(9)


#a=np.ones([3,4])


#a=np.empty(8)


#a=np.arange(10)


#a=np.linspace(0,1,5)


#a=np.eye(2)


#print(a)


#print(a.size)


#print(a.dtype)


#a=np.array([1,2,3])
#b=5
#print(a+b)


#a=np.array([1,2,3])
#a=np.array([[1,2,3],[4,5,6]])
#print(a[0])
#print(a[0][1])


'''a=np.array([1,2,3,4,5])
indices = np.array([0, 2, 4])
print(a[indices])'''


'''a=np.array([[1,2,3],[4,5,6]])
r=np.array([1,0])
c=np.array([0,1])
print(a[r,c])


a=np.array([1,2,3,4,5])
print(a[a>4])'''




'''a = np.array([1, 2])
b = np.array([3, 4])
c=np.hstack(a,b)
print(c)
d=np.vstack(a,b)
print(d)
e=np.stack((a,b),axis=1)
print(e)
'''


#QUESTIONS
#1)
'''a=np.random.randint(10,size=(2,3,4))
b=np.random.randint(10,size=(3,4))
print(a*b)'''

#2)
'''def calc():
    try:
        ar=int(input("Enter rows for a "))
        ac=int(input("Enter columns for a "))
        a=np.random.randint(10,size=(ar,ac))


        br=int(input("Enter rows for a "))
        bc=int(input("Enter columns for a "))
        b=np.random.randint(10,size=(br,bc))


        o=input("what operation do you need to do")
        if o=="+":
            return(a+b)
        elif o=="-":
            return(a-b)
        elif o=="*":
            return(a*b)
        elif o=="/":
            return(a/b)
        else:
            return("wrong input")

    except ValueError:
        print("Error: Broadcasting is not possible. Arrays c and d must have compatible shapes.")




print(calc())
'''


#3)
'''import numpy as np
e=np.random.randint(10,size=(5,3))
f=np.random.randint(10,size=5)
op=e[:,:,np.newaxis]*f[np.newaxis,np.newaxis,:]
print(op)'''



#4)
'''g=np.random.randint(10,size=(4,3,2))
print(g[::2, ::2, :])'''


#5)
'''def calc():
    try:
        ar=int(input("Enter rows for a "))
        ac=int(input("Enter columns for a "))
        h=np.random.randint(10,size=(ar,ac))


        i=int(input("i "))
        j=int(input("j "))
        b=np.random.randint(10,size=(br,bc))'''



#6)
'''def calc():
    ar=int(input("Enter rows for a "))
    ac=int(input("Enter columns for a "))
    l=np.random.randint(10,size=(ar,ac))
    print(l)

    r_mean=np.mean(l,axis=1)
    c_mean=np.mean(l,axis=0)
    m=r_mean*c_mean

    return m'''



#7)
'''l=np.random.randint(10,size=(4,6))
print(l)
z=l.reshape(2,2,6)
print(z)
c=z.ravel()
print(c)'''



#8)
'''l=np.random.randint(10,size=(4,6))
o=int(input("Enter position "))
r=np.roll(l,o,axis=0)
print(r)
'''



