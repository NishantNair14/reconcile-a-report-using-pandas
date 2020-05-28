# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df=pd.read_csv(path)
df['state']=df['state'].apply(lambda x:x.lower())
#print(df)
df['Total']=df['Jan']+df['Feb']+df['Mar']
sum_row=df[['Jan','Feb','Mar','Total']].sum()
print(sum_row)
df_final=df.append(sum_row,ignore_index=True)
print(df_final)
# Code ends here


# --------------
import requests

# Code starts here
url='https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response=requests.get(url)
df1=pd.read_html(response.content)[0]

df1=df1[11:]
#df1.columns=['']
df1.columns = df1.iloc[0]
df1 = df1[1:]

#print(df1)
df1['United States of America'].apply(lambda x: x.replace(" ", "")).astype(object)
df1['United States of America']=df1
list(df1.columns.values)
print(df1)
# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
#print(df1['US'])
mapping=df1.set_index('United States of America')['US'].to_dict()
#print(mapping)
df_final.insert(6,'abbr',np.nan)
df_final['abbr']=df_final['state'].map(mapping)

print(df_final)
# Code ends here


# --------------
# Code stars here
#print(df_final)
df_final['abbr'][df_final['state']=='mississipi'].replace(np.nan,'MS')
df_final[df_final['state']=='tenessee'].replace(np.nan,'TN')

df_final.loc[df_final.state=='mississipi','abbr']='MS'
df_final.loc[df_final.state=='tenessee','abbr']='TN'
print(df_final)
# Code ends here


# --------------
# Code starts here

df_final.loc[df_final.state=='northcarolina','abbr']='NC'
df_final.loc[df_final.state=='rhodeisland','abbr']='RI'
df_final.loc[df_final.state=='northdakota','abbr']='ND'
print(df_final)
df_sub=df_final.groupby('abbr')['abbr','Jan','Feb','Mar','Total'].sum()    
print(df_sub)
formatted_df=df_sub.applymap(lambda x:'$'+str(x))
print(formatted_df)
# Code ends here


# --------------
# Code starts here
sum_row=df[['Jan','Feb','Mar','Total']].sum()
df_sub_sum=pd.DataFrame(data=sum_row).T
print(df_sub_sum)
df_sub_sum=df_sub_sum.applymap(lambda x:'$'+str(x))
print(df_sub_sum)

final_table=formatted_df.append(df_sub_sum)
print(final_table)

final_table.rename(index={0:'Total'})
# Code ends here


# --------------
# Code starts here
df_sub['total']=df_sub['Jan']+df_sub['Feb']+df_sub['Mar']
print(df_sub['total'])
df_sub['total'].plot.pie()

# Code ends here


