# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two': pd.Series([1, 2, 3, 4], index=['a', 'b','c', 'd'])}
# df = pd.DataFrame(d)
# print("adding a new column by passing a Series:")
# df['three']=pd.Series([10,20,30],index=['a','b','c'])
# print(df)
#
# print("adding a new column using the existing column in DataFrames:")
# df['four']=df['one']+df['three']
# print(df)

# import pandas as pd
# d = {'name': pd.Series(['tom','james','ricky','vin','steve','smith','jack']),
#      'age': pd.Series([25, 36, 57, 44, 77, 43, 33]),
#      'rating': pd.Series([4.34, 4.56, 4.78, 5.4, 6.4, 8.9, 5.4 ])}
#
# df = pd.DataFrame(d)
# print(df)
# print("the transpose of the data series is:")
# print(df.T)

# import pandas as pd
# d = {'name': pd.Series(['tom','james','ricky','vin','steve','smith','jack']),
#      'age': pd.Series([25, 36, 57, 44, 77, 43, 33]),
#      'rating': pd.Series([4.34, 4.56, 4.78, 5.4, 6.4, 8.9, 5.4 ])}
#
# df = pd.DataFrame(d)
# print("the data types  of each column is:")
# print(df.dtypes)

#sum

import pandas as pd
d = {'name': pd.Series(['tom','james','ricky','vin','steve','smith','jack']),
     'age': pd.Series([25, 36, 57, 44, 77, 43, 33]),
     'rating': pd.Series([4.34, 4.56, 4.78, 5.4, 6.4, 8.9, 5.4 ])}

df = pd.DataFrame(d)
print(df.sum())

#mean value

# import pandas as pd
# d = {'name': pd.Series(['tom','james','ricky','vin','steve','smith','jack']),
#      'age': pd.Series([25, 36, 57, 44, 77, 43, 33]),
#      'rating': pd.Series([4.34, 4.56, 4.78, 5.4, 6.4, 8.9, 5.4 ])}
#
# df = pd.DataFrame(d)
# print(df.mean())


# import pandas as pd
# d = {'name': pd.Series(['tom','james','ricky','vin','steve','smith','jack']),
#      'age': pd.Series([25, 36, 57, 44, 77, 43, 33]),
#      'rating': pd.Series([4.34, 4.56, 4.78, 5.4, 6.4, 8.9, 5.4 ])}
#
# df = pd.DataFrame(d)
# print(df.describe)

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c'])
print(df)
print("NaN replaced with '0':")
print(df.fillna(0))