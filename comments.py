""" st.write("Here's our first attempt at using data to create a table:")


st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe.style.highlight_max(axis=0))
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

x= st.slider('x') # 👈 this is a widget
st.write(x, 'squared is', x*x)
 """

""" x_coordinate = float(50.941303)
y_coordinate = float(6.958138)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [x_coordinate, y_coordinate],
    columns=["lat", "lon"],
)
st.map(map_data)

x_slider = st.slider("x_slider")
y_slider = st.slider("y_slider")
st.write(x_slider, x_coordinate-x_slider)
st.write(y_slider, y_coordinate-y_slider)

st.text_input("Your name", key="name")
st.session_state.name
 """

""" 
if st.checkbox('Show Dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    chart_data """
""" df = DataFrame({
    'first column': [1,2,3,4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best Fam?',
    df['first column']
)
'You selected', option """

""" 
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted ?", ("Email", "Home Phone", "mobile phone")
)

add_slider = st.sidebar.slider("Select a Range of Values", 0.0, 100.0, (25.0, 75.0)) """


""" #add a placeholder 
left_column, right_column = st.columns(2)
# You can use a column just like a sidebar:
left_column.button("press me!")

# or even better, call a streamlit func inside a "with" block:
with right_column:
    chosen = (
        st.radio('Sorting hat', ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    )
    st.write(f"You are in {chosen} house!")
 """
""" st.markdown(
    
    <style>
        .stProgress > div > div > div > div {
          background-color: #8BC6EC;
          background-image: linear-gradient(135deg, #8BC6EC 0%, #9599E2 100%);
        }
    </style>,
    unsafe_allow_html=True,
)
 """

""" # add a placeholder
left_column, right_column = st.columns(2)
# You can use a column just like a sidebar:
left_column.button("press me!")

# or even better, call a streamlit func inside a "with" block:
with right_column:
    chosen = st.radio(
        "Sorting hat", ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")

"Starting a long computation..."
# add a placeholder

latest_iterations = st.empty()
bar = st.progress(0)

for i in range(100):
    # update bar w/ eatch iter.
    latest_iterations.text(f"Iteration{i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"..and now we're done! "
 """

"""
 # First App

from re import X
from numpy import right_shift
from pandas.core.frame import DataFrame
import streamlit as st
import pandas as pd
import random


def _update_slider(name, value):
    st.session_state[name] = value


def _update_slider_x(value):
    st.session_state["number-slider-x"] = value


def _update_slider_y(value):
    st.session_state["number-slider-y"] = value


if "number_slider-x" and "number-slider-y" not in st.session_state:
    st.session_state["number-slider-x"] = 0
    st.session_state["number-slider-y"] = 0


st.button(
    "Update Slider Values",
    on_click=_update_slider,
    kwargs={"value": random.randint(0, 100), "name": "number-slider-x"},
)


@st.cache  # fun will be cached
def mySlowFunction(arg1, arg2):
    # Do smth really slow here!
    checkForFirst = isinstance(arg1, float)
    checkForSecond = isinstance(arg2, float)
    if checkForFirst and checkForSecond:
        calc = arg1 * arg2
        the_output = "Its:", calc, checkForFirst, checkForSecond
        return the_output


coordiantes_slider_x = st.slider(
    "Select calc coordiantes_slider",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    key="number-slider-x",
)

c1, c2 = st.columns(2)

coordiantes_slider_y = st.slider(
    "Select calc coordiantes_slider",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    key="number-slider-y",
)

col1, col2 = st.columns(2)
with col1:
    input = st.number_input(
        "Enter value for x",
        on_change=_update_slider_x,
        key="input-1",
        kwargs=({"value": input}),
    )

with col2:
    input2 = st.number_input(
        "Enter value for y",
        on_change=_update_slider_y,
        key="input-2",
        kwargs=({"value": input2}),
    )

st.write(mySlowFunction(coordiantes_slider_x, coordiantes_slider_y))

 """