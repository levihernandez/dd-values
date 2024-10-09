# tests/test_app.py
import streamlit as st
from streamlit import session_state

def test_app():
    # Simulate a run of the Streamlit app
    session_state.clear()  # Clear session state to prevent interference

    # Define a simple Streamlit app for testing
    st.title("Test App")
    st.write("This is a test.")

    # Check if the title is rendered correctly
    assert st.session_state.get('title') == "Test App"
