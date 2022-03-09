import streamlit as st
import util

def app():
    st.image('./Streamlit_UI/Header.gif', use_column_width=True)
    st.write("Upload a Picture to see if it is a fake or real face.")
    st.markdown('*Need a face to test? Visit this [link]("https://github.com/kanakmi/Deforgify/tree/main/Model%20Training/dataset")*')
    file_uploaded = st.file_uploader("Choose the Image File", type=["jpg", "png", "jpeg"])
    if file_uploaded is not None:
        res = util.classify_image(file_uploaded)
        c1, buff, c2 = st.columns([2, 0.5, 2])
        c1.image(file_uploaded, use_column_width=True)
        c2.subheader("Classification Result")
        c2.write("The image is classified as **{}**.".format(res['label'].title()))
