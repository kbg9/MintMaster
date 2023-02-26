# import streamlit as st
# import pandas as pd

# import os

# if not os.path.exists("pages"):
#     os.makedirs("pages")

# def register():
#     st.title("Registration Page")
#     st.write("Please fill in the following details to register.")
    
#     # Create input fields for user information
#     name = st.text_input("Name")
#     mobile = st.text_input("Mobile Number")
#     uid = st.text_input("UID")
#     api_key = st.text_input("API Key")
    
#     # Save user information to CSV file on submit
#     if st.button("Submit"):
#         # user_df = pd.read_csv("D:/Mint Master Python/GIT/MintMaster/pages/user_info.csv")
#         # new_user = pd.DataFrame({
#         #     "Name": [name],
#         #     "Mobile": [mobile],
#         #     "UID": [uid],
#         #     "API Key": [api_key]
#         # })
#         # user_df = pd.concat([user_df, new_user], ignore_index=True)
#         user_df.to_csv("D:/Mint Master Python/GIT/MintMaster/pages/user_info.csv", index=False)
#         st.success("Registration Successful! Please go to the login page to access your account.")
#         st.markdown("[Click here to go to login page](/login)")

# if __name__ == '__main__':
#     register()









import streamlit as st
import pandas as pd

import os

# if not os.path.exists(""):
#     os.makedirs("")

def register():
    st.title("Registration Page")
    st.write("Please fill in the following details to register.")
    
    # Create input fields for user information
    name = st.text_input("Name")
    mobile = st.text_input("Mobile Number")
    uid = st.text_input("UID")
    api_key = st.text_input("API Key")
    
    # Save user information to CSV file on submit
    if st.button("Submit"):
        user_df = pd.read_csv("D:/Mint Master Python/GIT/MintMaster/pages/user_info.csv")
        new_user = pd.DataFrame({
            "Name": [name],
            "Mobile": [mobile],
            "UID": [uid],
            "API Key": [api_key]
        })
        user_df = pd.concat([user_df, new_user], ignore_index=True)
        user_df.to_csv("D:/Mint Master Python/GIT/MintMaster/pages/user_info.csv", index=False)
        st.success("Registration Successful! Please go to the login page to access your account.")
        st.markdown("[Click here to go to login page](/login)")

if __name__ == '__main__':
    register()
