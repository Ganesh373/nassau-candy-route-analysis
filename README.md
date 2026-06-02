# 🚚 Factory-to-Customer Shipping Route Efficiency Analysis for Nassau Candy Distributor

## 📌 Project Overview

This project analyzes factory-to-customer shipping performance for Nassau Candy Distributor. The objective is to transform raw order and shipment data into actionable logistics intelligence by identifying efficient shipping routes, geographic bottlenecks, factory performance trends, and ship mode effectiveness.

The analysis helps answer key business questions such as:

- Which factory-to-customer routes are most efficient?
- Which routes consistently experience delays?
- How does shipping performance vary across regions and states?
- Which factories perform best and worst?
- Which geographic areas require logistics optimization?
- How effective are different shipping modes?

The project combines data analytics, route efficiency benchmarking, KPI development, visualization, and dashboarding using Python and Streamlit.

---

## 🎯 Problem Statement

Nassau Candy Distributor operates a nationwide distribution network connecting multiple factories to customers across different states and regions.

Without route-level visibility, logistics decisions become reactive rather than proactive.

This project aims to provide:

- Route-level efficiency monitoring
- Geographic bottleneck identification
- Factory performance evaluation
- Ship mode comparison
- Data-driven operational recommendations

---

## 📂 Dataset Information

The dataset contains:

- Customer Orders
- Shipping Information
- Product Details
- Sales Data
- Profit Data
- Geographic Information

### Key Fields

| Field | Description |
|---------|---------|
| Order ID | Unique order identifier |
| Order Date | Date order was placed |
| Ship Date | Date order was shipped |
| Ship Mode | Shipping method |
| Customer ID | Unique customer identifier |
| State/Province | Customer state |
| Region | Customer region |
| Product Name | Product description |
| Sales | Revenue generated |
| Gross Profit | Profit generated |
| Cost | Manufacturing cost |

---

## 🏭 Factory Mapping

Products were mapped to factories using business rules provided in the project requirements.

### Factories

- Lot's O' Nuts
- Wicked Choccy's
- Sugar Shack
- Secret Factory
- The Other Factory

---

## ⚙️ Methodology

### 1. Data Cleaning

- Date conversion and validation
- Missing value inspection
- Lead time calculation
- Data consistency checks

### 2. Feature Engineering

Created:

- Factory Assignment
- Route Identification
- Shipping Lead Time
- Delay Indicators
- Route Efficiency Metrics

### 3. Route Analysis

Defined routes as:

```text
Factory → Customer State
```

Metrics calculated:

- Shipment Volume
- Average Lead Time
- Lead Time Variability
- Delay Frequency
- Route Efficiency Score

### 4. Geographic Analysis

Evaluated:

- State-level performance
- Regional performance
- Geographic bottlenecks
- High-volume delay-prone locations

### 5. Ship Mode Analysis

Compared:

- Standard Class
- Second Class
- First Class
- Same Day

---

## 📊 Key Performance Indicators (KPIs)

### Shipping Lead Time

```text
Ship Date − Order Date
```

### Average Lead Time

Average shipping duration per route.

### Route Volume

Number of shipments per route.

### Delay Frequency

Percentage of shipments exceeding the selected threshold.

### Route Efficiency Score

Normalized route performance score.

---

## 📈 Key Findings

### Factory Performance

- The Other Factory achieved the lowest average lead time.
- Sugar Shack recorded the highest average lead time.

### Regional Performance

- Gulf Region demonstrated the strongest shipping performance.
- Interior Region exhibited the highest average lead time.

### Route Performance

#### Best Route

```text
Secret Factory → Nebraska
```

#### Worst Route

```text
Sugar Shack → New Jersey
```

### Geographic Bottlenecks

High-volume states with elevated lead times:

- Washington
- North Carolina
- Georgia
- Tennessee
- Colorado

### Ship Mode Analysis

- Standard Class achieved the lowest average lead time.
- First Class recorded the highest average lead time.

---

## 🖥️ Streamlit Dashboard Features

### Executive Overview

- Total Orders
- Total Sales
- Average Lead Time
- Delay Percentage

### Route Efficiency Dashboard

- Top 10 Efficient Routes
- Bottom 10 Routes
- Route Performance Leaderboard

### Geographic Analysis

- Regional Performance
- State Bottlenecks
- Shipping Efficiency Insights

### Ship Mode Comparison

- Lead Time Analysis
- Sales Comparison
- Profit Comparison

### Route Drill-Down

Interactive route selection providing:

- Shipment details
- Timeline analysis
- Route-level KPIs

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Plotly
- Streamlit

### Development Environment

- Jupyter Notebook
- Streamlit

### Version Control

- Git
- GitHub

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Ganesh373/nassau-candy-route-analysis.git
```

Navigate to the project folder:

```bash
cd nassau-candy-route-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
nassau-candy-route-analysis/
│
├── app.py
├── Nassau Candy Distributor.csv
├── requirements.txt
├── README.md
├── Nassau_Candy_Analysis.ipynb
└── Project_Report.pdf
```

---

## 📌 Business Recommendations

1. Prioritize optimization efforts in Washington, Tennessee, Georgia, Colorado, and North Carolina.
2. Investigate operational practices contributing to Sugar Shack's higher lead times.
3. Establish route-level monitoring for early bottleneck detection.
4. Continuously benchmark route performance using efficiency scores.
5. Expand dashboard usage to support data-driven logistics planning.

---

## 📚 Conclusion

This project demonstrates how logistics data can be transformed into actionable route-level intelligence. Through route efficiency analysis, geographic bottleneck identification, and performance benchmarking, Nassau Candy Distributor can better understand shipping performance and support future logistics optimization initiatives.

---

## 👨‍💻 Author

**Ganesh**

Factory-to-Customer Shipping Route Efficiency Analysis  
Nassau Candy Distributor Project
