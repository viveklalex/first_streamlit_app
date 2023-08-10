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

# Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):

            
            
            with my_cnx.cursor() as my_cur:
            
            my_cur.execute("insert into fruit_load_list values ('from streamlit')")
            return "Thanks for adding " + new_fruit
            
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List"):
        my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
        back_from_function = insert_row_snowflake(add_my_fruit)
        streamlit.text(back_from_function)
