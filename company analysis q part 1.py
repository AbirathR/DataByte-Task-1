import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel('company_sales_data.xlsx')
plt.plot(df['month_number'],df['total_profit'])
plt.xlabel('month number')
plt.ylabel('total profit')
plt.title('company sales analysis')
plt.xticks(  range(1,len(df)+1,1))
plt.show()
