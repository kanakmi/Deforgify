import streamlit as st
import dashboard
import classifyPage

st.set_page_config(
    page_title="Deforgify",
    page_icon="🤖",
    layout="wide")

PAGES = {
    "Dashboard": dashboard,
    "Classify Image": classifyPage
}

st.sidebar.title("Deforgify")

st.sidebar.write("Deforgify is a tool that utilizes the power of Deep Learning to distinguish Real images from the Fake ones.")

st.sidebar.subheader('Navigation:')
selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()