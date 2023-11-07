import streamlit as st
from streamlit_option_menu import option_menu
from dataAnalysisView import show_data_analysis_view



#Sidebar menu
with st.sidebar: 
    selected = option_menu(
        menu_title=None,
        options=["Dashboard"],
        icons=["book"],
        menu_icon="cast",
        default_index=0
    )


if selected == "Dashboard":
    show_data_analysis_view()

