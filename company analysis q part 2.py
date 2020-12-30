import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('company_sales_data.xlsx')
plt.plot(df['month_number'],df['facecream'],label='Facecream')
plt.plot(df['month_number'],df['facewash'],label='Facewash')
plt.plot(df['month_number'],df['toothpaste'],label='Toothpaste')
plt.plot(df['month_number'],df['bathingsoap'],label='Bathingsoap')
plt.plot(df['month_number'],df['shampoo'],label='Shampoo')
plt.plot(df['month_number'],df['moisturizer'],label='Moisturizer')
plt.xlabel('month number')
plt.ylabel('Product sales')
plt.title('company sales analysis')
plt.xticks(  range(1,len(df)+1,1))
plt.legend()
plt.show()

