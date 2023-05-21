import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)

## adding user interactive widget:
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# put some pick list
streamlit.multiselect("Pick some fruites:", list(my_fruit_list.index)) #but this shows numbers, we need to pick another column as index
# display the table on the page
streamlit.dataframe(my_fruit_list)

# lets change the index to get the fruit names
import pandas
my_fruit_list = pandas.read("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# should get the fruit names, then set index to fruit column
my_fruit_list = my_fruit_list.set_index('Fruit')  
streamlit.multiselect("Pick some fruits:" list(my_fruit_list.index)
streamlit.datafram(my_fruit_list)                      


