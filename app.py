import streamlit as st
import pandas as pd

st.set_page_config(page_title="Talking Rabbitt", page_icon="🐰", layout="centered")

st.title("Talking Rabbitt")
st.markdown("**Ask questions about your sales data in natural language.**")

st.markdown("---")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Data Preview")
    st.dataframe(df)

    st.markdown("---")

    st.subheader("💬 Ask a question")

    st.caption("Try asking:")
    st.markdown("""
- Which product has the **highest revenue**?
- Which product sold the **most units**?
- Show **revenue by region**
- Show **revenue by category**
""")

    question = st.text_input("Type your question here")

    if question:
        question = question.lower()

        # Highest revenue product
        if "highest revenue" in question or "top revenue" in question:
            row = df.loc[df["Revenue"].idxmax()]
            st.success(f"Highest revenue product: **{row['Product']}** (${row['Revenue']})")

            st.subheader("Revenue by Product")
            st.bar_chart(df.set_index("Product")["Revenue"])

        # Most units sold
        elif "most units" in question or "most sold" in question:
            row = df.loc[df["Units_Sold"].idxmax()]
            st.success(f"Most units sold: **{row['Product']}** ({row['Units_Sold']} units)")

            st.subheader("Units Sold by Product")
            st.bar_chart(df.set_index("Product")["Units_Sold"])

        # Revenue by region
        elif "region" in question:
            region_sales = df.groupby("Region")["Revenue"].sum()
            st.subheader("Revenue by Region")
            st.bar_chart(region_sales)

        # Revenue by category
        elif "category" in question:
            category_sales = df.groupby("Category")["Revenue"].sum()
            st.subheader("Revenue by Category")
            st.bar_chart(category_sales)

        else:
            st.info("Showing overall revenue by product.")
            st.bar_chart(df.set_index("Product")["Revenue"])