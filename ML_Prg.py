import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
import streamlit as st 


df = pd.read_csv("data.csv")
ds=df.dropna()
x = ds.drop("price", axis=1)
y = ds["price"]
model = LinearRegression()
model.fit(x, y)
        
def main(): 
    st.title("House Price Predictor")
   
    area = st.text_input("area","0")
    rooms = st.text_input("rooms","0")
    
    if st.button("Predict"):
        new_house= [[int(area),int(rooms)]]
        price= model.predict(new_house)            

        st.success("{} {}".format("House Price will be" , int(price)))
      
if __name__=='__main__': 
    main()
