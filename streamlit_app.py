import streamlit
import pandas
import requests
import snowflake.connector



streamlit.header ("The fruit load list contains:|") 

#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

# Add a button to load the fruit

if streamlit.button('Get Fruit Load List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_load_list()
      streamlit.dataframe(my_data_rows)
