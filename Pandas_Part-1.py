#Create a series from array
#Example 1

# import pandas as pd
# import numpy as np
# data = np.array(['a','b','c','d'])
# s = pd.Series(data)
# print (s)

#Example 2

# import pandas as pd
# import numpy as np
# data = np.array(['a','b','c','d','e'])
# s = pd.Series(data, index=[1,2,3,4,5])
# print (s)

#Create a series from dict
#Example 1

# import pandas as pd
# data = {'Index': 'Numbers', 'a': 0., 'b': 1., 'c': 2.}
# c = pd.Series(data)
# print(c)

#Retrive data Using Label

# import pandas as pd 
# s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# print (s[['a','b','e']])

#Create an Empty DataFrame
#Example 1

# import pandas as pd
# df = pd.DataFrame()
# print(df)

# example 2

# import pandas as pd
# data = [1,2,3,4,5,6]
# df = pd.DataFrame(data)
# print(df)

# example 3

# import pandas as pd
# data = [['SITE1','Afraaz',10],['SITE2','Ithris',20],['SITE3','Irfan',30]]
# df = pd.DataFrame(data,columns=['Location','Name','Age'],index=[1,2,3])
# df['Age'] = df['Age'].astype(float)
# print(df)

#Create a DataFrame from Dict of ndarrays / Lists
#Example 1 

# import pandas as pd
# data = {'Name':['Syed','Jack','Ram','Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data)
# print(df)

# importing data from weather in Json format
#Example 1

# import requests
# import json
# api_key = "3de3adda05dc30643c3b901868801434"
# city=input()
# url="https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric"% (city, api_key)
# # url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
# response = requests.get(url)
# data = json.loads(response.text)
# print(data)
# print("the temperature in {} ".format(city)+str(data["main"]["temp"]))

#Example 2

# import pandas as pd
# data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
#            'team': ['CSK', 'MI', 'MI', 'SRH', 'KKR', 'CSK','CSK', 'CSK'],
#            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
#            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
# ipl = pd.DataFrame(data)
# print (ipl)
# print(ipl.describe())
# ipl.info()
# print(ipl.head(5))
# print(ipl.tail(10))

#Sorting
# print(ipl.sort_values(by=['year','wins'],ascending=False,ignore_index=True))
# print(ipl.columns)
# print(ipl.shape)
# print(ipl.size)
# print(ipl.empty)
# print(ipl.isna())
# print(ipl.isna().sum())

#printing the mathematical operations

# print(ipl["wins"]/1)
# print(ipl["wins"]+1)
# print(ipl["wins"]-1)
# print(ipl["wins"]*1)

# Saving a dataframe in Diffrent format

# ipl.to_csv("imam.csv")
# ipl.to_html("imam.html")
# ipl.to_json('imam.json')
# ipl.to_xml('imam.xml')

#Saving a file in parquet format

# import pandas as pd

# data = {
#     'Name': ['John', 'Emily'],
#     'Age': [25, 28],
#     'Gender': ['Male', 'Female']
# }

# df = pd.DataFrame(data)

# df.to_parquet('data.parquet', index=False)

#Reading a parquet file

# a=pd.read_parquet("C:/Users/Mohamed Imamrila/Downloads/Data Science/data.parquet")
# print(a)

#Saving DataFrame as a OCR

# import pyarrow.orc as orc

# data = {
#     'Name': ['John', 'Emily', 'David'],
#     'Age': [25, 28, 30],
#     'Gender': ['Male', 'Female', 'Male'],
#     'Salary': [5000, 6000, 5500],
#     'Join_Date': pd.to_datetime(['2022-01-01', '2022-02-01', '2022-03-01'])
# }

# df = pd.DataFrame(data)

# df.to_orc('data.orc', index=False)

# print(ipl.nlargest(3,"wins"))
# print(ipl.nsmallest(3,"wins"))
# print(ipl.nunique())
# print(ipl['team'].unique())

## Experiment 1 ##

# import pandas as pd

# def create_dataframe():
#     # '''
#     # Create a pandas dataframe called 'olympic_medal_counts_df' containing
#     # the data from the table of 2014 Sochi winter olympics medal counts.

#     # The columns for this dataframe should be called
#     # 'country_name', 'gold', 'silver', and 'bronze'.

#     # There is no need to  specify row indexes for this dataframe
#     # (in this case, the rows will automatically be assigned numbered indexes).

#     # '''

#    Data = {"countries":['Russian Fed.', 'Norway', 'Canada', 'United States',
#                  'Netherlands', 'Germany', 'Switzerland', 'Belarus',
#                  'Austria', 'France', 'Poland', 'China', 'Korea',
#                  'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
#                  'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
#                  'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan'], 
#     "gold" : [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], 
#     "silver" : [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0], 
#     "bronze" : [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]}
#    olympic_medal_counts_df = pd.DataFrame(Data)
#    olympic_medal_counts_df["Total Medal"] = olympic_medal_counts_df['gold']+['silver']+['bronze']
#    olympic_medal_counts_df.to_csv("olympic_medal_counts_df.csv")
#    return olympic_medal_counts_df
# create_dataframe()

# import pandas as pd
# data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
#            'team': ['CSK', 'MI', 'MI', 'SRH', 'KKR', 'CSK','CSK', 'CSK'],
#            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
#            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
# ipl = pd.DataFrame(data)
# print (ipl)

## Sperating a Coloumn 

# x = ipl.columns[3]
# print(x)
# ipl[x]

## iloc Function ##

# print(ipl.iloc[3])
# print(ipl.iloc[1,3])
# print(ipl.iloc[[1,3]])

## Slicing in iloc Fuction 

# print(ipl.iloc[1:3,0:3])

## Drop Fuction

# print(ipl.drop(columns='wins',inplace= True))
# print(ipl.drop(index=0))

## Unique Function

# print(ipl["team"].unique())

## Concat, Merge Function ##

## Concat Function ##
 
# import pandas as pd
# data1 = {
# 'ID': ['1','2','3','4','5'],
# 'Feature1': ['A','B','C','D','E'],
# 'Feature2': ['L','M','N',"O",'P']
# }
# df1 = pd.DataFrame(data1, columns = ["ID", "Feature1", "Feature2","Feature3"])
# # print(df1)
# d2 = {
# 'ID': ['1','3','6','7','8',"9"],
# 'Feature1': ['AB','BC','CD','DE','EF',"fd"],
# 'Feature2': ['KL','LM','M-N',"N-O",'O-P',"rd"]
# }
# df2 = pd.DataFrame(d2, columns = ["ID", "Feature1", "Feature2"])
# print(df2)
# DF = pd.concat([df1,df2],ignore_index=True)
# print(DF)
# DF1 = pd.concat([df1,df2],keys=["1st","2nd"])
# # print(DF1)
# DF2 = pd.concat([df1,df2],sort=True,axis=0) ## axis = 0 is row and axis = 1 is a coloumn ##
# # print(DF2)
# DFFR = df1["ID"]+df2["Feature1"]
# print(DFFR)

## Merge Function ##

# DF_merge_i= pd.merge(df1,df2, on ="ID", how = 'inner')
# DF_merge_r= pd.merge(df1,df2, on ="ID", how = 'right')
# DF_merge_l= pd.merge(df1,df2, on ="ID", how = 'left')
# DF_merge_o= pd.merge(df1,df2, on ="ID", how = 'outer')

# print(DF_merge_i)
# print(DF_merge_r)
# print(DF_merge_l)
# print(DF_merge_o)

## Join Function ##

# f = df1.join(df2["Feature1"],rsuffix="s").join(df2["Feature2"],rsuffix="z")
# print(f)


## GROUP BY FUNCTION ##

import pandas as pd
titanic = pd.read_csv("https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/titanic_train.csv")
titanic.head(10)