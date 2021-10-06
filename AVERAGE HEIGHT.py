import pandas as pd

df = pd.read_csv('Hap Seng_M3_F27.txt', delimiter='\t')
#print(df)
df.columns=['1','2','3','4','5','6','7','8','X','Y','Z','12']
#print(df['Z'])
height = df['Z']
#print(len(height))
total=sum(df['Z'])
#print(total)

height = [i for i in height if i !=0]
#print(height)
amount=len(height)
#print(amount)

average= total/amount
print(average)

