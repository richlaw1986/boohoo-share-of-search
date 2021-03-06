
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from PIL import Image


st.set_page_config(page_title=None, page_icon=None, layout='wide', initial_sidebar_state='auto')

DATA_URL = (
    "boohoo-absolute-data.csv"
)

st.title("Share of Search Dashboard")

#with open("style.css") as f:
#    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
image = Image.open('boohoo.png')
st.sidebar.image(image)
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

#st.sidebar.markdown("### Choose View")
select = st.sidebar.selectbox('Metric', ['Compare Trends', 'Individual Trends'], key='5')
if not st.sidebar.checkbox("Hide", False, key=5):
    if select == 'Compare Trends':
        st.markdown("#### The graph shows estimated weekly search volume by brand - by combining a relative Google Trends score over the past 5 years with an estimated search volume for each brand. Zoom into to any time period over the past 5 years by selecting a portion of the graph, then zoom back out by double-clicking.")
        fig_31 = px.line(data_two, x="Date", y="Estimated Weekly Search Volume", color="Brand",  title='Weekly Searches by Brand')
        st.plotly_chart(fig_31, use_container_width=True)
    if select == 'Individual Trends':
        st.markdown("#### The graphs show the trend for each brand in isolation on a weekly basis over the past 5 years.  Zoom into to any time period over the past 5 years by selecting a portion of the graph, then zoom back out by double-clicking.")
        fig_26 = px.line(data, x="Date", y="Boohoo",  title='Boohoo Trend')
        st.plotly_chart(fig_26, use_container_width=True)
        fig_27 = px.line(data, x="Date", y="ASOS",  title='ASOS Trend')
        st.plotly_chart(fig_27, use_container_width=True)
        fig_28 = px.line(data, x="Date", y="Missguided",  title='Missguided Trend')
        st.plotly_chart(fig_28, use_container_width=True)
        fig_29 = px.line(data, x="Date", y="PrettyLittleThing", title='PrettyLittleThing Trend')
        st.plotly_chart(fig_29, use_container_width=True)
        fig_30 = px.line(data, x="Date", y="Nasty Gal",  title="Nasty Gal Trend")
        st.plotly_chart(fig_30, use_container_width=True)
