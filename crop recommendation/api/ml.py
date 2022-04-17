import pandas as pd
import numpy as np
import xgboost as xgb
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
#######################################################################
data = pd.read_csv('data/Crop_recommendation.csv')

labels = ['rice', 'blackgram', 'maize', 'watermelon', 'jute', 'cotton']

rice = data.loc[data.label == 'rice']
blackgram = data.loc[data.label == 'blackgram']
maize = data.loc[data.label == 'maize']
watermelon = data.loc[data.label == 'watermelon']
jute = data.loc[data.label == 'jute']
cotton = data.loc[data.label == 'cotton']

df = pd.concat([rice, blackgram, maize, watermelon, jute, cotton])
df.drop(labels=['rainfall'], axis=1, inplace=True)

features = [col for col in df.columns if col not in ['label']]

print(features)
target = 'label'
print(target)

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

#########################################################

encoder = LabelEncoder()

y_train_ = encoder.fit_transform(y_train)
y_test_ = encoder.transform(y_test)


model = XGBClassifier(random_state = 1, use_label_encoder=False)
_ = model.fit(X_train, y_train_, eval_metric='mlogloss')

with open('encoder.pkl', 'wb') as f:
    pickle.dump(encoder, f)

with open('crop_recommendation_model.pkl', 'wb') as f:
    pickle.dump(model, f)
