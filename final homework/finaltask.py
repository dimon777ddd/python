import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

# convert categorical variable to one-hot encoding
one_hot = pd.get_dummies(data['whoAmI'])
data = data.drop('whoAmI', axis=1)
data = pd.concat([data, one_hot], axis=1)

data.head()
