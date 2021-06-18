# import pandas as pd
# s = pd.Series()
# print(s)


# import pandas as pd
# import numpy as np
# data = np.array(['a','b','c','d'])
# s = pd.Series(data,index=[100,101,102,103])
# print(s)

#converting dictonary data to series

# import pandas as pd
# import numpy as np
# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data)
# print(s)

#adding index to dictionary

# import pandas as pd
# import numpy as np
# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data,index=['b','c','d','a'])
# print(s)


# import pandas as pd
# s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# print(s)
# print(s[0])

#slising

# import pandas as pd
# s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# print(s)
# print(s[:3])

# import pandas as pd
# s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# print(s)
# print(s['a'])

#passing multiple index

import pandas as pd
s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s[['a','c','d']])

