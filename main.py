import asyncio  # asyncio is library imported to use asyn await
import keyword
import calendar
import modules.functions as f
import pandas as pf

cal = calendar.month(2016, 1)
print("calendar:-", cal)

leapOrNot = calendar.isleap(2016)
print("leapOrNot:-", leapOrNot)

calendarKeyWordds = dir(calendar)
print("calendarKeyWordds:-", dir(calendar))

print("keyword.kwlist:-", keyword.kwlist)

msg = "Hai, Welcome to python world"
print("message spliting:-", msg.split())


def a_void_function():
    a = 5
    b = 3
    c = a + b
    print("calling void funtion:-", c)


x = a_void_function
print("None keyword eg:-", x)
# Call the function
a_void_function()


async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("world")


asyncio.run(main())

for i in range(1, 11):
    if i == 5:
        break
    print("break keyword eg:-", i)

for i in range(1, 11):
    if i % 2 == 0:
        continue
        i = i + 1
    print("continue keyword eg:-", i)

areaOfSquare = f.calculation_area_of_square(5)
print("area of square = ", areaOfSquare)

areaOfTriangle = f.calculation_area_of_triangle(5, 6)
print("area of triangle = ", areaOfTriangle)

book = {}
book["tom"] = {"name": "Tom", "address": "1 red st,NY", "phone": "987654321"}
book["bob"] = {"name": "Bob", "address": "1 green st,NY", "phone": "23456789"}

import json

s = json.dumps(book)
book = json.loads(s)
print("JSON format:-", book)

for person in book:
    print("booke person", book[person])


import numpy as np  # numpy is python library imported to use array, do liner algebra,fourier transform and matrices

# numpy is open source project and defined as Numerical Python(numpy)
# array of objet is called 'ndarray'
# arrays are stored in one continuous place in memory unlike List
# this is why numpy is 50X faster than list

arr = np.array([1, 2, 3, 4])


two_dimension_arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
three_dimension_arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],[[1, 2, 3, 4], [5, 6, 7, 8]]])
print('three_dimension_arr',three_dimension_arr.reshape(2,8))
reshape_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("numpy arr", type(arr))
print("find dimension", arr.ndim)
print("find shape", arr.shape)
print("reshape", reshape_arr.reshape(5, 2))
# from matplotlib import pyplot as plt
# import numpy as np

# # Generate 100 random data points along 3 dimensions
# x, y, scale = np.random.randn(3, 100)
# fig, ax = plt.subplots()

# # Map each onto a scatterplot we'll create with Matplotlib
# ax.scatter(x=x, y=y, c=scale, s=np.abs(scale) * 500)
# ax.set(title="Some random data, created with JupyterLab!")
# plt.show()


dataSet = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 6, 8]}
myvar = pf.DataFrame(dataSet)
print("dataFrame", myvar)


file_path_excel = "/home/tlspc-054/Downloads/samplepython.xlsx"
file_path_csv = "/home/tlspc-054/Downloads/samplepython - Sheet1.csv"
df_excel = pf.read_excel(file_path_excel)
df_csv = pf.read_csv(file_path_csv)
df1 = pf.DataFrame(df_excel)
df2 = pf.DataFrame(df_csv)
print("df1", df1)
print("df2", df2)
