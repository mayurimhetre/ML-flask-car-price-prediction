import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



df = pd.read_csv('car data.csv')
df['Fuel_Type'].value_counts()
df['Seller_Type'].value_counts()
df['Transmission'].value_counts()
df['Owner'].value_counts()
#df_1 = [feature for feature in df.columns if df[feature].dtypes == 'object']

#for feature in df_1:
#   plt.bar(df[feature],df['Selling_Price'])
#   plt.show()


df2 = 2021 - df['Year']
df['NewYear'] = df2
df.drop(['Car_Name','Year'],axis =1,inplace=True)
final_dataset = pd.get_dummies(df,drop_first=True)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()

X = final_dataset.drop('Selling_Price', axis =1)
y = final_dataset['Selling_Price']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
lm.fit(X_train,y_train)

pred = lm.predict(X_test)

from sklearn.metrics import r2_score
re= r2_score(y_test, pred)
print("r2 value is",re)
#sns.distplot(y_test-pred)
from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, pred))
print('MSE:', metrics.mean_squared_error(y_test, pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, pred)))

print(X_train.columns)

import pickle
# open a file, where you ant to store the data
file = open('random_forest_regression_model_01.pkl', 'wb')

# dump information to that file
pickle.dump(lm, file)