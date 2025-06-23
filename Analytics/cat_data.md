
When your data has categories represented by strings, it will be difficult to use them to train machine learning models which often only accepts numeric data.

Instead of ignoring the categorical data and excluding the information from our model, you can tranform the data so it can be used in your models.

Take a look at the table below, it is the same data set that we used in the multiple regression chapter.

Example:
```python
import pandas as pd

cars = pd.read_csv('data.csv')
print(cars.to_string())
```
Result
```python
             Car       Model  Volume  Weight  CO2
  0       Toyoty        Aygo    1000     790   99
  1   Mitsubishi  Space Star    1200    1160   95
  2        Skoda      Citigo    1000     929   95
  3         Fiat         500     900     865   90
  4         Mini      Cooper    1500    1140  105
  5           VW         Up!    1000     929  105
  6        Skoda       Fabia    1400    1109   90
  7     Mercedes     A-Class    1500    1365   92
  8         Ford      Fiesta    1500    1112   98
  9         Audi          A1    1600    1150   99
  10     Hyundai         I20    1100     980   99
  11      Suzuki       Swift    1300     990  101
  12        Ford      Fiesta    1000    1112   99
  13       Honda       Civic    1600    1252   94
  14      Hundai         I30    1600    1326   97
  15        Opel       Astra    1600    1330   97
  16         BMW           1    1600    1365   99
  17       Mazda           3    2200    1280  104
  18       Skoda       Rapid    1600    1119  104
  19        Ford       Focus    2000    1328  105
  20        Ford      Mondeo    1600    1584   94
  21        Opel    Insignia    2000    1428   99
  22    Mercedes     C-Class    2100    1365   99
  23       Skoda     Octavia    1600    1415   99
  24       Volvo         S60    2000    1415   99
  25    Mercedes         CLA    1500    1465  102
  26        Audi          A4    2000    1490  104
  27        Audi          A6    2000    1725  114
  28       Volvo         V70    1600    1523  109
  29         BMW           5    2000    1705  114
  30    Mercedes     E-Class    2100    1605  115
  31       Volvo        XC70    2000    1746  117
  32        Ford       B-Max    1600    1235  104
  33         BMW         216    1600    1390  108
  34        Opel      Zafira    1600    1405  109
  35    Mercedes         SLK    2500    1395  120
```

In the multiple regression chapter, we tried to predict the CO2 emitted based on the volume of the engine and the weight of the car but we excluded information about the car brand and model.

The information about the car brand or the car model might help us make a better prediction of the CO2 emitted.


## One Hot Encoding
We cannot make use of the Car or Model column in our data since they are not numeric. A linear relationship between a categorical variable, Car or Model, and a numeric variable, CO2, cannot be determined.

To fix this issue, we must have a numeric representation of the categorical variable. One way to do this is to have a column representing each group in the category.

For each column, the values will be 1 or 0 where 1 represents the inclusion of the group and 0 represents the exclusion. This transformation is called one hot encoding.

You do not have to do this manually, the Python Pandas module has a function that called get_dummies() which does one hot encoding.

Example:
One Hot Encode the Car column:
```python
import pandas as pd

cars = pd.read_csv('data.csv')
ohe_cars = pd.get_dummies(cars[['Car']])

print(ohe_cars.to_string())
```
Result
```python
      Car_Audi  Car_BMW  Car_Fiat  Car_Ford  Car_Honda  Car_Hundai  Car_Hyundai  Car_Mazda  Car_Mercedes  Car_Mini  Car_Mitsubishi  Car_Opel  Car_Skoda  Car_Suzuki  Car_Toyoty  Car_VW  Car_Volvo
  0          0        0         0         0          0           0            0          0             0         0               0         0          0           0           1       0          0
  1          0        0         0         0          0           0            0          0             0         0               1         0          0           0           0       0          0
  2          0        0         0         0          0           0            0          0             0         0               0         0          1           0           0       0          0
  3          0        0         1         0          0           0            0          0             0         0               0         0          0           0           0       0          0
  4          0        0         0         0          0           0            0          0             0         1               0         0          0           0           0       0          0
  5          0        0         0         0          0           0            0          0             0         0               0         0          0           0           0       1          0
  6          0        0         0         0          0           0            0          0             0         0               0         0          1           0           0       0          0
  7          0        0         0         0          0           0            0          0             1         0               0         0          0           0           0       0          0
  8          0        0         0         1          0           0            0          0             0         0               0         0          0           0           0       0          0
  9          1        0         0         0          0           0            0          0             0         0               0         0          0           0           0       0          0
  10         0        0         0         0          0           0            1          0             0         0               0         0          0           0           0       0          0
  11         0        0         0         0          0           0            0          0             0         0               0         0          0           1           0       0          0
  12         0        0         0         1          0           0            0          0             0         0               0         0          0           0           0       0          0
  13         0        0         0         0          1           0            0          0             0         0               0         0          0           0           0       0          0
  14         0        0         0         0          0           1            0          0             0         0               0         0          0           0           0       0          0
  15         0        0         0         0          0           0            0          0             0         0               0         1          0           0           0       0          0
  16         0        1         0         0          0           0            0          0             0         0               0         0          0           0           0       0          0
  17         0        0         0         0          0           0            0          1             0         0               0         0          0           0           0       0          0
  18         0        0         0         0          0           0            0          0             0         0               0         0          1           0           0       0          0
  19         0        0         0         1          0           0            0          0             0         0               0         0          0           0           0       0          0
  20         0        0         0         1          0           0            0          0             0         0               0         0          0           0           0       0          0
  21         0        0         0         0          0           0            0          0             0         0               0         1          0           0           0       0          0
  22         0        0         0         0          0           0            0          0             1         0               0         0          0           0           0       0          0
  23         0        0         0         0          0           0            0          0             0         0               0         0          1           0           0       0          0
  24         0        0         0         0          0           0            0          0             0         0               0         0          0           0           0       0          1
  25         0        0         0         0          0           0            0          0             1         0               0         0          0           0           0       0          0
  26         1        0         0         0          0           0            0          0             0         0               0         0          0           0           0       0          0
  27         1        0         0         0          0           0            0          0             0         0               0         0          0           0           0       0          0
  28         0        0         0         0          0           0            0          0             0         0               0         0          0           0           0       0          1
  29         0        1         0         0          0           0            0          0             0         0               0         0          0           0           0       0          0
  30         0        0         0         0          0           0            0          0             1         0               0         0          0           0           0       0          0
  31         0        0         0         0          0           0            0          0             0         0               0         0          0           0           0       0          1
  32         0        0         0         1          0           0            0          0             0         0               0         0          0           0           0       0          0
  33         0        1         0         0          0           0            0          0             0         0               0         0          0           0           0       0          0
  34         0        0         0         0          0           0            0          0             0         0               0         1          0           0           0       0          0
  35         0        0         0         0          0           0            0          0             1         0               0         0          0           0           0       0          0
```

Results

A column was created for every car brand in the Car column.


## Predict CO2
We can use this additional information alongside the volume and weight to predict CO2

To combine the information, we can use the concat() function from pandas.

First we will need to import a couple modules.

We will start with importing the Pandas.
```python
import pandas
```
The pandas module allows us to read csv files and manipulate DataFrame objects:
```python
cars = pandas.read_csv("data.csv")
```
It also allows us to create the dummy variables:
```python
ohe_cars = pandas.get_dummies(cars[['Car']])
```
Then we must select the independent variables (X) and add the dummy variables columnwise.

Also store the dependent variable in y.
```python
X = pandas.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']
```
We also need to import a method from sklearn to create a linear model
```python
from sklearn import linear_model
```
Now we can fit the data to a linear regression:
```python
regr = linear_model.LinearRegression()
regr.fit(X,y)
```
Finally we can predict the CO2 emissions based on the car's weight, volume, and manufacturer.
```python
##predict the CO2 emission of a Volvo where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
```

Example
```python
import pandas
from sklearn import linear_model

cars = pandas.read_csv("data.csv")
ohe_cars = pandas.get_dummies(cars[['Car']])

X = pandas.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']

regr = linear_model.LinearRegression()
regr.fit(X,y)

##predict the CO2 emission of a Volvo where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])

print(predictedCO2)
```
Result
 [122.45153299]

We now have a coefficient for the volume, the weight, and each car brand in the data set


## Dummifying
It is not necessary to create one column for each group in your category. The information can be retained using 1 column less than the number of groups you have.

For example, you have a column representing colors and in that column, you have two colors, red and blue.

Example
```python
import pandas as pd

colors = pd.DataFrame({'color': ['blue', 'red']})

print(colors)
```
Result
```python
    color
  0  blue
  1   red
```
You can create 1 column called red where 1 represents red and 0 represents not red, which means it is blue.

To do this, we can use the same function that we used for one hot encoding, get_dummies, and then drop one of the columns. There is an argument, drop_first, which allows us to exclude the first column from the resulting table.

Example
```python
import pandas as pd

colors = pd.DataFrame({'color': ['blue', 'red']})
dummies = pd.get_dummies(colors, drop_first=True)

print(dummies)
```python
Result
```python
     color_red
  0          0
  1          1
```
What if you have more than 2 groups? How can the multiple groups be represented by 1 less column?

Let's say we have three colors this time, red, blue and green. When we get_dummies while dropping the first column, we get the following table.

Example
```python
import pandas as pd

colors = pd.DataFrame({'color': ['blue', 'red', 'green']})
dummies = pd.get_dummies(colors, drop_first=True)
dummies['color'] = colors['color']

print(dummies)
```
Result
```python
     color_green  color_red  color
  0            0          0   blue
  1            0          1    red
  2            1          0  green
```


<br><br>