from agent.tools import DataLoaderTool
from agent.visualizer import plot_corr_matrix, plot_histogram, correlation_heatmap, bar_chart
from agent.rag import build_rag_chain
import os 
from dotenv import load_dotenv

load_dotenv()

def main():
    file_path = "data/sample.csv"

    loader = DataLoaderTool()
    loader.load_csv(file_path)

    # Step 2: Run EDA
    print("\n=== EDA Report ===")
    eda_report = loader.run_eda()
    print(eda_report)
    
    with open("data/eda_report.txt", "w", encoding="utf-8") as f:
        f.write(eda_report)

    # Step 3: Visualizations
    df = loader.get_dataframe()
    numeric_df = df.select_dtypes(include='number')
    categoric_df = df.select_dtypes(include='object')

    print("\n=== Generating Visuals ===")

    print(f"\nCorrelation matrix:\n{plot_corr_matrix(numeric_df)}")

    for col in numeric_df.columns:
        print(f"\nHistogram saved as: {plot_histogram(numeric_df, col)}")

    print(f"\nHeatmap saved as: {correlation_heatmap(numeric_df)}")

    for col in categoric_df.columns:
        print(f"\nBar chart saved as: {bar_chart(categoric_df, col)}")

    # Step 4: RAG interaction
    rag_chain = build_rag_chain("data/eda_report.txt")
    print("Ask questions about your eda report (type 'exit' to quit):")

    while True:
        q = input("You: ")
        if q.lower() == "exit":
            break
        response = rag_chain.invoke({"query": q})
        print("Answer:", response["result"])

if __name__ == "__main__":
    main()
