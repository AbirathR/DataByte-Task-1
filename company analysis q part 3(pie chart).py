import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('company_sales_data.xlsx')
sum_of_cols=df.sum(axis=0)
no_of_units=[]
for i in range(1,7):
    no_of_units.append(sum_of_cols[i])
products=['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']
plt.axis('equal')
plt.pie(no_of_units,labels=products,autopct='%1.1f%%')
plt.show()

