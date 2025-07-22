import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv("drugs_side_effects_drugs_com_version2.csv")
print(df)
print(df['pregnancy_category'].unique())
print(df['csa'].unique())
print(df['rx_otc'].unique())
print(df['generic_name'].unique())
print(df['medical_condition'].unique())

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['csa']=label_encoder.fit_transform(df['csa'])
df['rx_otc']=label_encoder.fit_transform(df['rx_otc'])
df['generic_name']=label_encoder.fit_transform(df['generic_name'])
df['medical_condition']=label_encoder.fit_transform(df['medical_condition'])
df['pregnancy_category']=label_encoder.fit_transform(df['pregnancy_category'])
df['side_effects']=label_encoder.fit_transform(df['side_effects'])
print(df['generic_name'].unique())
print(df['rx_otc'].unique())
print(df['csa'].unique())
print(df['side_effects'].unique())
print(df['medical_condition'].unique())
df_1=pd.DataFrame(df,columns=('generic_name',
 'medical_condition', 'no_of_reviews', 'side_effects', 'rating',
 'csa', 'pregnancy_category', 'rx_otc', 'alcohol'))
print(df_1.head(10))
# print(df_1.info())

# Convert all columns to numeric, coercing errors

for col in df_1.columns:
    df_1[col] = pd.to_numeric(df_1[col], errors='coerce')

#The StandardScaler from the sklearn.preprocessing module is used to standardize features by removing the mean and scaling to unit variance.   

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
print(scaler.fit(df_1))
scaled_data = scaler.fit_transform(df_1)
print(scaled_data)


df_std = pd.DataFrame(scaler.fit_transform(df_1),columns=df_1.columns)
print(df_std)

plt.figure(figsize=(12, 8))
sns.heatmap(df_1.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
print(plt.show())

data_ver =pd.read_csv('drugs_side_effects_drugs_com_version2.csv')
print(data_ver)

# CHECK FOR OCCUREENCE AND FREQUENCY OF MEDICAL CONDITION.SORTED HIGHEST TO LOWEST.

medical_condition_counts=data_ver['medical_condition'].value_counts().sort_values(ascending=False)

print("\nMedical condition occurrence and frequency (sorted from highest to lowest):")
print(medical_condition_counts)

 # Save the results to CSV files if needed
medical_condition_counts.to_csv('medical_condition_counts.csv')

# Importing necessary libraries for processing text

from collections import Counter
import re

# Function to extract side effects from text, split by semicolons
def extract_side_effects(text):

 # Split the text on semicolons then strip whitespace

    return [effect.strip() for effect in re.split(r'[;]', text)]



# Extract and count occurrences of side effects


side_effects =data_ver['side_effects'].dropna().apply(extract_side_effects).explode()
print(side_effects)

side_effect_counts =side_effects.value_counts().sort_values(ascending=False)

print("\nSide effects occurrence and frequency (sorted from highest to lowest):")

print(side_effect_counts)

 # Save the side effect counts to a CSV file

side_effect_counts.to_csv('side_effect_counts.csv')


 # Function to extract drug classes from text, split by commas

def extract_drug_classes(text):
 # Split the text on commas then strip whitespace
    return [effect.strip() for effect in re.split(r'[,]',text)]

 # Extract and count occurrences of drug classes
drug_classes = data_ver['drug_classes'].dropna().apply(extract_drug_classes).explode()
drug_classes_counts = drug_classes.value_counts().sort_values(ascending=False)
print("\nDrug Classes occurrence and frequency (sorted from highest to lowest):")

print(drug_classes_counts)
drug_classes_counts.to_csv('drug_classes_counts.csv')

 # Define functions to check for specific side effects and create new boolean columns

def has_hives(text):
    return 'hives' in text.lower()
data_ver['Hives'] = data_ver['side_effects'].apply(has_hives)

def has_difficult_breathing(text):
 return 'difficult breathing' in text.lower() or 'difficulty breathing' in text.lower()
data_ver['Difficult Breathing'] =data_ver['side_effects'].apply(has_difficult_breathing)

def has_itching(text):
 return 'itching' in text.lower()
data_ver['Itching'] = data_ver['side_effects'].apply(has_itching)

 # Define functions to check for specific drug classes and createnew boolean columns

def is_usc(text):
 return 'Upper respiratory combinations' in text
data_ver['Upper respiratory combinations'] = data_ver['drug_classes'].apply(is_usc)

def is_steriods(text):
 return 'Topical steroids' in text
data_ver['Topical steroids'] =data_ver['drug_classes'].apply(is_steriods)

def is_acne(text):
 return 'Topical acne agents' in text
data_ver['Topical acne agents'] =data_ver['drug_classes'].apply(is_acne)

 # Define functions to check for specific medical conditions and create new boolean columns

def has_pain(text):
 return 'Pain' in text
data_ver['Pain'] =data_ver['medical_condition'].apply(has_pain)

def has_colds_and_flu(text):
 return 'Colds & Flu' in text
data_ver['Colds & Flu'] =data_ver['medical_condition'].apply(has_colds_and_flu)

def has_acne(text):
 return 'Acne' in text
data_ver['Acne'] =data_ver['medical_condition'].apply(has_acne)


 # Plot the count of occurrences for each side effect

 # Plot count of Hives

data_ver['Hives'].value_counts().plot(kind='bar')
plt.title('Count of Hives')
plt.xlabel('Hives')
plt.ylabel('Count')
plt.xticks([0, 1], ['False', 'True'], rotation=0)
plt.show()

 # Plot count of Difficult Breathing

data_ver['Difficult Breathing'].value_counts().plot(kind='bar')
plt.title('Count of Difficult Breathing')
plt.xlabel('Difficult Breathing')
plt.ylabel('Count')
plt.xticks([0, 1], ['False', 'True'], rotation=0)
plt.show()

 # Plot count of Itching

data_ver['Itching'].value_counts().plot(kind='bar')
plt.title('Count of Itching')
plt.xlabel('Itching')
plt.ylabel('Count')
plt.xticks([0, 1], ['False', 'True'], rotation=0)
plt.show()

 # Plot count of Upper respiratory combinations

data_ver['Upper respiratory combinations'].value_counts().plot(kind='bar')
plt.title('Count of Upper respiratory combinations')
plt.xlabel('Upper respiratory combinations')
plt.ylabel('Count')
plt.xticks([0, 1], ['False', 'True'], rotation=0)
plt.show()

 # Plot count of Topical steroids

data_ver['Topical steroids'].value_counts().plot(kind='bar')
plt.title('Count of Topical steroids')
plt.xlabel('Topical steroids')
plt.ylabel('Count')
plt.xticks([0, 1], ['False', 'True'], rotation=0)
plt.show()

plt.boxplot('pregnancy_category')
plt.title(f"Box-plot to see the pregnancy categories of drugs")
plt.show()

plt.boxplot('activities')
plt.title(f"Box Plot of activites for each disease")
plt.show()