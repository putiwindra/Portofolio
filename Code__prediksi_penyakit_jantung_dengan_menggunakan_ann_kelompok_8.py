# -*- coding: utf-8 -*-
"""Laporan _Prediksi Penyakit Jantung dengan Menggunakan ANN_Kelompok 8

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1juD5w0Tvdx-YUbmS0_2svtT3vDBbqBxJ

<h1 style="font-family: Source Sans Pro; padding: 12px; font-size: 48px; color: #0171bb; text-align: center; line-height: 1.25;"><b>Heart Failure EDA & ANN Modeling </span></b><br><span style="color: #0180d4; font-size: 24px"></h1>
<hr>

# <div style="font-family: Trebuchet MS; color: #0171bb; padding: 12px; line-height: 1.5;"> 1. About Data  </div>
<div style="font-family: Segoe UI; line-height: 2; color: #000000; text-align: justify">

1. **age**: age of person  
2. **Sex**: Male or Female
3. **ChestPinType** : any pain in the area of your chest

  **ASY = Asymptomatic**

  **NAP = Non Anginal pain**

  **ATA = Atypical Angina**

  **TA = Typical Angina**

4. **Restin BP** : Resting Blood Pressure (Hypertension)
5. **Cholesterol** : Cholesterol level in the blood
6. **fasting BS** : A fasting blood sugar (FBS) level is the result of a blood sample taken after a patient fasts for at least eight hours, 1 = if FastingBS > 120 mg/dl, 0 = otherwise
7. **Resting ECG**:is a non-invasive test that can detect abnormalities including arrhythmias, evidence of coronary heart disease, left ventricular hypertrophy and bundle branch blocks
8. **MaxHR** : Maximum Heart Rate
9. **ExerciseAngina** : If person do angina exercise or not, Y = Yes, N = No
10. **Oldpeak**: ST depression induced by exercise relative to rest
11. **ST_Slope** : The ST segment shift relative to exercise-induced increments in heart rate

   **Up = upsloping**

 **Flat = flat**

  **Down = downsloping**

# <div style="font-family: Trebuchet MS; color: #0171bb; padding: 12px; line-height: 1.5;"> 2. Importing Data  </div>
<div style="font-family: Segoe UI; line-height: 2; color: #000000; text-align: justify">
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
from plotly.subplots import make_subplots
from collections import Counter
from sklearn.metrics import confusion_matrix, accuracy_score, plot_confusion_matrix
from sklearn.metrics import classification_report
# %matplotlib inline
init_notebook_mode(connected= True)

data=pd.read_csv('heart.csv')

data.shape

data.head()

data.columns

for i in data.columns :
    print(i)
    print(data[i].value_counts())
    print('-'*100)

data.info()

data.isnull().sum()

fig=px.pie(data,names=['Positive','Negative'],values=data['HeartDisease'].value_counts(),hole=0.5,
           title="<b>Precentage of Positive and Negative ",template='plotly',color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_layout(title_font_size=12)
fig.show()

counts0 = Counter(data[data['HeartDisease']==0]['Sex'])
counts1 = Counter(data[data['HeartDisease']==1]['Sex'])
fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]])

fig.add_trace(go.Pie(
     values=[item[1] for item in sorted(counts0.items())],
     labels=[item[0] for item in sorted(counts0.items())],
     domain=dict(x=[0, 0.5]),
     name=" Negative",title=' Negative'),
     row=1, col=1)
fig.update_traces(marker=dict(colors=['#19D3F3', '#FF6692']))
fig.add_trace(go.Pie(
     values=[item[1] for item in sorted(counts1.items())],
     labels=[item[0] for item in sorted(counts1.items())],
     domain=dict(x=[0.5, 1.0]),
     name=" Positive",title=' Positive'),
    row=1, col=2)

fig.update_layout(
    title={'text':'HeartDisease  vs Sex','xanchor':'left','yanchor': 'top','y':0.9,'x':0.35},
    xaxis_title="X Axis Title",
    yaxis_title="Y Axis Title",
    legend_title="Sex",
    font=dict(size=18)
)

fig.show()

plt.figure(figsize=(12,7))
sns.countplot(data['HeartDisease'],hue=data['ChestPainType'])

counts0 = Counter(data[data['HeartDisease']==0]['FastingBS'])
counts1 = Counter(data[data['HeartDisease']==1]['FastingBS'])
fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]])

fig.add_trace(go.Pie(
     values=[item[1] for item in sorted(counts0.items())],
     labels=[item[0] for item in sorted(counts0.items())],
     domain=dict(x=[0, 0.5]),
     name=" Negative",title=' Negative'),
     row=1, col=1)
fig.update_traces(marker=dict(colors=['#19D3F3', '#FF97FF']))
fig.add_trace(go.Pie(
     values=[item[1] for item in sorted(counts1.items())],
     labels=[item[0] for item in sorted(counts1.items())],
     domain=dict(x=[0.5, 1.0]),
     name=" Positive",title=' Positive'),
    row=1, col=2)

fig.update_layout(
    title={'text':'HeartDisease  vs FastingBS','xanchor':'left','yanchor': 'top','y':0.9,'x':0.35},
    xaxis_title="X Axis Title",
    yaxis_title="Y Axis Title",
    legend_title="FastingBS",
    font=dict(size=18)
)
fig.show()

sns.set(rc={'figure.figsize':(25,9)})
sns.set_theme(style="whitegrid")
ax = sns.countplot(x='RestingBP',hue='HeartDisease',palette=['#66C4CC',"#F59F70"],data=data)
ax.set_title('Stroke/Non stroke cases at various glucose Levels').set_fontsize(22)
ax.set_xlabel('MaxHR',fontsize=14)
ax.set_ylabel('Count',fontsize=14)

str_only = data[data['HeartDisease'] == 1]
no_str_only = data[data['HeartDisease'] == 0]

plt.figure(figsize=(15,7))
sns.countplot(data['HeartDisease'],hue=data['ExerciseAngina'])

counts0 = Counter(data[data['HeartDisease']==0]['RestingECG'])
counts1 = Counter(data[data['HeartDisease']==1]['RestingECG'])
fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]])

fig.add_trace(go.Pie(
     values=[item[1] for item in sorted(counts0.items())],
     labels=[item[0] for item in sorted(counts0.items())],
     domain=dict(x=[0, 0.5]),
     name=" Negative",title=' Negative'),
     row=1, col=1)
fig.update_traces(marker=dict(colors=['#19D3F3', '#FF97FF']))
fig.add_trace(go.Pie(
     values=[item[1] for item in sorted(counts1.items())],
     labels=[item[0] for item in sorted(counts1.items())],
     domain=dict(x=[0.5, 1.0]),
     name=" Positive",title=' Positive'),
    row=1, col=2)

fig.update_layout(
    title={'text':'HeartDisease  vs RestingECG','xanchor':'left','yanchor': 'top','y':0.9,'x':0.35},
    xaxis_title="X Axis Title",
    yaxis_title="Y Axis Title",
    legend_title="RestingECG",
    font=dict(size=18)
)
fig.show()

"""# <div style="font-family: Trebuchet MS; color: #0171bb; padding: 12px; line-height: 1.5;"> 3. Missing Values  </div>
<div style="font-family: Segoe UI; line-height: 2; color: #000000; text-align: justify">


"""

data.Cholesterol.value_counts()

"""### '0' is missing values

"""

data['Cholesterol'] = data['Cholesterol'].replace([0],np.nan)

df2=data.copy()

df2.Cholesterol.value_counts()

#The distribution of the data of the column
plt.figure(figsize=(15,10))
sns.displot(data = df2, x = "Cholesterol", kde = True,color='#ff77bb')

df2.isnull().sum()

#filling the missings randomly
fill_list = data["Cholesterol"].dropna()
df2 = data["Cholesterol"].fillna(pd.Series(np.random.choice(fill_list, size = len(data.index))))
df2

df2.value_counts()

df2.isnull().sum()

#checking the distribution after filling the missing values randomly
sns.displot(df2, kde = True, color = "Purple")

df3 = data["Cholesterol"].fillna(data["Cholesterol"].mean())
df3

#checking the distribution after filling the missing values with the mean
sns.displot(df3, kde = True, color = "Purple")

data["Cholesterol"] = df2
data.head()

data.Cholesterol.value_counts()

"""# <div style="font-family: Trebuchet MS; color: #0171bb; padding: 12px; line-height: 1.5;"> 4. Outliers </div>
<div style="font-family: Segoe UI; line-height: 2; color: #000000; text-align: justify">

"""

sns.set(rc = {'figure.figsize':(8,6)})
sns.stripplot(y="Age", x ="HeartDisease", data = data)

sns.set(rc = {'figure.figsize':(8,6)})
sns.stripplot(y="RestingBP", x ="HeartDisease", data = data)

#Handling the outliers in this column
data = data.loc[(data["RestingBP"]>80)]
data.head()

#re-checking for the outliers
sns.stripplot(y="RestingBP", x ="HeartDisease", data = data, palette='viridis')

sns.set(rc = {'figure.figsize':(8,6)})
sns.stripplot(y="Cholesterol", x ="HeartDisease", data = data)

#Handling the outliers in this column
data = data.loc[(data["Cholesterol"]<450)]
data.head()

#re-checking for the outliers
sns.stripplot(y="Cholesterol", x ="HeartDisease", data = data, palette='viridis')

sns.set(rc = {'figure.figsize':(8,6)})
sns.stripplot(y="MaxHR", x ="HeartDisease", data = data)

"""# <div style="font-family: Trebuchet MS; color: #0171bb; padding: 12px; line-height: 1.5;"> 5. Encoding  </div>
<div style="font-family: Segoe UI; line-height: 2; color: #000000; text-align: justify">

"""

data.info()

from sklearn.preprocessing import LabelEncoder, MinMaxScaler
gender_le = LabelEncoder()
data["Sex"] = gender_le.fit_transform(data["Sex"])

data.Sex.value_counts()

ChestPainType_le = LabelEncoder()
data["ChestPainType"] = ChestPainType_le.fit_transform(data["ChestPainType"])

data.ChestPainType.value_counts()

RestingECG_le = LabelEncoder()
data["RestingECG"] = RestingECG_le.fit_transform(data["RestingECG"])

data.RestingECG.value_counts()

ExerciseAngina_le = LabelEncoder()
data["ExerciseAngina"] = ExerciseAngina_le.fit_transform(data["ExerciseAngina"])

data.ExerciseAngina.value_counts()

ST_Slope_le = LabelEncoder()
data["ST_Slope"] = ST_Slope_le.fit_transform(data["ST_Slope"])

data.ST_Slope.value_counts()

data.info()

plt.figure(figsize=(12,12))
sns.heatmap(data.corr(),annot=True,cmap="BuPu")

data.isnull().sum()

"""# <div style="font-family: Trebuchet MS; color: #0171bb; padding: 12px; line-height: 1.5;"> 6. Feature Selection  </div>
<div style="font-family: Segoe UI; line-height: 2; color: #000000; text-align: justify">


"""

from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2,f_classif

X=data.drop('HeartDisease',axis=1).values
y=data['HeartDisease'].values

X

X.shape

y.shape

FeatureSelection=SelectPercentile(score_func=f_classif,percentile=80)
X_Sel=FeatureSelection.fit_transform(X,y)

X_Sel.shape

FeatureSelection.get_support()

X_Sel

"""# <div style="font-family: Trebuchet MS; color: #0171bb; padding: 12px; line-height: 1.5;"> 7. Scalling  </div>
<div style="font-family: Segoe UI; line-height: 2; color: #000000; text-align: justify">
    
****
"""

from sklearn.preprocessing import StandardScaler
scalr=StandardScaler(copy=True,with_mean=True,with_std=True)
X=scalr.fit_transform(X_Sel)

X

"""# <div style="font-family: Trebuchet MS; color: #0171bb; padding: 12px; line-height: 1.5;"> 8. Split data  </div>
<div style="font-family: Segoe UI; line-height: 2; color: #000000; text-align: justify">
    
****

"""

from sklearn.model_selection import train_test_split

X_Sel.shape

y.shape

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42,shuffle=True)

"""# <div style="font-family: Trebuchet MS; color: #0171bb; padding: 12px; line-height: 1.5;"> 9. Modeling  </div>
<div style="font-family: Segoe UI; line-height: 2; color: #000000; text-align: justify">
    
****

# ANN
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras import callbacks

model=Sequential()

model.add(Dense(16, activation='swish')) # First hidden layer
model.add(Dropout(0.25))
model.add(Dense(16, activation='swish')) # Second hidden layer
model.add(Dropout(0.25))
model.add(Dense(1, activation='sigmoid')) # Output layer

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['Accuracy'])

earlystopping = callbacks.EarlyStopping(monitor='val_loss',
                                        mode='min',
                                        verbose=1,
                                        patience=20)

history = model.fit(X_train, y_train,validation_data=(X_test,y_test), batch_size = 32, epochs = 500, callbacks =[earlystopping])

# summarize history for acc
plt.plot(history.history['Accuracy'])
plt.plot(history.history['val_Accuracy'])
plt.title('Model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='lower right')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')
plt.show()

print('Max val_acc achieved: %.2f' %(max(history.history['val_Accuracy'])*100), '%')
print('Max acc achieved: %.2f' %(max(history.history['Accuracy'])*100), '%')

print('Final val_acc achieved: %.2f' %(history.history['val_Accuracy'][-1]*100), '%')
print('Final acc achieved: %.2f' %(history.history['Accuracy'][-1]*100), '%')

y_pred = model.predict(X_test)

y_pred = (y_pred > 0.5)

ann_cm = confusion_matrix(y_test, y_pred)
ann_acc = round(accuracy_score(y_pred,y_test) * 100, 2)
print(ann_cm)
print(ann_acc,'%')

print(classification_report(y_pred,y_test))