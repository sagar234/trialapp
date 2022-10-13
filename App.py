from datetime import date
from pyexpat import model
from re import X
from sqlite3 import Date
from tkinter import Y
from types import CoroutineType
from unicodedata import name
import pandas as pd
import os
from pathlib import Path
import streamlit as st
import plotly.express as px 
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel (r'MMR01-10-2022Update Data.xlsx')
st.header('MMR_Report')
st.dataframe(df)
pie_chart = px.pie(df,
                   title='Model MTD(P)',
                   values='MTD(P)',
                   names= 'Model')
st.plotly_chart(pie_chart)
pie_chart2 = px.pie(df,
                   title='Model MTD(A)',
                   values='MTD(A)',
                   names= 'Model')
st.plotly_chart(pie_chart2)
pie_chart3 = px.pie(df,
                   title='Model Trip(A)',
                   values='Trip(A)',
                   names= 'Model')
st.plotly_chart(pie_chart3)
pie_chart4 = px.pie(df,
                   title='Model Trip(P)',
                   values='Trip(P)',
                   names= 'Model')
st.plotly_chart(pie_chart4)
pie_chart5 = px.pie(df,
                   title='Model Trip(P)',
                   values='Trip(P)',
                   names= 'City')
st.plotly_chart(pie_chart5)


