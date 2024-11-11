# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cCynAaE3NNiygxhil9WopTCDwquOeGB0
"""

import streamlit as st
import streamlit.components.v1 as components

st.title("Indian Air Quality Index Dashboard")

# Embed the Power BI dashboard
components.html(
    """
    <iframe title="Indian Air Quality Index new final" width="600" height="373.5"
    src="https://app.powerbi.com/view?r=eyJrIjoiZjdlZjg3NDUtNjcwNC00MWY3LWE5OWYtZTIxZDQ4NTY0NDliIiwidCI6ImRjNTdkYjliLWNjNTQtNDI5Yi1iOWU4LTBhZmZhMzZmMDY2NiJ9"
    frameborder="0" allowFullScreen="true"></iframe>
    """,
    height=400
)