import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Nassau Candy Distributor",
    page_icon="🚚",
    layout="wide"
)

st.title("🚚 Factory-to-Customer Shipping Route Efficiency Analysis")
st.markdown("### Nassau Candy Distributor")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv("Nassau Candy Distributor.csv")

    df['Order Date'] = pd.to_datetime(
        df['Order Date'],
        dayfirst=True,
        errors='coerce'
    )

    df['Ship Date'] = pd.to_datetime(
        df['Ship Date'],
        dayfirst=True,
        errors='coerce'
    )

    df['Lead Time'] = (
        df['Ship Date'] -
        df['Order Date']
    ).dt.days

    factory_map = {
        "Wonka Bar - Nutty Crunch Surprise":"Lot's O' Nuts",
        "Wonka Bar - Fudge Mallows":"Lot's O' Nuts",
        "Wonka Bar -Scrumdiddlyumptious":"Lot's O' Nuts",
        "Wonka Bar - Milk Chocolate":"Wicked Choccy's",
        "Wonka Bar - Triple Dazzle Caramel":"Wicked Choccy's",
        "Laffy Taffy":"Sugar Shack",
        "SweeTARTS":"Sugar Shack",
        "Nerds":"Sugar Shack",
        "Fun Dip":"Sugar Shack",
        "Fizzy Lifting Drinks":"Sugar Shack",
        "Everlasting Gobstopper":"Secret Factory",
        "Hair Toffee":"The Other Factory",
        "Lickable Wallpaper":"Secret Factory",
        "Wonka Gum":"Secret Factory",
        "Kazookles":"The Other Factory"
    }

    df['Factory'] = df['Product Name'].map(factory_map)

    df['Route_State'] = (
        df['Factory']
        + " → "
        + df['State/Province']
    )

    return df

df = load_data()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Filters")

start_date = st.sidebar.date_input(
    "Start Date",
    df['Order Date'].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df['Order Date'].max()
)

region_filter = st.sidebar.multiselect(
    "Region",
    options=sorted(df['Region'].unique()),
    default=sorted(df['Region'].unique())
)

state_filter = st.sidebar.multiselect(
    "State",
    options=sorted(df['State/Province'].unique()),
    default=sorted(df['State/Province'].unique())
)

ship_filter = st.sidebar.multiselect(
    "Ship Mode",
    options=sorted(df['Ship Mode'].unique()),
    default=sorted(df['Ship Mode'].unique())
)

lead_threshold = st.sidebar.slider(
    "Lead Time Threshold",
    int(df['Lead Time'].min()),
    int(df['Lead Time'].max()),
    int(df['Lead Time'].mean())
)

# --------------------------------------------------
# FILTER DATA
# --------------------------------------------------

filtered_df = df[
    (df['Order Date'] >= pd.Timestamp(start_date))
    &
    (df['Order Date'] <= pd.Timestamp(end_date))
    &
    (df['Region'].isin(region_filter))
    &
    (df['State/Province'].isin(state_filter))
    &
    (df['Ship Mode'].isin(ship_filter))
]

filtered_df['Delayed'] = (
    filtered_df['Lead Time']
    > lead_threshold
)

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

st.header("📊 Executive Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Orders",
        filtered_df['Order ID'].nunique()
    )

with col2:
    st.metric(
        "Total Sales",
        f"${filtered_df['Sales'].sum():,.2f}"
    )

with col3:
    st.metric(
        "Avg Lead Time",
        round(filtered_df['Lead Time'].mean(),2)
    )

with col4:
    st.metric(
        "Delay %",
        round(
            filtered_df['Delayed'].mean()*100,
            2
        )
    )

# --------------------------------------------------
# ROUTE EFFICIENCY
# --------------------------------------------------

st.header("🚛 Route Efficiency Overview")

route_summary = filtered_df.groupby(
    'Route_State'
).agg(
    Shipments=('Order ID','count'),
    Avg_Lead_Time=('Lead Time','mean'),
    Sales=('Sales','sum')
).reset_index()

top_routes = route_summary.sort_values(
    'Avg_Lead_Time'
).head(10)

bottom_routes = route_summary.sort_values(
    'Avg_Lead_Time',
    ascending=False
).head(10)

c1, c2 = st.columns(2)

with c1:

    fig = px.bar(
        top_routes,
        x='Avg_Lead_Time',
        y='Route_State',
        title='Top 10 Efficient Routes'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with c2:

    fig = px.bar(
        bottom_routes,
        x='Avg_Lead_Time',
        y='Route_State',
        title='Bottom 10 Routes'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# REGION ANALYSIS
# --------------------------------------------------

st.header("🌎 Regional Performance")

region_summary = filtered_df.groupby(
    'Region'
).agg(
    Orders=('Order ID','count'),
    Avg_Lead_Time=('Lead Time','mean'),
    Sales=('Sales','sum')
).reset_index()

fig = px.bar(
    region_summary,
    x='Region',
    y='Avg_Lead_Time',
    color='Region',
    title='Average Lead Time by Region'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# STATE BOTTLENECK ANALYSIS
# --------------------------------------------------

st.header("📍 Geographic Bottlenecks")

state_summary = filtered_df.groupby(
    'State/Province'
).agg(
    Orders=('Order ID','count'),
    Avg_Lead_Time=('Lead Time','mean')
).reset_index()

state_summary = state_summary.sort_values(
    'Avg_Lead_Time',
    ascending=False
)

fig = px.bar(
    state_summary.head(15),
    x='State/Province',
    y='Avg_Lead_Time',
    title='Top Bottleneck States'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# SHIP MODE ANALYSIS
# --------------------------------------------------

st.header("🚢 Ship Mode Comparison")

ship_summary = filtered_df.groupby(
    'Ship Mode'
).agg(
    Orders=('Order ID','count'),
    Avg_Lead_Time=('Lead Time','mean'),
    Sales=('Sales','sum'),
    Profit=('Gross Profit','sum')
).reset_index()

fig = px.bar(
    ship_summary,
    x='Ship Mode',
    y='Avg_Lead_Time',
    color='Ship Mode',
    title='Lead Time by Ship Mode'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(ship_summary)

# --------------------------------------------------
# FACTORY PERFORMANCE
# --------------------------------------------------

st.header("🏭 Factory Performance")

factory_summary = filtered_df.groupby(
    'Factory'
).agg(
    Orders=('Order ID','count'),
    Avg_Lead_Time=('Lead Time','mean'),
    Sales=('Sales','sum'),
    Profit=('Gross Profit','sum')
).reset_index()

fig = px.bar(
    factory_summary,
    x='Factory',
    y='Avg_Lead_Time',
    color='Factory',
    title='Factory Performance'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# ROUTE DRILL DOWN
# --------------------------------------------------

st.header("🔍 Route Drill Down")

route_choice = st.selectbox(
    "Select Route",
    sorted(filtered_df['Route_State'].unique())
)

route_data = filtered_df[
    filtered_df['Route_State']
    == route_choice
]

st.subheader(route_choice)

st.write(
    "Orders:",
    route_data['Order ID'].nunique()
)

st.write(
    "Average Lead Time:",
    round(route_data['Lead Time'].mean(),2)
)

st.write(
    "Sales:",
    round(route_data['Sales'].sum(),2)
)

timeline = route_data.sort_values(
    'Order Date'
)

fig = px.line(
    timeline,
    x='Order Date',
    y='Lead Time',
    title='Shipment Timeline'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(route_data)

# --------------------------------------------------
# RAW DATA
# --------------------------------------------------

st.header("📄 Raw Data")

st.dataframe(filtered_df)