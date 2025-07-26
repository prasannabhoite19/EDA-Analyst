# EDA_Analyst

## Overview

**EDA_Analyst** is a project focused on Exploratory Data Analysis (EDA) to help analysts and data scientists quickly understand and visualize datasets. The project includes scripts and tools for data cleaning, visualization, and statistical analysis.

## Features

- Data loading and preprocessing
- Visualization of distributions, correlations.
- Summary statistics and insights

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/EDA_Analyst.git
    cd EDA_Analyst
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

Run the main script with your dataset:
```sh
python main.py --input data/your_dataset.csv
```

Run the streamlit app:
```sh
streamlit run app.py
```

## Project Structure

```
EDA_Analyst/
├── app.py                  streamlit app
├── agent/
│   ├── tools.py            preprocessing agent 
│   ├── visualizer.py       visulazation agent
│   └── rag.py              answering agent about eda report
├── data/
│   └── sample.csv          dataset
│   └── eda_report.txt      eda report
├── images/                 saved plots
├── main.py                 main interface
└── .env                    openai api key

```

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.
