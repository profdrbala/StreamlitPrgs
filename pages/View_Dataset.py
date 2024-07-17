import streamlit as st
import pandas as pd

st.markdown("# View Dataset 🎉")
st.sidebar.markdown("# View Dataset 🎉")

   
df1 = pd.read_csv("data.csv")
st.write(df1)
