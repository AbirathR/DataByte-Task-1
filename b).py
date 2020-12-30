import csv
reader = csv.reader(open('data_csv.csv'))
z={}
q=[]
h=[]
result = {}
for row in reader:
    key = row[0]
    result[key] = row[1]

for k in sorted(result.keys()) :
    z[k]=result[k]
for c in z:
    h.append(c)
a=input('Enter first country code in caps')
b=input('Enter second country code in caps')

for country in z:
    if(result[country]==a):
        q.append(country)
    if(result[country]==b):
        q.append(country)
q.sort()
e=h.index(q[0])
f=h.index(q[1])
for i in range(e+1,f):
    print(h[i])






    
    
    

