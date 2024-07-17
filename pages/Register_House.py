import streamlit as st
import streamlit as st
import pandas as pd

st.markdown("# Register ❄️")
st.sidebar.markdown("# Register ❄️")



st.title("House Price App")
area = st.text_input("Enter house squre foot")
room = st.text_input("Enter number of rooms")
price = st.text_input("Enter house Price")

file = "data.csv"

data = {
    'area': [area],
    'room': [room],
    'price': [price],
    }

# Make data frame of above data
df = pd.DataFrame(data)
if(st.button('Submit')):
# append data frame to CSV file
    df.to_csv(file, mode='a', index=False, header=False)
        # success
    st.success("Successfully stored")

        


