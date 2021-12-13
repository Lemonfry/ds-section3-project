import pymongo
from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split

client = MongoClient("mongodb+srv://rjs2114:1357@cluster0.7tqlw.mongodb.net/projectDB?retryWrites=true&w=majority")
heart_db = client["db_1"]
heart_collection = heart_db["collection_1"]
heart_df = pd.DataFrame(list(heart_collection.find()))
# heart_df = heart_df[0:0]

heart_df = heart_df.drop(['_id'], axis=1)
heart_df = heart_df.dropna(axis=1)
heart_df = heart_df.astype(int)
target = 'HeartDiseaseorAttack'
features = heart_df.drop(columns=[target]).columns
# print(heart_df)
train, test = train_test_split(heart_df, test_size=0.20, stratify=heart_df[target], random_state=2)
train, val = train_test_split(train, test_size=0.20, stratify=train[target], random_state=2)
# print(train)
X_train = train[features]
y_train = train[target]
X_val = val[features]
y_val = val[target]
X_test = test[features]
y_test = test[target]

from category_encoders import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from xgboost import XGBClassifier

ord = OrdinalEncoder()
xgbc = make_pipeline(
    OrdinalEncoder(),
    StandardScaler(),
    XGBClassifier(verbosity=0, n_jobs=-1)
    )

xgbc.fit(X_train, y_train)

print('분류 훈련 정확도: ', xgbc.score(X_train, y_train))
print('분류 검증 정확도: ', xgbc.score(X_val, y_val))

from sklearn.metrics import accuracy_score
y_pred = xgbc.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print('분류 테스트 정확도: ', acc)

import pickle
with open('xgbc.pkl','wb') as pickle_file:
    pickle.dump(xgbc, pickle_file)