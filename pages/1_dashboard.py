import streamlit as st
import pandas as pd
import numpy as np
import time

st.write('# Fashion Data')

data = pd.read_csv('streamlit_exp/sample_fashion.csv')
st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']
)

st.bar_chart(chart_data)
st.line_chart(chart_data)
st.area_chart(chart_data, y_label= 'amount', x_label='time')

with st.spinner('waiting..'):
    time.sleep(3)
st.success('Done!')