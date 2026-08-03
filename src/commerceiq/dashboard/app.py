import streamlit as st
import tempfile
from pathlib import Path
from commerceiq.app.commerceiq_app import CommerceIQApp

st.set_page_config(
    page_title="CommerceIQ",
    page_icon="📊",
    layout="wide",
)

st.title("📊 CommerceIQ")
st.caption("Business Intelligence Platform")

uploaded_file = st.file_uploader(
    "Upload an orders CSV",
    type="csv",
)

if uploaded_file is None:
    st.info("Upload a CSV file to begin.")
    st.stop()
with tempfile.NamedTemporaryFile(
    delete=False,
    suffix=".csv"
) as tmp:

    tmp.write(uploaded_file.getvalue())

    csv_path = Path(tmp.name)
with st.spinner("Analyzing dataset..."):

    app = CommerceIQApp()

    result = app.run(csv_path)
col1, col2, col3, col4 = st.columns(4)
col1.metric(
    "Revenue",
    f"{result.kpis.total_revenue:,.2f} TND",
)

col2.metric(
    "Orders",
    f"{result.kpis.total_orders:,}",
)

col3.metric(
    "Customers",
    f"{result.kpis.unique_customers:,}",
)

col4.metric(
    "Average Basket",
    f"{result.kpis.average_order_value:,.2f} TND",
)
st.divider()

st.subheader("Revenue by Channel")

st.dataframe(
    result.analysis.revenue_by_channel,
    use_container_width=True,
)