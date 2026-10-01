# 📊 AI Business Analytics Dashboard

An interactive business intelligence dashboard built with **Python, Streamlit, Pandas, Plotly, and OpenAI**. It transforms sales data into KPIs, interactive visualizations, filtered analysis, and AI-powered business insights.

## 🌐 Live Demo

**[Open the Live Dashboard](https://ai-business-analytics-dashboard-khxsb8bjplbuvgwdirkhsn.streamlit.app/)**

## 🚀 Key Features

- Upload CSV or Excel business datasets
- Interactive filters for region, category, and customer type
- Executive KPI tracking
- Revenue and profitability analysis
- Product, regional, category, and customer performance analysis
- Interactive Plotly charts
- AI Business Analyst for natural-language data questions
- AI-generated Executive Business Brief
- Download filtered data as CSV
- Built-in data validation and cleaning

## 📈 Dashboard Analytics

The dashboard tracks:

- **Total Revenue**
- **Total Profit**
- **Profit Margin**
- **Transaction Count**
- **Average Transaction Value**
- Monthly Revenue Trends
- Product Performance
- Regional Performance
- Category Profitability
- Customer Performance

## 🤖 AI Business Analyst

The dashboard integrates the **OpenAI API** to analyze the currently filtered dataset.

Users can ask questions such as:

> Which product generated the most revenue?

> Which region performed best?

> Which products have the highest profit margins?

The **Executive AI Brief** also generates a concise summary of important trends, opportunities, and business observations based on the dashboard data.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web dashboard |
| Pandas | Data cleaning and analysis |
| Plotly | Interactive visualizations |
| OpenAI API | AI-powered business insights |
| OpenPyXL | Excel file support |

## 📂 Demo Dataset

The repository includes a **synthetic sales dataset with 1,000 transactions** across multiple products, categories, regions, and customer types.

The dataset was generated programmatically for portfolio demonstration and contains **no real customer or company information**.

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/bibirhussainy/AI-Business-Analytics-Dashboard.git
cd AI-Business-Analytics-Dashboard
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create:

```text
.streamlit/secrets.toml
```

Add your OpenAI API key:

```toml
OPENAI_API_KEY = "your-api-key"
```

Run the application:

```bash
streamlit run app.py
```

## 🔐 Security

API credentials are managed using **Streamlit Secrets** and excluded from version control through `.gitignore`.

## 💼 Skills Demonstrated

**Data Analysis · Business Intelligence · Python · Pandas · Data Visualization · KPI Analysis · Streamlit · Plotly · Generative AI · API Integration**

## 👤 Author

**Bibi Ruqaya Hussainy**
