import streamlit

streamlit.title('My Mom''s New Healthy Diner')
streamlit.header('Breakfast Favorits')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)

## adding user interactive widget:
#import pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# put some pick list
#streamlit.multiselect("Pick some fruites:", list(my_fruit_list.index)) #but this shows numbers, we need to pick another column as index
# display the table on the page
#streamlit.dataframe(my_fruit_list) 

#import pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#streamlit.dataframe(my_fruit_list)

#import pandas  
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
##showing preselected fruits
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
#streamlit.dataframe(my_fruit_list)

import pandas  
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.datafram(fruityvice_normalized)

