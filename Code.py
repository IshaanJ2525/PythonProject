import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data file
data = pd.read_csv("data.csv")
print(data.to_string())

# Cleaning Date column
data['Date'] = pd.to_datetime(data['Date'].astype(str).str.replace("'", "").str.strip(), errors='coerce')
data = data.dropna(subset=['Date'])  # Remove rows with invalid/missing dates
data = data.dropna(subset=['Calories'])

# Removing large durations
data = data[data['Duration'] < 200]

#Data After cleaning
print("\n\n",data.to_string())

# Stats
average_duration = np.mean(data['Duration'])
max_pulse = np.max(data['Pulse'])
min_calories = np.min(data['Calories'])

print("\n\n Average Workout Duration:", round(average_duration, 2), "minutes")
print("Maximum Pulse:", max_pulse)
print("Minimum Calories Burned:", min_calories)

# Bar Plot
plt.figure(figsize=(10, 5))
plt.bar(data['Date'].dt.strftime('%m-%d'), data['Duration'], color='skyblue')
plt.title("\n\n Workout Duration by Date")
plt.xlabel("Date (MM-DD)")
plt.ylabel("Duration (minutes)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Line Graph
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Calories'], color='green', marker='o')
plt.title("Calories Burned Over Time")
plt.xlabel("Date")
plt.ylabel("Calories")
plt.grid(True)
plt.tight_layout()
plt.show()
