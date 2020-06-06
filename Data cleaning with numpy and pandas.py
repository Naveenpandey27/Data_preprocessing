import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\admin\Desktop\BL-Flickr-Images-Book.csv')
df.head()

to_drop = ['Edition Statement','Corporate Author','Corporate Contributors','Former owner','Engraver','Contributors','Issuance type','Shelfmarks']
df.drop(to_drop, inplace=True, axis=1)

df.head()

df['Identifier'].is_unique

df = df.set_index('Identifier')
df.head()

df.iloc[216]

df.get_dtype_counts()

df.loc[1905:, 'Date of Publication'].head(10)

regex = r'^(\d{4})'

extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
extr.head() 

df['Date of Publication'] = pd.to_numeric(extr)
df['Date of Publication'].dtype

df['Date of Publication'].isnull().sum() / len(df) 

df['Place of Publication'].head(10)

df.loc[4157862] 

df.loc[4159587] 

pub = df['Place of Publication']
london = pub.str.contains('London')
london[:7]

oxford = pub.str.contains('oxford')
oxford[:6]

df['Place of Publication'] = np.where(london, 'London', np.where(oxford, 'Oxford', pub.str.replace('-', ' ')))

df['Place of Publication'].head() 

df.head()

  




