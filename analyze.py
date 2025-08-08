import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 1. Load the CSV file
# ---------------------------
# If you're using Colab, upload your CSV first.
df = pd.read_csv("sales_data.csv")

print("First few rows of our data:")
print(df.head())

# ---------------------------
# 2. Quick data info
# ---------------------------
print("\nBasic info about the dataset:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

# Make sure 'Date' column is in proper datetime format (if it exists)
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])

# ---------------------------
# 3. Sales by product
# ---------------------------
product_sales = df.groupby("Product")["Sales"].sum().reset_index()
print("\nTotal sales by product:")
print(product_sales)

# Plot
plt.figure(figsize=(8,5))
plt.bar(product_sales["Product"], product_sales["Sales"], color="skyblue")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=30)
plt.show()

# ---------------------------
# 4. Sales by region
# ---------------------------
region_sales = df.groupby("Region")["Sales"].sum().reset_index()
print("\nTotal sales by region:")
print(region_sales)

# Plot
plt.figure(figsize=(8,5))
plt.bar(region_sales["Region"], region_sales["Sales"], color="lightgreen")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# ---------------------------
# 5. Monthly sales trend
# ---------------------------
if "Date" in df.columns:
    monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum().reset_index()
    monthly_sales["Date"] = monthly_sales["Date"].astype(str)

    print("\nMonthly sales trend:")
    print(monthly_sales)

    # Plot
    plt.figure(figsize=(10,5))
    plt.plot(monthly_sales["Date"], monthly_sales["Sales"], marker="o", color="orange")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()

print("\n✅ Done! We've explored the data and created charts.")
