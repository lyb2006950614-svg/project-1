import numpy as np

a = np.array([1, 2, 3])

print(a.shape)
import numpy as np

b = np.array([[1, 2, 3],

        [4, 5, 6]])

print(b.shape)

import numpy as np

c = np.array([[[1, 2],

               [3, 4]]])

print(c.shape)

import numpy as np

c = np.array([[[1, 2],[3,4]],

    [[5, 6],[7, 8]]])

print(c.shape)

import numpy as np
sales = np.array([

    [100, 120, 90],

    [110, 130, 95],

    [105, 125, 100]

])

print("每天銷售:", sales.sum(axis=1))

print("每商品銷售:", sales.sum(axis=0))

print("總銷售:", sales.sum())

import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[0])

import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[0:4:2])

import numpy as np

a = np.array([

[10, 20, 30],

[40, 50, 60],

[70, 80, 90]

])

print(a[1])

print(a[:,2])

print(a[0,:])

