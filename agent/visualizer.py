import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('images', exist_ok=True)

def plot_corr_matrix(numeric_df):
    return numeric_df.corr()

def plot_histogram(numeric_df, column):
    plt.figure(figsize=(8, 4))
    numeric_df[column].hist(bins=30)
    plt.title(f"Histogram of {column}")
    filename = f"hist_{column}.png"
    filepath = os.path.join('images', filename)
    plt.savefig(filepath)
    plt.close()
    return filepath

def correlation_heatmap(numeric_df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    filename = 'correlation_heatmap.png'
    filepath = os.path.join("images", filename)
    plt.savefig(filepath)
    plt.close()
    return filepath

def bar_chart(categoric_df, column):
    plt.figure(figsize=(8, 4))
    categoric_df[column].value_counts().plot(kind='bar')
    plt.title(f"Bar Chart of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    filename = f"bar_chart_{column}.png"
    filepath = os.path.join("images", filename)
    plt.savefig(filepath)
    plt.close()
    return filepath
