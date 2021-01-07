Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from nsepy import get_history
>>> gill = get_history("Reliance",start=date(2001,1,1),end=date(2020,12,12))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    gill = get_history("Reliance",start=date(2001,1,1),end=date(2020,12,12))
NameError: name 'date' is not defined
>>> from datetime import date
>>> gill = get_history("Reliance",start=date(2001,1,1),end=date(2020,12,12))

>>> gill
              Symbol Series  ...  Deliverable Volume  %Deliverble
Date                         ...                                 
2001-01-01  RELIANCE     EQ  ...                 NaN          NaN
2001-01-02  RELIANCE     EQ  ...                 NaN          NaN
2001-01-03  RELIANCE     EQ  ...                 NaN          NaN
2001-01-04  RELIANCE     EQ  ...                 NaN          NaN
2001-01-05  RELIANCE     EQ  ...                 NaN          NaN
...              ...    ...  ...                 ...          ...
2020-12-07  RELIANCE     EQ  ...           3706525.0       0.4403
2020-12-08  RELIANCE     EQ  ...           5692600.0       0.2842
2020-12-09  RELIANCE     EQ  ...           4861192.0       0.3610
2020-12-10  RELIANCE     EQ  ...           2670339.0       0.3602
2020-12-11  RELIANCE     EQ  ...           3553151.0       0.2857

[4966 rows x 14 columns]
>>> gill.columns
Index(['Symbol', 'Series', 'Prev Close', 'Open', 'High', 'Low', 'Last',
       'Close', 'VWAP', 'Volume', 'Turnover', 'Trades', 'Deliverable Volume',
       '%Deliverble'],
      dtype='object')
>>> col = ['VWAP', 'Volume', 'Turnover', 'Trades', 'Deliverable Volume',
       '%Deliverble']
>>> for i in range(len(col)):
	gill = gill.drop(col[i],axis= 1)

	
>>> gill.columns
Index(['Symbol', 'Series', 'Prev Close', 'Open', 'High', 'Low', 'Last',
       'Close'],
      dtype='object')
>>> import panads as pp
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    import panads as pp
ModuleNotFoundError: No module named 'panads'
>>> import pandas as pp
>>> import seaborn as ss
>>> import matplotlib.pyplot as ppt
>>> pp.set_option('display.max_columns',22)
>>> pp.set_option('display.width',1000)
>>> gill.insert(len(gill.columns),"Mar Cap(cr)",6762037614*gill['Close'])
>>> gill.insert(len(gill.columns),"Ambani Net W.",gill['Mar Cap(cr)']*46.32/100)
>>> gill.insert(len(gill.columns),"Net Worth Change",(gill['Close']-gill['Open'])/gill['Open']*gill['Ambani Net W'])

>>> gill.insert(len(gill.columns),"Net Worth Change",(gill['Close']-gill['Open'])/gill['Open']*gill['Ambani Net W.'])
>>> gill

>>> gill['Mar Cap(cr)']= gill['Mar Cap(cr)'].astype(int)
>>> gill['Ambani Net W.']=gill['Ambani Net W.'].astype(int)
>>> gill

>>> gill['Mar Cap(cr)'] = int(gill['Open']*6762037614/10000000)

>>> gill['Mar Cap(cr)'] = gill['Open']*6762037614/10000000
>>> gill['Mar Cap(cr)']= gill['Mar Cap(cr)'].astype(int)
>>> gill

>>> gill['Ambani Net W.']= gill['Mar Cap(cr)']*0.4632
>>> gill['Ambani Net W.']=gill['Ambani Net W.'].astype(int)
>>> gill['Net Worth Change']= (gill['Close']-gill['Open'])/gill['Open']*gill['Ambani Net W.']
>>> gill['Net Worth Change']= gill['Net Worth Change'].astype(int)
>>> gill

>>> gill.insert(len(gill.columns),"Net Worth %Change",gill['Net Worth Change']/gill['Ambani Net W.']*100)
>>> gill['Net Worth %Change']= gill['Net Worth %Change'].astype(int)
>>> gill = gill.drop('Prev Close',axis=1)
>>> gill = gill.drop('Series',axis =1)
>>> gill

>>> gill['Net Worth %Change']= gill['Net Worth Change']/gill['Ambani Net W.']*100
>>> gill
              Symbol     Open     High      Low     Last    Close  Mar Cap(cr)  Ambani Net W.  Net Worth Change  Net Worth %Change
Date                                                                                                                              
2001-01-01  RELIANCE   340.00   343.65   339.00   341.20   341.75       229909         106493               548           0.514588
2001-01-02  RELIANCE   340.35   359.00   340.25   358.10   354.30       230145         106603              4369           4.098384
2001-01-03  RELIANCE   355.00   361.70   353.00   358.20   360.05       240052         111192              1581           1.421865
2001-01-04  RELIANCE   359.10   366.90   356.20   357.00   357.80       242824         112476              -407          -0.361855
2001-01-05  RELIANCE   356.50   366.80   356.50   363.40   364.30       241066         111661              2443           2.187872
...              ...      ...      ...      ...      ...      ...          ...            ...               ...                ...
2020-12-07  RELIANCE  1940.60  1965.00  1940.60  1958.35  1958.20      1312241         607830              5512           0.906833
2020-12-08  RELIANCE  1961.15  2014.25  1950.00  1992.45  1993.75      1326137         614266             10210           1.662146
2020-12-09  RELIANCE  2009.95  2033.80  1999.25  2026.00  2026.95      1359135         629551              5324           0.845682
2020-12-10  RELIANCE  2021.60  2028.50  2001.00  2008.00  2007.00      1367013         633200             -4572          -0.722047
2020-12-11  RELIANCE  2013.00  2038.00  1974.25  1999.40  2005.80      1361198         630506             -2255          -0.357649

[4966 rows x 10 columns]
>>> ss.barplot('Net Worth Change',