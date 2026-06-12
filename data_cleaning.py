import pandas as pd

# load dataset
df = pd.read_excel("Amazon 2_Raw.xlsx")

# preview
print(df.head())
print(df.info())

# remove duplicates
df = df.drop_duplicates()

# rename columns
df.columns = ['order_id','order_date','geography','category','product_name','sales','quantity','profit']

# missing values check
print(df.isnull().sum())

# handle missing
df['sales'] = df['sales'].fillna(0)
df['profit'] = df['profit'].fillna(0)
df['quantity'] = df['quantity'].fillna(1)

# convert date
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')



# numeric conversion
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['profit'] = pd.to_numeric(df['profit'], errors='coerce')



# split geography 
geo_split = df['geography'].str.split(',', expand=True)
df['country'] = geo_split[0]
df['city'] = geo_split[1]
df['state'] = geo_split[2]

# new columns
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month

# profit margin 
df['profit_margin'] = df['profit'] / df['sales']
df['profit_margin'] = df['profit_margin'].replace([float('inf'), -float('inf')], 0)

# final save
df.to_csv("cleaned_data.csv", index=False)

print("Data Cleaning + Transformation Done ")