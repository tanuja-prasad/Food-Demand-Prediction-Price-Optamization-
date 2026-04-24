# 🍔 Food Demand Prediction & Price Optimization

## 📌 Problem Statement

To build a machine learning model that predicts product demand and recommends the optimal selling price to maximize profit based on factors like weather, location, time, and customer footfall.

---

## 📊 Project Overview

This project uses historical sales data from a food business to:

* Predict demand for different food items
* Analyze how external factors impact sales
* Suggest the best price to maximize profit

The system tries multiple price points and selects the one that gives the highest expected profit.

---

## 🧾 Dataset Description

The dataset contains the following features:

| Feature       | Description                          |
| ------------- | ------------------------------------ |
| day_type      | Weekday / Weekend                    |
| weather       | Sunny / Cloudy / Rainy               |
| location_type | College / Residential / Office       |
| time_of_day   | Morning / Afternoon / Evening        |
| item_type     | Maggie / Sandwich / Tea / Cold Drink |
| footfall      | Number of customers                  |
| item_price    | Selling price                        |
| cost_price    | Cost of item                         |
| demand        | Number of items sold (Target)        |

---

## ⚙️ Data Preprocessing

* Converted categorical values into numerical format using mapping
* Checked for missing values and dataset structure


---

## 🤖 Model Used

* **Linear Regression**
* Train-test split: 80% training, 20% testing

---

## 📈 Model Performance

| Metric                         | Value  |
| ------------------------------ | ------ |
| R² Score                       | 0.40   |
| Mean Squared Error (MSE)       | 562.38 |
| Root Mean Squared Error (RMSE) | ~23.7  |

### 📌 Interpretation

* Model explains ~40% of demand variation
* Average prediction error is ~24 units of demand
* Suitable for basic analysis, but needs improvement for real-world use

---

## 💡 Price Optimization Logic

1. User inputs conditions (day, weather, location, etc.)

2. Model predicts demand for different prices (₹20 to ₹110)

3. Profit is calculated:

   Profit = (Selling Price - Cost Price) × Predicted Demand

4. The price with maximum profit is selected

---

## 🧠 Example Output

```
Best Price Strategy:
Price: 60
Expected Demand: 120
Expected Profit: 4800 Rs
```

---

## 💾 Model Saving

The trained model is saved using pickle:

```
price_recco_model.pkl
```

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install numpy pandas scikit-learn
```

### 2. Run the script

```
python your_script.py
```

### 3. Enter inputs when prompted

---

## 🔧 Future Improvements

* Use advanced models (Random Forest, XGBoost)
* Apply One-Hot Encoding instead of label mapping
* Add more real-world features (festivals, discounts, competition)
* Build an interactive UI using Streamlit
* Improve model accuracy (target R² > 0.7)

---

## 👩‍💻 Author

Tanuja Prasad

---

## ⭐ Conclusion

This project demonstrates how machine learning can help small businesses make smarter pricing decisions by combining demand prediction with profit optimization.

Google Colab Notebook Link :

https://colab.research.google.com/drive/1NofVfOExsYs3R2LfeayuVjtdFwxYT4y9?usp=sharing

Screenshots
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9b5d64d4-3383-4d57-aff8-e91dbb1be324" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/85533564-32fe-4052-b107-182db5df0a70" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4276b445-5951-4b87-be8c-5ca8f5c4cc31" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4b5d3e07-ae2c-48e2-af66-616da813d9c6" />




