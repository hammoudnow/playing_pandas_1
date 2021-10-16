
import pandas as pd
import numpy as np

df = pd.read_csv("vgsales.csv")
#print (df.info())
#like getting the Mean
mean = df["Global_Sales"].mean()
print ([mean])
#you can get the oldest date  .min()
print (df["Year"].min())
print (df["Year"].max())
#.agg() method is aggregation method that lets you compute summary statistics
def pct30(column):
    return column.quantile(0.3)   #it will return the 30% percantile of any column
df["New_Sales"] = df["Global_Sales"].agg(pct30)
print (df)  #its one value, for all column
multiple_agg = df[["Global_Sales", "Other_Sales"]].agg(pct30)
#print (multiple_agg)
#Cumulative sum .cumsum, you can also have .cummax, .cummin, .cumprod
cum_sum = df["Global_Sales"].cumsum()
print (cum_sum)

#Counting, but first you can drop the duplicates in one of the columns
#the drop.duplicates takes subset which is the column you want to remove its duplicates
dropping_Platform_Duplicates = df.drop_duplicates(subset = "Platform")
#print (dropping_Platform_Duplicates.head(15))

#But if you want to remove duplicates based on two columns which is more logical
#as you can have same platform but different games (which are not actually duplicates)
dropping_two_columns = df.drop_duplicates(subset = ["Platform" , "Genre"])
print (dropping_two_columns.head(15))

#now lets start counting based on the above
print (dropping_two_columns["Genre"].value_counts(sort = True))
#you can also do normalization as proportion of the total
print (dropping_two_columns["Genre"].value_counts(normalize = True))

#.pivot_table() method is just an alternative to .groupby()
pv_tb = df.pivot_table(values="Global_Sales", index = "Platform", columns="Genre", fill_value=0, margins = True)
print (pv_tb.head(5))
