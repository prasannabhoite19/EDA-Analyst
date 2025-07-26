import streamlit as st
import pandas as pd
import os
from agent.tools import DataLoaderTool
from agent.visualizer import plot_corr_matrix, plot_histogram, correlation_heatmap, bar_chart
from agent.rag import build_rag_chain
from PIL import Image
import tempfile
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(page_title="AI Data Analyst", layout="wide")

st.title("🧠 AI-Powered Data Analyst")

# Step 1: Upload CSV file
uploaded_file = st.file_uploader("📤 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Save to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    loader = DataLoaderTool()
    loader.load_csv(file_path)

    st.subheader("📊 Exploratory Data Analysis")
    eda_report = loader.run_eda()
    st.text(eda_report)

    with open("data/eda_report.txt", "w") as f:
        f.write(eda_report)

    df = loader.get_dataframe()

    numeric_df = df.select_dtypes(include='number')
    categoric_df = df.select_dtypes(include='object')

    st.subheader("Correlation Matrix")
    st.dataframe(plot_corr_matrix(numeric_df), use_container_width=True)

    st.subheader("📈 Histograms (Numerical Columns)")
    for col in numeric_df.columns:
        hist_path = plot_histogram(numeric_df, col)
        st.image(Image.open(hist_path), caption=f"Histogram of {col}", use_container_width=True)

    st.subheader("🧯 Bar Charts (Categorical Columns)")
    for col in categoric_df.columns:
        bar_path = bar_chart(categoric_df, col)
        st.image(Image.open(bar_path), caption=f"Bar chart of {col}", use_container_width=True)

    st.subheader("🧊 Correlation Heatmap")
    heatmap_path = correlation_heatmap(numeric_df)
    st.image(Image.open(heatmap_path), caption="Correlation Heatmap", use_container_width=True)

    st.subheader("🤖 Ask Questions About Your EDA Report")

    rag_chain = build_rag_chain('data/eda_report.txt')
    user_question = st.text_input("Type your question:")

    if user_question:
        response = rag_chain.invoke(user_question)
        st.success(response['result'])
