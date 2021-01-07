Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pp
>>> pp.set_option('Max_columns',20)
>>> pp.set_option('display_width',1000)

>>> pp.set_option('display.width',1000)
>>> import os
>>> os.chdir('F:\\python')
>>> gill = pp.read_csv('NSE.csv')
>>> import seaborn as ss
>>> import matplotlib.pyplot as ppt
>>> gill.columns
Index(['Date', 'Open', 'High', 'Low', 'Close', 'Change', 'Year', 'Month', 'Day', 'P Change', 'Candle Type'], dtype='object')
>>> ss.barplot('Year','Open',data=gill,ci=0)

<AxesSubplot:xlabel='Year', ylabel='Open'>
>>> ppt.show()
>>> ss.barplot('Change','Year',data=gill,ci=0,estimator=sum)

<AxesSubplot:xlabel='Change', ylabel='Year'>
>>> ppt.show()
>>> ss.barplot('Year','Change',data=gill,ci=0,estimator=sum)

<AxesSubplot:xlabel='Year', ylabel='Change'>
>>> ppt.show()
>>> ss.barplot('Month','Change',data=gill,ci=0,estimator=sum)

<AxesSubplot:xlabel='Month', ylabel='Change'>
>>> ppt.show()
>>> pp.crosstab(index=gill['Month'],columns=gill['Candle Type'],normalize='index')
Candle Type      Bear      Bull
Month                          
1            0.500000  0.500000
2            0.500000  0.500000
3            0.446154  0.553846
4            0.443983  0.556017
5            0.505535  0.494465
6            0.463768  0.536232
7            0.434028  0.565972
8            0.488722  0.511278
9            0.460076  0.539924
10           0.474104  0.525896
11           0.453815  0.546185
12           0.509804  0.490196
>>> ss.barplot('Day','Change',data=gill,ci=0,estimator=sum)

Warning (from warnings module):
  File "C:\Users\mylappi\AppData\Local\Programs\Python\Python38-32\lib\site-packages\seaborn\_decorators.py", line 36
    warnings.warn(
FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
<AxesSubplot:xlabel='Day', ylabel='Change'>
>>> ppt.show()
>>> pp.crosstab(index=gill['Month'],columns=gill['Candle Type'],normalize='index')

>>> pp.crosstab(index=gill['Day'],columns=gill['Candle Type'],normalize='index')
Candle Type      Bear      Bull
Day                            
Fri          0.441368  0.558632
Mon          0.452951  0.547049
Thu          0.492038  0.507962
Tue          0.491366  0.508634
Wed          0.487421  0.512579
>>> gill.sort_values(by='Change',ascending=False).head(5)
           Date          Open          High           Low         Close  Change  Year  Month  Day  P Change Candle Type
2832  9/20/2019  10746.799810  11381.900390  10691.000000  11274.200200  795.90  2019      9  Fri      7.41        Bull
2956  3/25/2020   7735.149902   8376.750000   7714.750000   8317.849609  715.85  2020      3  Wed      9.25        Bull
328   5/18/2009   3673.149902   4384.299805   3673.149902   4323.149902  651.80  2009      5  Mon     17.74        Bull
2957  3/26/2020   8451.000000   8749.049805   8304.900391   8641.450195  498.10  2020      3  Thu      5.89        Bull
2130  11/9/2016   8067.500000   8476.200195   8002.250000   8432.000000  488.10  2016     11  Wed      6.05        Bull
>>> gill.sort_values(by='Change',ascending=True).head(5)
           Date          Open          High          Low        Close   Change  Year  Month  Day  P Change Candle Type
2951  3/18/2020   9088.450195   9127.549805  8407.049805  8468.799805 -1025.15  2020      3  Wed    -11.28        Bear
2947  3/12/2020  10039.950200  10040.750000  9508.000000  9590.150391  -932.35  2020      3  Thu     -9.29        Bear
2958  3/27/2020   8949.099609   9038.900391  8522.900391  8660.250000  -563.15  2020      3  Fri     -6.29        Bear
3006  6/11/2020  10094.099610  10112.049810  9885.049805  9902.000000  -549.15  2020      6  Thu     -5.44        Bear
14    1/21/2008   5705.000000   5705.000000  4977.100098  5208.799805  -501.65  2008      1  Mon     -8.79        Bear
>>> gill.sort_values(by='P Change',ascending=False).head(5)
            Date          Open          High           Low         Close  Change  Year  Month  Day  P Change Candle Type
328    5/18/2009   3673.149902   4384.299805   3673.149902   4323.149902  651.80  2009      5  Mon     17.74        Bull
2956   3/25/2020   7735.149902   8376.750000   7714.750000   8317.849609  715.85  2020      3  Wed      9.25        Bull
2832   9/20/2019  10746.799810  11381.900390  10691.000000  11274.200200  795.90  2019      9  Fri      7.41        Bull
205   10/31/2008   2696.300049   2921.350098   2696.300049   2885.600098  189.10  2008     10  Fri      7.01        Bull
18     1/25/2008   5035.049805   5399.250000   5035.049805   5383.350098  345.90  2008      1  Fri      6.87        Bull
>>> 