import streamlit as st
import pandas as pd

import os

if not os.path.exists("pages"):
    os.makedirs("pages")

def login():
    st.title("Login Page")
    st.write("Please enter your UID and API Key to login.")
    
    # Create input fields for UID and API Key
    uid = st.text_input("UID")
    api_key = st.text_input("API Key")
    
    # Check UID and API Key in user_info.csv on login button click
    if st.button("Login"):
        user_df = pd.read_csv("D:/Mint Master Python/GIT/MintMaster/pages/user_info.csv")
        print(user_df) # check the loaded dataframe
        print("UID entered: ", uid)
        print("API Key entered: ", api_key)

        if (float(uid) in user_df["UID"].values) and (float(api_key) in user_df["API Key"].values):
            st.success("Login Successful!")
            st.markdown("[Click here to go to Set Parameter page](/parameter)")
        else:
            st.error("Invalid UID or API Key. Please try again.")

        # if (str(uid) in user_df["UID"].astype(str).values) and (str(api_key) in user_df["API Key"].astype(str).values):
        #     st.success("Login Successful!")
        #     st.markdown("[Click here to go to Set Parameter page](/parameter)")
        # else:
        #     st.error("Invalid UID or API Key.")


        # if (uid in user_df["UID"].tolist()) and (api_key in user_df["API Key"].tolist()):
        #     st.success("Login Successful!")
        #     st.markdown("[Click here to go to Set Parameter page](/parameter)")
        # else:
        #     st.error("Invalid UID or API Key.")



        # if (uid in user_df["UID"].values) and (api_key in user_df["API Key"].values):
        #     st.success("Login Successful!")
        #     st.markdown("[Click here to go to Set Parameter page](/parameter)")
        # else:
        #     st.error("Invalid UID or API Key.")
            
if __name__ == '__main__':
    login()

