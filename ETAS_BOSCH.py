# circuit breaker design pattern

l = [0, 1, 0, 3, 5]  # keep all zeros at the end of the list eg [1,3,5,0,0]

d = {1: 0, 0: 2, 3: 1}  # dictionary sort based on the values

# print(sorted(d.items(), key=lambda x: x[1]))  # What algorithm used backedn in sorted

# Compare s1 and s2 and print success if same s2 is present in s1 in same order
s1 = 'owner'
s2 = 'one'
# t = []
#
# # check = re.compile(['one'])
#
# for i in range(len(s2)):
#     for j in range(len(s1)):
#         if s2[i] == s1[i]:
#             t.append(s2[i])
# print(t)

import pandas

# creation of Dataframe from dictionary
data = {'name': 'vinod', 'salary': '78000'}
# To create a dataframe where dict keys as rows(index) and column names are 0,1,2....
df = pandas.DataFrame(data=data.items())
# print(df)
#         0      1
# 0    name  vinod
# 1  salary  78000
data1 = {'name': ['vinod'], 'salary': ['78000']}
# To create a dataframe where dict keys as columns and index names are 0,1,2....
df = pandas.DataFrame.from_dict(data1)
# print(df)
#     name salary
# 0  vinod  78000


# Creation of df from series
series = pandas.Series([1, 2, 3, 4, 5, 6])
# print(series[0:4])
df = pandas.DataFrame(data=series, columns=['test'])
# print(df)

# creation of pandas from list
k = ['vinod','rashmi','vin','ras']
v = [78000,67000,130000,130000]
dict(zip(k,v))
a=dict(zip(k,v))
df = pandas.DataFrame(a.items(),columns=['name', 'salary'])
# print(df)

# creation of pandas df with tuple and iterate over a pandas dataframe
data = ((1,2),(2,4),(2,4),(5,6))
df = pandas.DataFrame(data,columns=['A','B'], index=['test1', 'test2', 'test3', 'test4'])
#print(df)
# df.items iterate over columns and series data
# for col,data in df.items():
#     print(col)
#     print(data)
# A
# test1    1
# test2    2
# test3    2
# test4    5
# Name: A, dtype: int64
# B
# test1    2
# test2    4
# test3    4
# test4    6
# Name: B, dtype: int64
# df.iteritems iterate over columns and series data
# for col,data in df.iteritems():
    # print(col)
    # print(data)
# A
# test1    1
# test2    2
# test3    2
# test4    5
# Name: A, dtype: int64
# B
# test1    2
# test2    4
# test3    4
# test4    6
# Name: B, dtype: int64

# df.iterrows iterate over index and row series data
inp = [{'c1':10, 'c2':100}, {'c1':11,'c2':110}, {'c1':12,'c2':120}, {'c1':12,'c2':120}]
df = pandas.DataFrame(inp, index=['A','B','C','D'])
# print(df)
# for index, row in df.iterrows():
#     print(row['c1'].dtype, row['c2'])
# # 10 100
# # 11 110
# # 12 120
# drop duplicates from dataframe instantly
# df.drop_duplicates(inplace=True)
#print(df)
# re index we can add or remove the index which will delete or adds row to the existing data frame
# df = df.reindex(index=['A','B','C','D','E'], fill_value=0)
# # df=df.reindex(index=['A','B','C'])
# print(df.shape)
# df['c1'] = df['c1'].astype('float64')
# print(df['c1'].dtype)

# Truncate in data frame
# df = pandas.DataFrame({'A': ['a', 'b', 'c', 'd', 'e'],
#                    'B': ['f', 'g', 'h', 'i', 'j'],
#                    'C': ['k', 'l', 'm', 'n', 'o']},
#                   index=[1, 2, 3, 4, 5])
# print(df)
# df = df.truncate(before=3, after=5, axis=0)
# print(df)

