import streamlit as st
import numpy as np
import pandas as pd

st.title('My first app')

st.write("Using data to create a table.")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30 ,40]
}))

s_string = "Second table using magic commands"

s_string

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [15, 25, 35, 45]
})

df

s_line_chart = "Line Chart"
s_line_chart

chart_data = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

plot_a_map = "Plot a Map"
plot_a_map

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)

cbox = "Use checkboxes to show/hide data"
cbox

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c']
    )
    chart_data

#s_box = "Use a selectbox for options"
#s_box

#option = st.selectbox(
#    'Which number do you like best?',
#    df['first column']
#)

#"You selected: ", option

lout = "Lay out your app"
lout

option2 = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected', option2

left, right = st.columns(2)
pressed = left.button("Press me?")
if pressed:
    right.write("woohoo!")
expander = st.expander("FAQ")
expander.write("Here you could in a long explanation")

import time

'Starting a computation'

last_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    last_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'...and now we\'re done!'
