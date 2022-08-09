import numpy as np  # linear algebra
import pandas as pd  # for data preparation
import plotly.express as px  # for data visualization
from textblob import TextBlob  # for sentiment analysis

#importing files
dff = pd.read_csv('cleaned_202108.csv')
dff = pd.read_csv('cleaned_202109.csv')
dff = pd.read_csv('cleaned_202110.csv')
dff = pd.read_csv('cleaned_202111.csv')
dff = pd.read_csv('cleaned_202112.csv')
dff = pd.read_csv('cleaned_202201.csv')
dff = pd.read_csv('cleaned_202202.csv')
dff = pd.read_csv('cleaned_202203.csv')
dff = pd.read_csv('cleaned_202204.csv')
dff = pd.read_csv('cleaned_202205.csv')
dff = pd.read_csv('cleaned_202206.csv')
dff = pd.read_csv('cleaned_202207.csv')

dff.shape

var = dff.columns


#Day Number Referance
data = pd.read_csv('DOW.csv')
print("For day number referance see chart:")
print(data)

#user pie chart
z = dff.groupby(['member_casual']).size().reset_index(name='counts')
pieChart = px.pie(z, values='counts', names='member_casual',
                  title='Distribution of User Types',
                  color_discrete_sequence=px.colors.qualitative.Set3)
pieChart.show()

#day pie chart
z = dff.groupby(['WEEKDAY']).size().reset_index(name='counts')
pieChart = px.pie(z, values='counts', names='WEEKDAY',
                  title='Distribution of Days Used',
                  color_discrete_sequence=px.colors.qualitative.Set3)

#bike type pie chart
z = dff.groupby(['rideable_type']).size().reset_index(name='counts')
pieChart = px.pie(z, values='counts', names='rideable_type',
                  title='Distribution of Bikes Used',
                  color_discrete_sequence=px.colors.qualitative.Set3)

pieChart.show()

