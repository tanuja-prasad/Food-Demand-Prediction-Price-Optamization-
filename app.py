import streamlit as st
import pandas as pd
import numpy as np
import pickle


model = pickle.load(open("price_recco_model.pkl", "rb"))


d1 = {'Weekday':0,'Weekend':1}
w = {'Sunny':0,'Cloudy':1,'Rainy':2}
loc = {'College':0,'Residential':1,'Office':2}
t = {'Evening':0,'Morning':1,'Afternoon':2}
menu = {'Maggie':0,'Sandwich':1,'Tea':2,'Cold Drink':3}


st.set_page_config(page_title="Food Profit Optimizer", layout="wide")


st.markdown("""
<style>


body {
    background: linear-gradient(to right, #f8f9fa, #e9ecef);
}

.main-title {
    font-size: 40px;
    font-weight: bold;
    color: #2c3e50;
}

.sub-title {
    font-size: 18px;
    color: black;
}

.metric-card {
    background: #ffffff;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}

.sidebar
{
    color:blue;
}

.highlight {
    color: #e74c3c;
    font-weight: bold;
}



</style>
""", unsafe_allow_html=True)


st.markdown('<div class="main-title">🍽️ Food Profit Optimizer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">AI-powered demand prediction & price optimization</div>', unsafe_allow_html=True)

st.markdown("---")



st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #000000;
}


[data-testid="stSidebar"] label {
    color: #ffffff;
}


[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
    background-color: #111111;
    color: #ffffff;
}


div[role="listbox"] {
    background-color: #111111;
    color: #ffffff;
}


div[role="option"]:hover {
    background-color: #333333;
}
</style>
""", unsafe_allow_html=True)

day_type = st.sidebar.selectbox("Day Type", list(d1.keys()))
weather = st.sidebar.selectbox("Weather", list(w.keys()))
location_type = st.sidebar.selectbox("Location", list(loc.keys()))
time_of_day = st.sidebar.selectbox("Time of Day", list(t.keys()))
item_type = st.sidebar.selectbox("Item", list(menu.keys()))

footfall = st.sidebar.slider("Footfall", 50, 300, 100)
cost_price = st.sidebar.slider("Cost Price", 10, 100, 30)


day = d1[day_type]
weather = w[weather]
location = loc[location_type]
daytime = t[time_of_day]
item = menu[item_type]


st.subheader("Try Your Price")

price = st.slider("Select Selling Price", 20, 1000, 50)

test = [[day, weather, location, daytime, item,
         footfall, price, cost_price]]

demand = model.predict(test)[0]
profit = (price - cost_price) * demand


col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>📦 Demand</h3>
        <h2 class="highlight">{int(demand)}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>💸 Profit</h3>
        <h2 class="highlight">₹{int(profit)}</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")


st.subheader("🔥 Best Price Recommendation")

results = []

for p in range(20, 150, 5):
    test = [[day, weather, location, daytime, item,
             footfall, p, cost_price]]
    
    d = model.predict(test)[0]
    prof = (p - cost_price) * d
    results.append((p, d, prof))

best = max(results, key=lambda x: x[2])

st.success(f"💡 Optimal Price: ₹{best[0]}")

col3, col4 = st.columns(2)

col3.metric("Expected Demand", f"{int(best[1])}")
col4.metric("Max Profit", f"₹{int(best[2])}")


st.markdown("### 📈 Profit vs Price")

df_results = pd.DataFrame(results, columns=["Price", "Demand", "Profit"])
st.area_chart(df_results.set_index("Price"))


st.markdown("### 💡 Smart Insights")

if weather == 2:
    st.warning("🌧️ Rainy Day → Promote Tea & Maggie")

if location == 0:
    st.info("🎓 College Area → Keep prices affordable")

if time_of_day == 0:
    st.success("🌆 Evening Rush → Focus on snacks")