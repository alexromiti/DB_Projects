import streamlit as st
from connection import con
from streamlit_option_menu import option_menu
from queries import total_revenue, most_sold_product, most_sold_brand, most_sold_model, sales_by_state, age_ranking
from queries import total_revenue_2020, most_sold_product_2020, most_sold_brand_2020, most_sold_model_2020, sales_by_state_2020, age_ranking_2020
from queries import total_revenue_2021, most_sold_product_2021, most_sold_brand_2021, most_sold_model_2021, sales_by_state_2021, age_ranking_2021
from queries import total_revenue_2022, most_sold_product_2022, most_sold_brand_2022, most_sold_model_2022, sales_by_state_2022,age_ranking_2022
from infoView import infoView

def show_data_analysis_view():



    #Sidebar menu
    with st.sidebar: 
        selected = option_menu(
            menu_title=None,
            options=["General","2020","2021","2022","Info"],
            icons=["calendar","calendar","calendar","calendar","book"],
            menu_icon="cast",
            default_index=0,
            orientation= 'horizontal'
        )

    if selected == "General":
        st.title("CAMEX SPORTSWEAR")
        total_revenue(con)
        most_sold_product(con)
        most_sold_brand(con)
        most_sold_model(con)
        sales_by_state(con)
        age_ranking(con)
    if selected == "2020":
        total_revenue_2020(con)
        most_sold_product_2020(con)
        most_sold_brand_2020(con)
        most_sold_model_2020(con)
        sales_by_state_2020(con)
        age_ranking_2020(con)

    if selected == "2021":
        total_revenue_2021(con)
        most_sold_product_2021(con)
        most_sold_brand_2021(con)
        most_sold_model_2021(con)
        sales_by_state_2021(con)
        age_ranking_2021(con)

    if selected == "2022":
        total_revenue_2022(con)
        most_sold_product_2022(con)
        most_sold_brand_2022(con)
        most_sold_model_2022(con)
        sales_by_state_2022(con)
        age_ranking_2022(con)

    if selected == "Info":
        infoView()





# Export the show_home_view function
__all__ = ["show_data_analysis_view"]


