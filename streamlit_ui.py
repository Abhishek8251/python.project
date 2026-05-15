import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="CRUD File Manager", layout="centered")

st.title("📁 File Management System")

file_name = st.text_input("Enter File Name")
content = st.text_area("File Content")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Create"):
        if Path(file_name).exists():
            st.warning("File already exists!")
        else:
            with open(file_name, "w") as f:
                f.write(content)
            st.success("File Created Successfully!")

with col2:
    if st.button("Read"):
        if Path(file_name).exists():
            with open(file_name, "r") as f:
                st.text_area("File Output", f.read(), height=200)
        else:
            st.error("File Not Found!")

with col3:
    if st.button("Update"):
        if Path(file_name).exists():
            with open(file_name, "w") as f:
                f.write(content)
            st.success("File Updated!")
        else:
            st.error("File Not Found!")

with col4:
    if st.button("Delete"):
        if Path(file_name).exists():
            os.remove(file_name)
            st.success("File Deleted!")
        else:
            st.error("File Not Found!")