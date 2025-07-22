import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data =pd.read_csv("drugs_side_effects.csv")
print(data)

# TO SHOW MAIN INFORMATION ON DATASET

print(data.info())

# TO SHOW COLUMN QUANTITY AND COLUMN

print("the dataset has {}rows and {} column".format(data.shape[0],data.shape[1]))
print("column:")
print(data.columns)
print(data.head())
data.drop(columns=["brand_names"],inplace=True)
print(data.head())

#FIND DUPLICATE ROWS BASED ON ALL COLUMN

duplicate_rows=data[data.duplicated()]
print(duplicate_rows)

#   COUNT DUPLICATED ROWS

duplicated_count=duplicate_rows.shape[0]
print("count of duplicated_count : ", duplicated_count)
print(data.isnull())

print(data.info())

#CONVERT "RATING " AND "NO_OF_REVIEWS" ATTRIBUTES TO NUMERIC DATA TYPES

data["rating"]=pd.to_numeric(data["rating"],errors="coerce")
data["no_of_reviews"]=pd.to_numeric(data["no_of_reviews"],errors="coerce")
print(data.dtypes.value_counts())
print(data.describe())

# Convert 'activity' to string, remove whitespace and '%'character, 

data["activity"]=data["activity"].astype(str).str.replace(r'\s+', '',regex=True).str.rstrip('%')
print(data["activity"].head())

#CONVERT ACITIVITY STRING DATATYPE INTO NUMERIC

data["activity"]=pd.to_numeric(data["activity"],errors="coerce")

#CONVERT ACITIVITY STRING DATATYPE INTO FLOAT AND DIVIDE BY 100

data["activity"]=data["activity"].astype(float)/100

#DISPLAY THE UPDATED COLUMN OF ACTIVITY

print(data["activity"].head())

#PRINT TOTAL NUMBER OF MISSING VALUES

print(data.isnull().sum())
print("There are {} missing values in this dataset".format(data.isnull().sum().sum()))
print('Number of Instances=%d' % (data.shape[0]))
print('Number of attributes=%s' %(data.shape[1]))
#CHECKING HOW MANY NAN VALUES IN EACH COLUMN OF DATA SET

print("number of missing values:")
for col in data.columns:
     print('\t%s: %d' % (col,data[col].isna().sum()))

# IN ALCOHOL COLUMN WE HAVE X AND NAN VALUES WE WILL REPLACE THIS VALUE BY X BY 1 AND NAN BY 0 WITH BOOLEAN VALUES

data["alcohol"]=data["alcohol"].replace(np.nan,'0')
data["alcohol"]=data["alcohol"].replace({'X':1})
print(data['alcohol'].head())

# TO AVOID MISSING VALUE LETS FILL THEM WITH SOME INFORMATION
#TO AVOID MISSING VALUES LETS FILL WITH SOME INFORMATION WE FILL THE ZERO IN RELATED DRUGS & SIDE_EFFECTS WITH NULL VALUES .

data["side_effects"]=data["side_effects"].fillna("unknown")
data['related_drugs']=data['related_drugs'].fillna("unknown")

#FILL THE NULL VALUES  WITH 0 AS BASE FOR 'RATING' AND 'NO_OF_REVIEWS' COLUMN
# IT WILL SHOW NO INFORMATION ABOUT IT

data['rating']=data['rating'].fillna('0')
data['no_of_reviews']=data['no_of_reviews'].fillna('0')
#FILL NULL VALUES WITH GENERIC_NAME AND DRUG_CLASSES
data['generic_name']=data['generic_name'].replace(np.nan,'UnKnown')
data['drug_classes']=data['drug_classes'].replace(np.nan,'UnKnown')

#LETS  CHECK  rx_otc CATEGORICAL VALUES COLUMN
print(data['rx_otc'].unique())

#LETS CHECK PREGANNANCY CATEGORICAL VALUES COLUMN
print(data['pregnancy_category'].unique())

#FILL NULL VALUE WITH Unknwon AS A BASIC VALUES in rx_otc and pregnancy_category.
data["rx_otc"]=data['rx_otc'].replace('np.nan','Unknown')
data["pregnancy_category"]=data['pregnancy_category'].replace('np.nan','Unknown')

data['no_of_reviews']=pd.to_numeric(data['no_of_reviews'],errors='coerce')
print(data['no_of_reviews'].info())

dfs=data.copy()
print(dfs)

#LETS CHECK ANY MISSINGVALUES LEFT 
print("There are {} missing values in this dataset".format(data.isnull().sum().sum()))
print('Number of Instances=%d' % (data.shape[0]))
print('Number of attributes=%s' %(data.shape[1]))
print("number of missing values:")
for col in data.columns:
     print('\t%s: %d' % (col,data[col].isna().sum()))
data_version2=data.copy()
print(data_version2.head(10))





