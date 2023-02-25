import streamlit as st

# # Import the pages
# from pages import login, registration, parameter
from pages.login import login
from pages.registration import register
from pages.parameter import parameter


# Define the page dictionary
PAGES = {
    "Login": login,
    "Registration": register,        
    "Set Parameters": parameter
}


# Define the app function
def app():
    # Add a sidebar to the app
    st.sidebar.title("Navigation")
    # Create a dropdown menu in the sidebar for the app pages
    page = st.sidebar.selectbox("Select a page", options=list(PAGES.keys()))
    # Run the app function corresponding to the selected page
    PAGES[page]()

if __name__ == "__main__":
    app()
# Set the page title and icon
# st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:")

# # Add a menu to the sidebar to navigate between pages
# st.sidebar.title("Navigation")
# selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# # Display the selected page with the page function
# page = PAGES[selection]
# page.app()
