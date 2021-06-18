# import pandas as pd
# df = pd.DataFrame()
# print(df)

# import pandas as pd
# data = [1,2,3,4,5]
# df = pd.DataFrame(data)
# print(df)

#nexted list

# import pandas as pd
# data = [['alex',10],['bob, 12'],['clark',13]]
# df = pd.DataFrame(data,columns=['name','age'])
# print(df)

# import pandas as pd
# data = [['alex',10],['bob, 12'],['clark',13]]
# df = pd.DataFrame(data,columns=['name','age'],dtype=float)
# print(df)

import pandas as pd
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3], index=['a', 'b','c', 'd'])}
df = pd.DataFrame(d)
print(df)
print(df ['two'])