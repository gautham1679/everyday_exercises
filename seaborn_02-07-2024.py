import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

'''data = {'Time': [1, 2, 3, 4, 5], 'Value': [3, 5, 2, 4, 6]}
df = pd.DataFrame(data)
sns.lineplot(x='Time', y='Value', data=df)
plt.show()  '''



'''x=[1,2,3,4]
y=[4,5,3,1]
sns.lineplot(x=x,y=y)
plt.show()'''



'''d=sns.load_dataset("flights")
sns.lineplot(x="year",y="passengers",data=d)
plt.show()'''

'''d=sns.load_dataset("flights")
sns.lineplot(x="year",y="passengers",data=d,hue="month",style="month",markers=True,dashes=False)
plt.show()'''



#HISTOGRAM


'''p=sns.load_dataset("penguins")
p.head(20)
sns.histplot(data=p,x="flipper_length_mm",bins=30,color="red",kde=True,hue="species",multiple="stack")
plt.show()'''




'''p=sns.load_dataset("penguins")
p.head(20)
sns.histplot(data=p,x="flipper_length_mm",bins=30,color="red",kde=True,hue="species",element="step")
plt.show()'''




#t=sns.load_dataset("tips")
'''sns.histplot(data=t,x="size",stat="percent")
plt.show()
'''

'''sns.histplot(data=t, x="day", hue="sex", multiple="dodge", shrink=.8)
plt.show()'''



#BARPLOT


'''d=sns.load_dataset("penguins")
sns.barplot(x="island",y="body_mass_g",data=d,hue="sex")
plt.show()'''


'''data=sns.load_dataset("flights")
f=data.pivot(index="year",columns="month",values="passengers")
sns.barplot(f["Dec"])
plt.show()'''



#HEATMAP & SCATTERPLOT


'''sns.heatmap(data.corr(numeric_only=True),annot=True,linewidth=2,cmap="crest")
sns.scatterplot(data=data,x="total_bill",y="tip",hue="time",style="time",size="size")
plt.show()'''



'''data=sns.load_dataset("tips")
sns.kdeplot(x="total_bill",data=data)
plt.show()'''


'''data=sns.load_dataset("tips")
sns.kdeplot(x="total_bill",data=data,hue="sex",fill=True,palette="crest")
sns.rugplot(data=data,x="tip")
plt.show()
'''


#BOXPLOT



'''data=sns.load_dataset("tips")
sns.boxplot(x="day",y="total_bill",data=data,hue="time",order=["Fri","Sat"],showmeans=True)
plt.show()
'''


#VIOLINPLOT & PAIRPLOT

'''data=sns.load_dataset("tips")
sns.violinplot(x="time",y="total_bill",data=data,order=["Dinner","Lunch"])
plt.show()'''



data=sns.load_dataset("tips")
#sns.violinplot(x="day",y="total_bill",data=data,hue="time",order=["Fri"],split=True)
sns.pairplot(data,hue="sex",x_vars=["total_bill","tip"],y_vars=["total_bill","tip"])
plt.show()