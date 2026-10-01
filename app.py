import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from openai import OpenAI


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Business Intelligence Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROFESSIONAL CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main application */
    .stApp {
        background-color: #f5f7fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827 0%, #1f2937 100%);
        border-right: 1px solid #253247;
    }

    section[data-testid="stSidebar"] * {
        color: #f9fafb;
    }

    section[data-testid="stSidebar"] .stMultiSelect span {
        color: #111827;
    }

    /* Header */
    .dashboard-header {
        background: linear-gradient(120deg, #111827, #1e3a5f);
        padding: 28px 32px;
        border-radius: 16px;
        margin-bottom: 24px;
        box-shadow: 0 8px 25px rgba(15, 23, 42, 0.12);
    }

    .header-label {
        color: #93c5fd;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 8px;
    }

    .dashboard-title {
        color: white;
        font-size: 34px;
        font-weight: 750;
        margin: 0;
    }

    .dashboard-subtitle {
        color: #cbd5e1;
        font-size: 15px;
        margin-top: 8px;
        margin-bottom: 0;
    }

    /* Section label */
    .section-label {
        font-size: 12px;
        font-weight: 700;
        color: #64748b;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-top: 8px;
        margin-bottom: 4px;
    }

    /* KPI cards */
    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #e5e7eb;
        padding: 18px 18px;
        border-radius: 14px;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.05);
        min-height: 120px;
    }

    div[data-testid="stMetricLabel"] {
        font-size: 13px;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        font-size: 27px;
        font-weight: 700;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 9px;
        font-weight: 600;
        min-height: 42px;
    }

    .stDownloadButton > button {
        border-radius: 9px;
        font-weight: 600;
    }

    /* File uploader */
    div[data-testid="stFileUploader"] {
        background-color: white;
        border-radius: 12px;
        padding: 4px;
    }

    /* Dataframe */
    div[data-testid="stDataFrame"] {
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        overflow: hidden;
    }

    /* AI container styling */
    .ai-header {
        background: linear-gradient(120deg, #eef2ff, #f8fafc);
        border: 1px solid #dbeafe;
        padding: 20px 24px;
        border-radius: 14px;
        margin-top: 8px;
        margin-bottom: 16px;
    }

    .ai-title {
        color: #172554;
        font-size: 21px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .ai-description {
        color: #64748b;
        font-size: 14px;
        margin: 0;
    }

    /* Reduce excessive gaps */
    hr {
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="dashboard-header">
        <div class="header-label">BUSINESS INTELLIGENCE</div>
        <div class="dashboard-title">Executive Analytics Dashboard</div>
        <p class="dashboard-subtitle">
            Sales performance, profitability, customer insights and
            AI-powered business intelligence.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FILE UPLOAD
# ============================================================

st.markdown(
    '<div class="section-label">DATA SOURCE</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Upload business dataset",
    type=["csv", "xlsx"],
    label_visibility="collapsed"
)


if uploaded_file is not None:

    # ========================================================
    # LOAD DATA
    # ========================================================

    try:

        if uploaded_file.name.lower().endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        required_columns = [
            "Date",
            "Product",
            "Category",
            "Region",
            "Customer Type",
            "Quantity",
            "Sales",
            "Cost",
            "Profit"
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:
            st.error(
                "Missing required columns: "
                + ", ".join(missing_columns)
            )
            st.stop()

        df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce"
        )

        numeric_columns = [
            "Quantity",
            "Sales",
            "Cost",
            "Profit"
        ]

        for column in numeric_columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

        df = df.dropna(
            subset=required_columns
        )

    except Exception as e:
        st.error(f"Unable to process the dataset: {e}")
        st.stop()


    # ========================================================
    # SIDEBAR
    # ========================================================

    st.sidebar.markdown("## ◈ Analytics Control")

    st.sidebar.caption(
        "Use the filters below to explore business performance."
    )

    st.sidebar.divider()

    selected_regions = st.sidebar.multiselect(
        "Region",
        options=sorted(df["Region"].unique()),
        default=sorted(df["Region"].unique())
    )

    selected_categories = st.sidebar.multiselect(
        "Category",
        options=sorted(df["Category"].unique()),
        default=sorted(df["Category"].unique())
    )

    selected_customers = st.sidebar.multiselect(
        "Customer Type",
        options=sorted(df["Customer Type"].unique()),
        default=sorted(df["Customer Type"].unique())
    )

    st.sidebar.divider()

    st.sidebar.caption(
        f"Dataset: {len(df):,} transactions"
    )


    # ========================================================
    # FILTER DATA
    # ========================================================

    filtered_df = df[
        (df["Region"].isin(selected_regions))
        & (df["Category"].isin(selected_categories))
        & (df["Customer Type"].isin(selected_customers))
    ].copy()

    if filtered_df.empty:
        st.warning(
            "No records match the selected filters. "
            "Please change the filters."
        )
        st.stop()


    # ========================================================
    # CALCULATIONS
    # ========================================================

    total_sales = filtered_df["Sales"].sum()
    total_profit = filtered_df["Profit"].sum()
    total_transactions = len(filtered_df)
    total_quantity = filtered_df["Quantity"].sum()

    profit_margin = (
        (total_profit / total_sales) * 100
        if total_sales
        else 0
    )

    average_transaction = (
        total_sales / total_transactions
        if total_transactions
        else 0
    )


    # ========================================================
    # KPI CARDS
    # ========================================================

    st.markdown(
        '<div class="section-label">EXECUTIVE OVERVIEW</div>',
        unsafe_allow_html=True
    )

    k1, k2, k3, k4, k5 = st.columns(5)

    k1.metric(
        "Total Revenue",
        f"€{total_sales / 1_000_000:.2f}M"
        if total_sales >= 1_000_000
        else f"€{total_sales:,.0f}"
    )

    k2.metric(
        "Total Profit",
        f"€{total_profit:,.0f}"
    )

    k3.metric(
        "Profit Margin",
        f"{profit_margin:.1f}%"
    )

    k4.metric(
        "Transactions",
        f"{total_transactions:,}"
    )

    k5.metric(
        "Avg. Transaction",
        f"€{average_transaction:,.0f}"
    )


    # ========================================================
    # AGGREGATIONS
    # ========================================================

    monthly_sales = (
        filtered_df
        .assign(
            Month=filtered_df["Date"].dt.to_period("M")
        )
        .groupby("Month", as_index=False)["Sales"]
        .sum()
    )

    monthly_sales["Date"] = (
        monthly_sales["Month"]
        .dt
        .to_timestamp()
    )


    product_performance = (
        filtered_df
        .groupby("Product")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Units_Sold=("Quantity", "sum")
        )
        .reset_index()
    )

    product_performance["Profit_Margin_%"] = (
        (
            product_performance["Profit"]
            / product_performance["Sales"]
        )
        * 100
    ).round(1)

    product_performance = (
        product_performance
        .sort_values(
            "Sales",
            ascending=False
        )
    )


    region_sales = (
        filtered_df
        .groupby(
            "Region",
            as_index=False
        )["Sales"]
        .sum()
        .sort_values(
            "Sales",
            ascending=False
        )
    )


    category_profit = (
        filtered_df
        .groupby(
            "Category",
            as_index=False
        )["Profit"]
        .sum()
        .sort_values(
            "Profit",
            ascending=False
        )
    )


    customer_performance = (
        filtered_df
        .groupby("Customer Type")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Transactions=("Sales", "size"),
            Units_Sold=("Quantity", "sum")
        )
        .reset_index()
        .sort_values(
            "Sales",
            ascending=False
        )
    )


    # ========================================================
    # PROFESSIONAL CHART SETTINGS
    # ========================================================

    chart_config = {
        "displayModeBar": False,
        "responsive": True
    }

    plotly_template = "plotly_white"


    # ========================================================
    # SALES TREND + REGION
    # ========================================================

    st.markdown(
        '<div class="section-label">PERFORMANCE ANALYSIS</div>',
        unsafe_allow_html=True
    )

    left_chart, right_chart = st.columns(
        [1.7, 1]
    )


    with left_chart:

        st.markdown("### Revenue Trend")

        fig_monthly = px.line(
            monthly_sales,
            x="Date",
            y="Sales",
            markers=True,
            template=plotly_template
        )

        fig_monthly.update_traces(
            line=dict(width=3),
            marker=dict(size=7)
        )

        fig_monthly.update_layout(
            height=390,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),
            xaxis_title="",
            yaxis_title="Revenue (€)",
            hovermode="x unified"
        )

        fig_monthly.update_xaxes(
            tickformat="%b %Y",
            showgrid=False,
            range=[
                monthly_sales["Date"].min(),
                monthly_sales["Date"].max()
            ]
        )

        fig_monthly.update_yaxes(
            gridcolor="#eef2f7"
        )

        st.plotly_chart(
            fig_monthly,
            config=chart_config
        )


    with right_chart:

        st.markdown("### Revenue by Region")

        fig_region = go.Figure(
            data=[
                go.Pie(
                    labels=region_sales["Region"],
                    values=region_sales["Sales"],
                    hole=0.62,
                    textinfo="percent",
                    hovertemplate=(
                        "<b>%{label}</b><br>"
                        "Revenue: €%{value:,.0f}<br>"
                        "%{percent}"
                        "<extra></extra>"
                    )
                )
            ]
        )

        fig_region.update_layout(
            template=plotly_template,
            height=390,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),
            legend=dict(
                orientation="h",
                y=-0.1
            )
        )

        st.plotly_chart(
            fig_region,
            config=chart_config
        )


    # ========================================================
    # PRODUCT + CATEGORY CHARTS
    # ========================================================

    product_col, category_col = st.columns(2)


    with product_col:

        st.markdown("### Revenue by Product")

        fig_product = px.bar(
            product_performance,
            x="Sales",
            y="Product",
            orientation="h",
            template=plotly_template
        )

        fig_product.update_layout(
            height=420,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),
            xaxis_title="Revenue (€)",
            yaxis_title="",
            showlegend=False
        )

        fig_product.update_yaxes(
            categoryorder="total ascending"
        )

        fig_product.update_xaxes(
            gridcolor="#eef2f7"
        )

        st.plotly_chart(
            fig_product,
            config=chart_config
        )


    with category_col:

        st.markdown("### Profit by Category")

        fig_category = px.bar(
            category_profit,
            x="Category",
            y="Profit",
            template=plotly_template
        )

        fig_category.update_layout(
            height=420,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),
            xaxis_title="",
            yaxis_title="Profit (€)",
            showlegend=False
        )

        fig_category.update_xaxes(
            showgrid=False
        )

        fig_category.update_yaxes(
            gridcolor="#eef2f7"
        )

        st.plotly_chart(
            fig_category,
            config=chart_config
        )


    # ========================================================
    # PRODUCT TABLE
    # ========================================================

    st.markdown(
        '<div class="section-label">PRODUCT INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Product Performance")

    display_products = (
        product_performance.copy()
    )

    display_products["Sales"] = (
        display_products["Sales"]
        .map(lambda x: f"€{x:,.0f}")
    )

    display_products["Profit"] = (
        display_products["Profit"]
        .map(lambda x: f"€{x:,.0f}")
    )

    display_products["Units_Sold"] = (
        display_products["Units_Sold"]
        .map(lambda x: f"{x:,.0f}")
    )

    display_products["Profit_Margin_%"] = (
        display_products["Profit_Margin_%"]
        .map(lambda x: f"{x:.1f}%")
    )

    display_products.columns = [
        "Product",
        "Revenue",
        "Profit",
        "Units Sold",
        "Profit Margin"
    ]

    st.dataframe(
        display_products,
        hide_index=True
    )


    # ========================================================
    # AI CONTEXT
    # ========================================================

    analytics_context = f"""
FILTERED BUSINESS ANALYTICS DATA

OVERALL KPIs
Total Revenue: €{total_sales:,.2f}
Total Profit: €{total_profit:,.2f}
Transactions: {total_transactions}
Units Sold: {total_quantity:,.0f}
Profit Margin: {profit_margin:.2f}%
Average Transaction Value: €{average_transaction:,.2f}

MONTHLY REVENUE
{monthly_sales[['Date', 'Sales']].to_string(index=False)}

PRODUCT PERFORMANCE
{product_performance.to_string(index=False)}

REGIONAL REVENUE
{region_sales.to_string(index=False)}

CATEGORY PROFIT
{category_profit.to_string(index=False)}

CUSTOMER PERFORMANCE
{customer_performance.to_string(index=False)}
"""


    # ========================================================
    # AI BUSINESS ANALYST
    # ========================================================

    st.divider()

    st.markdown(
        """
        <div class="ai-header">
            <div class="ai-title">
                ✦ AI Business Analyst
            </div>
            <p class="ai-description">
                Ask questions about the filtered dataset and
                receive evidence-based business insights.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    question = st.text_input(
        "Business question",
        placeholder=(
            "Example: Which product generated the "
            "highest profit and what was its margin?"
        ),
        label_visibility="collapsed"
    )


    if st.button(
        "Analyze Data",
        type="primary"
    ):

        if not question.strip():

            st.warning(
                "Enter a business question first."
            )

        else:

            try:

                client = OpenAI(
                    api_key=st.secrets[
                        "OPENAI_API_KEY"
                    ]
                )

                with st.spinner(
                    "Analyzing current business data..."
                ):

                    response = client.responses.create(
                        model="gpt-5.6-luna",
                        instructions=(
                            "You are a professional business "
                            "intelligence analyst. "
                            "Use only the supplied filtered data. "
                            "Do not invent facts, explanations, "
                            "causes, or numbers. "
                            "Before answering, silently verify all "
                            "comparisons, rankings, totals, and "
                            "percentages against the supplied tables. "
                            "When saying highest, lowest, first, "
                            "second, or similar, sort and compare "
                            "the relevant values first. "
                            "Never make a ranking statement that "
                            "contradicts the numerical values. "
                            "If the data cannot answer a question, "
                            "state that clearly. "
                            "Keep the answer concise, professional, "
                            "and suitable for business management."
                        ),
                        input=(
                            analytics_context
                            + "\n\nBUSINESS QUESTION:\n"
                            + question
                        )
                    )

                st.success(
                    "Analysis complete"
                )

                st.markdown(
                    response.output_text
                )

            except Exception as e:

                st.error(
                    "AI analysis could not be completed. "
                    f"Error: {e}"
                )


    # ========================================================
    # EXECUTIVE SUMMARY
    # ========================================================

    st.markdown(
        """
        <div class="ai-header">
            <div class="ai-title">
                Executive AI Brief
            </div>
            <p class="ai-description">
                Generate a management-level summary from the
                currently selected dashboard data.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


    if st.button(
        "Generate Executive Brief"
    ):

        try:

            client = OpenAI(
                api_key=st.secrets[
                    "OPENAI_API_KEY"
                ]
            )

            with st.spinner(
                "Preparing executive brief..."
            ):

                summary_response = (
                    client.responses.create(
                        model="gpt-5.6-luna",
                        instructions=(
                            "You are a senior business intelligence "
                            "analyst preparing an executive brief. "
                            "Use only the supplied business data. "
                            "Do not invent causes or unsupported facts. "
                            "Before writing, silently verify every "
                            "ranking, comparison, total, percentage, "
                            "minimum, and maximum against the supplied "
                            "tables. "
                            "Pay special attention to product unit "
                            "rankings and profit margins. "
                            "Do not write a ranking and then correct "
                            "yourself later. "
                            "Write a polished executive summary covering "
                            "overall performance, revenue trends, product "
                            "performance, profitability, regional "
                            "performance, and customer performance. "
                            "Finish with exactly 3 concise business "
                            "recommendations. "
                            "Recommendations must be supported by the "
                            "provided data and should not claim causal "
                            "relationships that the data does not show."
                        ),
                        input=analytics_context
                    )
                )

            st.success(
                "Executive brief generated"
            )

            st.markdown(
                summary_response.output_text
            )

        except Exception as e:

            st.error(
                "Executive brief could not be generated. "
                f"Error: {e}"
            )


    # ========================================================
    # EXPORT + RAW DATA
    # ========================================================

    st.divider()

    export_col, info_col = st.columns(
        [1, 2]
    )

    with export_col:

        st.markdown("### Export")

        csv_data = (
            filtered_df
            .to_csv(index=False)
            .encode("utf-8")
        )

        st.download_button(
            "Download Filtered Dataset",
            data=csv_data,
            file_name="business_analytics_export.csv",
            mime="text/csv"
        )


    with info_col:

        st.markdown("### Current Selection")

        st.write(
            f"**{len(filtered_df):,}** transactions · "
            f"**{filtered_df['Region'].nunique()}** regions · "
            f"**{filtered_df['Product'].nunique()}** products · "
            f"**{filtered_df['Category'].nunique()}** categories"
        )


    with st.expander(
        "View underlying filtered data"
    ):

        st.dataframe(
            filtered_df,
            hide_index=True
        )


# ============================================================
# EMPTY STATE
# ============================================================

else:

    st.markdown("### Start your analysis")

    st.write(
        "Upload `sales_data.csv` to launch the interactive "
        "business intelligence dashboard."
    )

    st.info(
        "The dashboard supports CSV and Excel datasets."
    )