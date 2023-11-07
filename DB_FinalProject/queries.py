import streamlit as st
from connection import con
import pandas as pd
import plotly.express as px
import numpy as np




def total_revenue(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT DATE_FORMAT(date_purchase, '%Y-%m') AS month,
                SUM(quantity * price) AS total_revenue
            FROM sales
            JOIN products ON sales.id_product = products.id_product
            GROUP BY month
            ORDER BY month;
        ''')
        rows = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        rows = []

    df = pd.DataFrame(rows, columns=['Month', 'Total'])

    # Calculate trendline using NumPy
    x = np.arange(len(df))
    y = df['Total']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    trendline = p(x)

    # Add trendline to the DataFrame
    df['Trendline'] = trendline

    # Create a line chart with trendline using Plotly
    fig = px.line(df, x='Month', y=['Total', 'Trendline'])
    
    # Update layout to add title
    fig.update_layout(title='Total Revenue Over Time')

    # Display the chart in the Streamlit app
    st.plotly_chart(fig)

    # Calculate total revenue
    total_revenue = df['Total'].sum()

    # Add metric to dashboard
    st.metric("Total Revenue", f"${total_revenue:.2f}")

# Export the total_revenue function
__all__ = ["total_revenue"]


def total_revenue_2020(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT DATE_FORMAT(date_purchase, '%Y-%m') AS month,
                SUM(quantity * price) AS total_revenue
            FROM sales
            JOIN products ON sales.id_product = products.id_product
            WHERE YEAR(date_purchase) = 2020
            GROUP BY month
            ORDER BY month;
        ''')
        rows = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        rows = []

    df = pd.DataFrame(rows, columns=['Month', 'Total'])

    # Calculate trendline using NumPy
    x = np.arange(len(df))
    y = df['Total']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    trendline = p(x)

    # Add trendline to the DataFrame
    df['Trendline'] = trendline

    # Create a line chart with trendline using Plotly
    fig = px.line(df, x='Month', y=['Total', 'Trendline'])
    
    # Update layout to add title
    fig.update_layout(title='Total Revenue 2020')

    # Display the chart in the Streamlit app
    st.plotly_chart(fig)

    # Calculate total revenue
    total_revenue = df['Total'].sum()

    # Add metric to dashboard
    st.metric("Total Revenue", f"${total_revenue:.2f}")

# Export the total_revenue function
__all__ = ["total_revenue_2020"]

def total_revenue_2021(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT DATE_FORMAT(date_purchase, '%Y-%m') AS month,
                SUM(quantity * price) AS total_revenue
            FROM sales
            JOIN products ON sales.id_product = products.id_product
            WHERE YEAR(date_purchase) = 2021
            GROUP BY month
            ORDER BY month;
        ''')
        rows = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        rows = []

    df = pd.DataFrame(rows, columns=['Month', 'Total'])

    # Calculate trendline using NumPy
    x = np.arange(len(df))
    y = df['Total']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    trendline = p(x)

    # Add trendline to the DataFrame
    df['Trendline'] = trendline

    # Create a line chart with trendline using Plotly
    fig = px.line(df, x='Month', y=['Total', 'Trendline'])
    
    # Update layout to add title
    fig.update_layout(title='Total Revenue 2021')

    # Display the chart in the Streamlit app
    st.plotly_chart(fig)

    # Calculate total revenue
    total_revenue = df['Total'].sum()

    # Add metric to dashboard
    st.metric("Total Revenue", f"${total_revenue:.2f}")

# Export the total_revenue function
__all__ = ["total_revenue_2021"]


def total_revenue_2022(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT DATE_FORMAT(date_purchase, '%Y-%m') AS month,
                SUM(quantity * price) AS total_revenue
            FROM sales
            JOIN products ON sales.id_product = products.id_product
            WHERE YEAR(date_purchase) = 2022
            GROUP BY month
            ORDER BY month;
        ''')
        rows = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        rows = []

    df = pd.DataFrame(rows, columns=['Month', 'Total'])

    # Calculate trendline using NumPy
    x = np.arange(len(df))
    y = df['Total']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    trendline = p(x)

    # Add trendline to the DataFrame
    df['Trendline'] = trendline

    # Create a line chart with trendline using Plotly
    fig = px.line(df, x='Month', y=['Total', 'Trendline'])
    
    # Update layout to add title
    fig.update_layout(title='Total Revenue 2022')

    # Display the chart in the Streamlit app
    st.plotly_chart(fig)

    # Calculate total revenue
    total_revenue = df['Total'].sum()

    # Add metric to dashboard
    st.metric("Total Revenue", f"${total_revenue:.2f}")

# Export the total_revenue function
__all__ = ["total_revenue_2022"]

def most_sold_product(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT p.name_product, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            GROUP BY p.name_product
            ORDER BY total_quantity DESC
            LIMIT 1;
        ''')
        row = cursor.fetchone()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        row = None

    if row:
        product_name, total_quantity = row
        st.write(f"The most sold product is '{product_name}' with a total quantity of {total_quantity}.")

        # Get data for bar chart
        cursor.execute('''
            SELECT p.name_product, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            GROUP BY p.name_product
            ORDER BY total_quantity DESC;
        ''')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Product', 'Total Quantity'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Product', y='Total Quantity', title='Sales by Product', color='Product')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["most_sold_product"]

def most_sold_product_2020(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT p.name_product, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2020
            GROUP BY p.name_product
            ORDER BY total_quantity DESC
            LIMIT 1;
        ''')
        row = cursor.fetchone()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        row = None

    if row:
        product_name, total_quantity = row
        st.write(f"The most sold product is '{product_name}' with a total quantity of {total_quantity}.")

        # Get data for bar chart
        cursor.execute('''
            SELECT p.name_product, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2020
            GROUP BY p.name_product
            ORDER BY total_quantity DESC;
        ''')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Product', 'Total Quantity'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Product', y='Total Quantity', title='Sales by Product', color='Product')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["most_sold_product_2020"]

def most_sold_product_2021(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT p.name_product, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2021
            GROUP BY p.name_product
            ORDER BY total_quantity DESC
            LIMIT 1;
        ''')
        row = cursor.fetchone()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        row = None

    if row:
        product_name, total_quantity = row
        st.write(f"The most sold product is '{product_name}' with a total quantity of {total_quantity}.")

        # Get data for bar chart
        cursor.execute('''
            SELECT p.name_product, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2021
            GROUP BY p.name_product
            ORDER BY total_quantity DESC;
        ''')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Product', 'Total Quantity'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Product', y='Total Quantity', title='Sales by Product', color='Product')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["most_sold_product_2021"]


def most_sold_product_2022(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT p.name_product, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2022
            GROUP BY p.name_product
            ORDER BY total_quantity DESC
            LIMIT 1;
        ''')
        row = cursor.fetchone()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        row = None

    if row:
        product_name, total_quantity = row
        st.write(f"The most sold product is '{product_name}' with a total quantity of {total_quantity}.")

        # Get data for bar chart
        cursor.execute('''
            SELECT p.name_product, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2022
            GROUP BY p.name_product
            ORDER BY total_quantity DESC;
        ''')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Product', 'Total Quantity'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Product', y='Total Quantity', title='Sales by Product', color='Product')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["most_sold_product_2022"]



def most_sold_brand(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT p.brand, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            GROUP BY p.brand
            ORDER BY total_quantity DESC
            LIMIT 1;
        ''')
        row = cursor.fetchone()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        row = None

    if row:
        brand, total_quantity = row
        st.write(f"The most sold product brand is '{brand}' with a total quantity of {total_quantity}.")

        # Get data for bar chart
        cursor.execute('''
            SELECT p.brand, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            GROUP BY p.brand
            ORDER BY total_quantity DESC;
        ''')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Brand', 'Total Quantity'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Brand', y='Total Quantity', title='Sales by Brand', color='Brand')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")


# Export the total_revenue function
__all__ = ["most_sold_brand"]

def most_sold_brand_2020(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT p.brand, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2020
            GROUP BY p.brand
            ORDER BY total_quantity DESC
            LIMIT 1;
        ''')
        row = cursor.fetchone()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        row = None

    if row:
        brand, total_quantity = row
        st.write(f"The most sold product brand is '{brand}' with a total quantity of {total_quantity}.")

        # Get data for bar chart
        cursor.execute('''
            SELECT p.brand, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2020
            GROUP BY p.brand
            ORDER BY total_quantity DESC;
        ''')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Brand', 'Total Quantity'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Brand', y='Total Quantity', title='Sales by Brand', color='Brand')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")


# Export the total_revenue function
__all__ = ["most_sold_brand_2020"]


def most_sold_brand_2021(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT p.brand, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2021
            GROUP BY p.brand
            ORDER BY total_quantity DESC
            LIMIT 1;
        ''')
        row = cursor.fetchone()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        row = None

    if row:
        brand, total_quantity = row
        st.write(f"The most sold product brand is '{brand}' with a total quantity of {total_quantity}.")

        # Get data for bar chart
        cursor.execute('''
            SELECT p.brand, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2021
            GROUP BY p.brand
            ORDER BY total_quantity DESC;
        ''')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Brand', 'Total Quantity'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Brand', y='Total Quantity', title='Sales by Brand', color='Brand')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")


# Export the total_revenue function
__all__ = ["most_sold_brand_2021"]


def most_sold_brand_2022(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT p.brand, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2022
            GROUP BY p.brand
            ORDER BY total_quantity DESC
            LIMIT 1;
        ''')
        row = cursor.fetchone()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        row = None

    if row:
        brand, total_quantity = row
        st.write(f"The most sold product brand is '{brand}' with a total quantity of {total_quantity}.")

        # Get data for bar chart
        cursor.execute('''
            SELECT p.brand, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2022
            GROUP BY p.brand
            ORDER BY total_quantity DESC;
        ''')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Brand', 'Total Quantity'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Brand', y='Total Quantity', title='Sales by Brand', color='Brand')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")


# Export the total_revenue function
__all__ = ["most_sold_brand_2022"]

def most_sold_model(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT p.model, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            GROUP BY p.model
            ORDER BY total_quantity DESC
            LIMIT 1;
        ''')
        row = cursor.fetchone()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        row = None

    if row:
        model, total_quantity = row
        st.write(f"The most sold product model is '{model}' with a total quantity of {total_quantity}.")

        # Get data for bar chart
        cursor.execute('''
            SELECT p.model, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            GROUP BY p.model
            ORDER BY total_quantity DESC;
        ''')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Model', 'Total Quantity'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Model', y='Total Quantity', title='Sales by Model', color='Model')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["most_sold_model"]

def most_sold_model_2020(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT p.model, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2020
            GROUP BY p.model
            ORDER BY total_quantity DESC
            LIMIT 1;
        ''')
        row = cursor.fetchone()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        row = None

    if row:
        model, total_quantity = row
        st.write(f"The most sold product model is '{model}' with a total quantity of {total_quantity}.")

        # Get data for bar chart
        cursor.execute('''
            SELECT p.model, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2020
            GROUP BY p.model
            ORDER BY total_quantity DESC;
        ''')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Model', 'Total Quantity'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Model', y='Total Quantity', title='Sales by Model', color='Model')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["most_sold_model_2020"]


def most_sold_model_2021(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT p.model, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2021
            GROUP BY p.model
            ORDER BY total_quantity DESC
            LIMIT 1;
        ''')
        row = cursor.fetchone()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        row = None

    if row:
        model, total_quantity = row
        st.write(f"The most sold product model is '{model}' with a total quantity of {total_quantity}.")

        # Get data for bar chart
        cursor.execute('''
            SELECT p.model, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2021
            GROUP BY p.model
            ORDER BY total_quantity DESC;
        ''')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Model', 'Total Quantity'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Model', y='Total Quantity', title='Sales by Model', color='Model')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["most_sold_model_2021"]


def most_sold_model_2022(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT p.model, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2022
            GROUP BY p.model
            ORDER BY total_quantity DESC
            LIMIT 1;
        ''')
        row = cursor.fetchone()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        row = None

    if row:
        model, total_quantity = row
        st.write(f"The most sold product model is '{model}' with a total quantity of {total_quantity}.")

        # Get data for bar chart
        cursor.execute('''
            SELECT p.model, SUM(s.quantity) AS total_quantity
            FROM sales s
            JOIN products p ON s.id_product = p.id_product
            WHERE YEAR(s.date_purchase) = 2022
            GROUP BY p.model
            ORDER BY total_quantity DESC;
        ''')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Model', 'Total Quantity'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Model', y='Total Quantity', title='Sales by Model', color='Model')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["most_sold_model_2022"]

def sales_by_state(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT c.state, COUNT(*) AS total_sales
            FROM sales s
            JOIN customers c ON s.id_customer = c.id_customer
            GROUP BY c.state
            ORDER BY total_sales DESC;
        ''')
        rows = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        rows = []

    if rows:
        df = pd.DataFrame(rows, columns=['State', 'Total Sales'])

        # Create a pie chart using Plotly
        fig = px.pie(df, values='Total Sales', names='State', title='Sales by State')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["sales_by_state"]


def sales_by_state_2020(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT c.state, COUNT(*) AS total_sales
            FROM sales s
            JOIN customers c ON s.id_customer = c.id_customer
            WHERE YEAR(s.date_purchase) = 2020
            GROUP BY c.state
            ORDER BY total_sales DESC;
        ''')
        rows = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        rows = []

    if rows:
        df = pd.DataFrame(rows, columns=['State', 'Total Sales'])

        # Create a pie chart using Plotly
        fig = px.pie(df, values='Total Sales', names='State', title='Sales by State')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["sales_by_state_2020"]



def sales_by_state_2021(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT c.state, COUNT(*) AS total_sales
            FROM sales s
            JOIN customers c ON s.id_customer = c.id_customer
            WHERE YEAR(s.date_purchase) = 2021
            GROUP BY c.state
            ORDER BY total_sales DESC;
        ''')
        rows = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        rows = []

    if rows:
        df = pd.DataFrame(rows, columns=['State', 'Total Sales'])

        # Create a pie chart using Plotly
        fig = px.pie(df, values='Total Sales', names='State', title='Sales by State')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["sales_by_state_2021"]

def sales_by_state_2022(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT c.state, COUNT(*) AS total_sales
            FROM sales s
            JOIN customers c ON s.id_customer = c.id_customer
            WHERE YEAR(s.date_purchase) = 2022
            GROUP BY c.state
            ORDER BY total_sales DESC;
        ''')
        rows = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        rows = []

    if rows:
        df = pd.DataFrame(rows, columns=['State', 'Total Sales'])

        # Create a pie chart using Plotly
        fig = px.pie(df, values='Total Sales', names='State', title='Sales by State')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["sales_by_state_2022"]

def age_ranking_2020(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT
                CASE
                    WHEN age < 18 THEN '0-17'
                    WHEN age >= 18 AND age < 25 THEN '18-24'
                    WHEN age >= 25 AND age < 35 THEN '25-34'
                    WHEN age >= 35 AND age < 45 THEN '35-44'
                    WHEN age >= 45 AND age < 55 THEN '45-54'
                    ELSE '55+'
                END AS age_interval,
                COUNT(*) AS total_products
            FROM sales s
            JOIN customers c ON s.id_customer = c.id_customer
            WHERE YEAR(s.date_purchase) = 2020
            GROUP BY age_interval
            ORDER BY total_products DESC;
        ''')
        rows = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        rows = []

    if rows:
        df = pd.DataFrame(rows, columns=['Age Interval', 'Total Products'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Age Interval', y='Total Products', title='Product Sales by Age Interval', color='Age Interval')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["age_ranking_2020"]




def age_ranking_2021(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT
                CASE
                    WHEN age < 18 THEN '0-17'
                    WHEN age >= 18 AND age < 25 THEN '18-24'
                    WHEN age >= 25 AND age < 35 THEN '25-34'
                    WHEN age >= 35 AND age < 45 THEN '35-44'
                    WHEN age >= 45 AND age < 55 THEN '45-54'
                    ELSE '55+'
                END AS age_interval,
                COUNT(*) AS total_products
            FROM sales s
            JOIN customers c ON s.id_customer = c.id_customer
            WHERE YEAR(s.date_purchase) = 2021
            GROUP BY age_interval
            ORDER BY total_products DESC;
        ''')
        rows = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        rows = []

    if rows:
        df = pd.DataFrame(rows, columns=['Age Interval', 'Total Products'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Age Interval', y='Total Products', title='Product Sales by Age Interval', color='Age Interval')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["age_ranking_2021"]

def age_ranking(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT
                CASE
                    WHEN age < 18 THEN '0-17'
                    WHEN age >= 18 AND age < 25 THEN '18-24'
                    WHEN age >= 25 AND age < 35 THEN '25-34'
                    WHEN age >= 35 AND age < 45 THEN '35-44'
                    WHEN age >= 45 AND age < 55 THEN '45-54'
                    ELSE '55+'
                END AS age_interval,
                COUNT(*) AS total_products
            FROM sales s
            JOIN customers c ON s.id_customer = c.id_customer
            GROUP BY age_interval
            ORDER BY total_products DESC;
        ''')
        rows = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        rows = []

    if rows:
        df = pd.DataFrame(rows, columns=['Age Interval', 'Total Products'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Age Interval', y='Total Products', title='Product Sales by Age Interval', color='Age Interval')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["age_ranking"]

def age_ranking_2022(con):
    # Execute SQL query
    try:
        cursor = con.cursor()
        cursor.execute('''
            SELECT
                CASE
                    WHEN age < 18 THEN '0-17'
                    WHEN age >= 18 AND age < 25 THEN '18-24'
                    WHEN age >= 25 AND age < 35 THEN '25-34'
                    WHEN age >= 35 AND age < 45 THEN '35-44'
                    WHEN age >= 45 AND age < 55 THEN '45-54'
                    ELSE '55+'
                END AS age_interval,
                COUNT(*) AS total_products
            FROM sales s
            JOIN customers c ON s.id_customer = c.id_customer
            WHERE YEAR(s.date_purchase) = 2022
            GROUP BY age_interval
            ORDER BY total_products DESC;
        ''')
        rows = cursor.fetchall()
    except Exception as e:
        # Handle any exceptions that occur during query execution
        st.error(f"Error executing SQL query: {e}")
        rows = []

    if rows:
        df = pd.DataFrame(rows, columns=['Age Interval', 'Total Products'])

        # Create a bar chart using Plotly
        fig = px.bar(df, x='Age Interval', y='Total Products', title='Product Sales by Age Interval', color='Age Interval')

        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("No sales data available.")

# Export the total_revenue function
__all__ = ["age_ranking_2022"]