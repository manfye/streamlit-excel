# import statements
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from PIL import Image
from datetime import datetime
import time
from datetime import date
from io import StringIO
import plotly.express as px
import seaborn as sns

# adding title and text in the app


st.sidebar.title("World Happiness Index 2021:")
years_list = ["All","Western Europe", "South Asia", "Southeast Asia", "East Asia", "North America and ANZ","Middle East and North Africa", "Latin America and Caribbean","Central and Eastern Europe","Commonwealth of Independent States","Sub-Saharan Africa"] 

select = st.sidebar.selectbox('Filter the region here:', years_list, key='1')
st.image("https://images.pexels.com/photos/573259/pexels-photo-573259.jpeg?cs=srgb&dl=pexels-matheus-bertelli-573259.jpg&fm=jpg", caption='World Happiness Dataset')
df = pd.read_csv("world-happiness-report-2021.csv")

num_yrs = st.sidebar.slider('Select min Ladder Score', min_value=5, max_value=10, value = 10) # Getting the input.
df = df[df['Ladder score'] <= num_yrs] # Filtering the dataframe.

if select =="All":
    filtered_df = df
else:   
    filtered_df = df[df['Regional indicator']==select]


st.write(filtered_df)

fig = px.scatter(filtered_df,
                x="Logged GDP per capita",
                y="Healthy life expectancy",
                size="Ladder score",
                color="Regional indicator",
                hover_name="Country name",
                size_max=10)
st.write(fig)

st.write(px.bar(filtered_df, y='Ladder score', x='Country name'))

#correlate data
corr = filtered_df.corr()

#using matplotlib to define the size

plt.figure(figsize=(8, 8))

#creating the heatmap with seaborn


fig1 = plt.figure()
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);
st.pyplot(fig1)








# options = st.multiselect(
#      'What are your favorite colors',
#      ['Green', 'Yellow', 'Red', 'Blue'],
#      ['Yellow', 'Red'])

# st.write('You selected:', options)


# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     # To read file as bytes:
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)

#     # To convert to a string based IO:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     st.write(stringio)

#     # To read file as string:
#     string_data = stringio.read()
#     st.write(string_data)

#     # Can be used wherever a "file-like" object is accepted:
#     dataframe = pd.read_csv(uploaded_file)
#     st.write(dataframe)




# def get_user_name():
#     return 'John'

# with st.echo():
#     # Everything inside this block will be both printed to the screen
#     # and executed. !!

#     def get_punctuation():
#         return '!!!'

#     greeting = "Hi there, "
#     value = get_user_name()
#     punctuation = get_punctuation()

#     st.write(greeting, value, punctuation)
