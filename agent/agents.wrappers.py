from langchain_core.tools import tool
from agent.tools import DataLoaderTool
from agent.visualizer import plot_histogram, plot_corr_matrix, bar_chart

loader = DataLoaderTool()
loader.load_csv("data/sample.csv")
loader.run_eda()

df = loader.get_dataframe()