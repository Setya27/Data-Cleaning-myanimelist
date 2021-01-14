#!/usr/bin/env python
# coding: utf-8

get_ipython().run_line_magic('config', 'Completer.use_jedi = False')

### Import Libraries and Load Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('AnimeList.csv', index_col=0)
df.head()


### Data Cleaning
# Remove "Genre: "
df['Genres'] = df['Genre'].apply(lambda x: x.split(': ')[1])

# Join all values in Series Data
genre_join  = ','.join(df['Genres'])

# Split values by ',' in String Data
genre_split = genre_join.split(',')

# Remove space in leading and trailing whitespaces
result = []
for x in genre_split:
    result.append(x.strip())

# Put in Series dataset
data = pd.Series(result)


### Data Visualization
mydata = []
for y in data.value_counts():
    mydata.append(y)   

labels = []
for z in data.value_counts().index.tolist():
    labels.append(z)

newdf = pd.DataFrame({'Genre': labels, 'Total': mydata})

plt.figure(figsize=(15,10))
sns.barplot(data=newdf, x='Total', y='Genre')

