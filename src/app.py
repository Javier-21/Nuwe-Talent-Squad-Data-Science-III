# Imports and libraries
import pandas as pd
import numpy as np
import json 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import f1_score

# Load data
df = pd.read_csv("data/train.csv")
df_test = pd.read_csv("data/test.csv")

# Clean data
y_train = np.reshape(df[["parental level of education"]].to_numpy(), 800)
x_train = (df["math score"] + df["reading score"] + df["writing score"]).to_frame()
x_test = (df_test["math score"] + df_test["reading score"] + df_test["writing score"]).to_frame()

#Standarize data
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

# Split data in train-test
x_train_s, x_test_s, y_train_s, y_test_s = train_test_split(x_train, y_train, test_size=0.2, random_state=123)

# Train the model
model = SVC(kernel='rbf', random_state = 123, probability=True)
cv_results_svm = model.fit(x_train_s, y_train_s)
y_pred_s = model.predict(x_test_s)

# Evaluate the model
f1 = f1_score(y_test_s, y_pred_s, average='macro')
print('The F1 Score (macro) is: ', f1)

#Train a new model with all train dataser
model = SVC(kernel='rbf', random_state = 0)
cv_results_svm = model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# Generate the file predictions.json
output = dict()
output["target"] = dict()

for n, index in enumerate(df_test['Unnamed: 0']):
    output['target'][str(index)] = int(y_pred[n])

with open("predictions.json", "w") as write_file:
    predictions = json.dump(output, write_file)