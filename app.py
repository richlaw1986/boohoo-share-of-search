
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


st.set_page_config(page_title=None, page_icon=None, layout='wide', initial_sidebar_state='auto')

DATA_URL = (
    "boohoo-absolute-data.csv"
)

st.title("Boohoo Share of Search Dashboard")
st.sidebar.title("Choose an Option")


@st.cache(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

data = load_data()

DATA_URL2 = (
    "boohoo-relative-data.csv"
)

@st.cache(persist=True)
def load_data():
    data_two = pd.read_csv(DATA_URL2)
    data_two['Date'] = pd.to_datetime(data_two['Date'])
    return data_two

data_two = load_data()

st.sidebar.markdown("### Choose View")
select = st.sidebar.selectbox('Metric', ['Relative Trend', 'Absolute Trends'], key='5')
if not st.sidebar.checkbox("Hide", False, key=5):
    if select == 'Relative Trend':
        st.markdown("#### The graph shows estimated weekly search volume by brand - by combining a relative Google Trends score over the past 5 years with an estimated search volume for each brand. Zoom into to any time period over the past 5 years by selecting a portion of the graph, then zoom back out by double-clicking.")
        fig_31 = px.line(data_two, x="Date", y="Estimated Weekly Search Volume", color="Brand",  title='Relative Trends by Brand')
        st.plotly_chart(fig_31, use_container_width=True)
    if select == 'Absolute Trends':
        st.markdown("#### The graphs show the trend for each brand in isolation on a weekly basis over the past 5 years.  Zoom into to any time period over the past 5 years by selecting a portion of the graph, then zoom back out by double-clicking.")
        fig_26 = px.line(data, x="Date", y="Boohoo",  title='Boohoo Absolute Trend')
        st.plotly_chart(fig_26, use_container_width=True)
        fig_27 = px.line(data, x="Date", y="ASOS",  title='ASOS Absolute Trend')
        st.plotly_chart(fig_27, use_container_width=True)
        fig_28 = px.line(data, x="Date", y="Missguided",  title='Missguided Absolute Trend')
        st.plotly_chart(fig_28, use_container_width=True)
        fig_29 = px.line(data, x="Date", y="PrettyLittleThing", title='PrettyLittleThing Absolute Trends')
        st.plotly_chart(fig_29, use_container_width=True)
        fig_30 = px.line(data, x="Date", y="Nasty Gal",  title="Nast Galy Absolute Trend")
        st.plotly_chart(fig_30, use_container_width=True)
