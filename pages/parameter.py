import streamlit as st
import pandas as pd

import os

# if not os.path.exists(""):
#     os.makedirs("")

def parameter():
    st.title("Parameter Page")
    st.write("Please enter the following parameters.")
    
    # Create input fields for symbol, expiry date, max quantity, max stop loss
    symbol = st.text_input("Symbol")
    expiry_date = st.text_input("Expiry Date")
    max_qty = st.number_input("Max Quantity")
    max_stop_loss = st.number_input("Max Stop Loss")
    
    # Save parameters to CSV file on submit
    if st.button("Submit"):
        para_df = pd.read_csv("para.csv")
        new_para = pd.DataFrame({
            "Symbol": [symbol],
            "Expiry Date": [expiry_date],
            "Max Quantity": [max_qty],
            "Max Stop Loss": [max_stop_loss]
        })
        para_df = pd.concat([para_df, new_para], ignore_index=True)
        para_df.to_csv("para.csv", index=False)
        st.success("Parameters Saved Successfully!")
            
if __name__ == '__main__':
    parameter()
