import streamlit as st

def infoView():
    st.title("Información del Proyecto")
    
    # Información del proyecto
    institucion = "Universidad Panamericana."
    nombres_integrantes = "Camila Gómez Salas, José Alexander Romero Mitiaeva."
    descripcion = "La intención de este proyecto es analizar y mostrar la información más relevante de la tienda de ropa CAMEX SportsWear, de manera que se puedan mejorar las ventas para el próximo año 2023."
    herramientas = "StreamLit para la interfaz de la página; mysql.connector y mysql para la base de datos; pandas, plotly.express y numpy para el manejo y visualización de los datos; python como lenguaje general de desarrollo."
    
    # Mostrar la información del proyecto
    st.header("")
    st.write(f"**Institución:** {institucion}")
    st.write(f"**Nombres de los integrantes:** {nombres_integrantes}")
    st.write(f"**Descripción del proyecto:** {descripcion}")
    st.write(f"**Herramientas utilizadas:** {herramientas}")

# Export the show_home_view function
__all__ = ["infoView"]