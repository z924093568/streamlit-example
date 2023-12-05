import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
"""
# Zhang Zixuan streamlit app :balloon:!

The app is used to plot the time series within different CompanyID!
"""

pd_data = pd.read_pickle(filepath_or_buffer='./pd_data.pkl')

option = st.selectbox(
        'Select a CompanyID',
        pd_data.index.levels[0])

st.write(f'You selected CompanyID: {option}')

def line_charts(pd_data: pd.DataFrame, companyID: int):
    pd_data_t = pd_data.copy()
    sub = pd_data_t.loc[companyID]
    sub.reset_index(inplace=True)
    fig = px.line(sub, x="DataDate", y="PD", title=f'time series of Company {companyID}')
    return fig

fig = line_charts(pd_data, option)

st.plotly_chart(fig, use_container_width=True)
