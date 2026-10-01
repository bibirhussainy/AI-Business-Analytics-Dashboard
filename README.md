# 📊 AI Business Analytics Dashboard

An interactive business intelligence dashboard that combines data analytics, visualization, and generative AI to transform business sales data into actionable insights.

## 🚀 Features

- Upload and analyze CSV or Excel business datasets
- Interactive filtering by region, category, and customer type
- Executive KPI tracking for revenue, profit, margin, transactions, and average transaction value
- Revenue trend analysis
- Product, regional, category, and customer performance analysis
- Interactive Plotly visualizations
- AI Business Analyst for natural-language questions about the data
- AI-generated Executive Business Brief
- Download filtered datasets as CSV
- Built-in data validation and cleaning

## 🤖 AI Capabilities

The dashboard integrates the OpenAI API to provide grounded business analysis based on the currently filtered dataset.

Users can ask questions such as:

- Which product generated the most revenue?
- Which region performed best?
- Which products have the highest profit margins?
- What are the key trends in the data?

The Executive AI Brief summarizes important performance trends, opportunities, and business observations from the dashboard data.

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**
- **OpenAI API**
- **OpenPyXL**

## 📈 Analytics Included

The dashboard calculates and visualizes:

- Total Revenue
- Total Profit
- Profit Margin
- Transaction Count
- Average Transaction Value
- Monthly Revenue Trends
- Product Performance
- Regional Performance
- Category Profitability
- Customer Performance

## 📂 Demo Dataset

The repository includes a synthetic sales dataset containing 1,000 transactions across multiple products, categories, regions, and customer types.

The dataset was generated programmatically for portfolio demonstration purposes and does not contain real customer or company information.

## ▶️ Run Locally

Clone the repository and install the dependencies:

```bash
git clone https://github.com/bibirhussainy/AI-Business-Analytics-Dashboard.git
cd AI-Business-Analytics-Dashboard
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml` and add your OpenAI API key:

```toml
OPENAI_API_KEY = "your-api-key"
```

Then run:

```bash
streamlit run app.py
```

## 🔐 Security

API credentials are stored using Streamlit Secrets and are excluded from version control through `.gitignore`.

## 💼 Portfolio Purpose

This project demonstrates practical skills relevant to Data Analyst, Business Intelligence, Data & AI Analyst, and AI-focused roles, including data preparation, KPI analysis, interactive visualization, dashboard development, API integration, and generative AI.

## 👤 Author

**Bibi Ruqaya Hussainy**

## 🌐 Live Demo

Try the deployed dashboard here:

https://ai-business-analytics-dashboard-khxsb8bjplbuvgwdirkhsn.streamlit.app/
