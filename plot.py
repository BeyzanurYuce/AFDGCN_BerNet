import pandas as pd
import matplotlib.pyplot as plt

# Load Real Data
real_data_path = r"C:\Users\Lenovo\Downloads\Konya_Create_npz_File-main\all_csv_docs\azerbeycan.csv"
df_real = pd.read_csv(real_data_path)

# Load Prediction Data
pred_data_path = r"C:\Users\Lenovo\Downloads\Konya_Create_npz_File-main\output.csv"
df_pred = pd.read_csv(pred_data_path, skiprows=1, header=None, names=['timestep', 'location', 'flow', 'occupy', 'speed'])

# Define Parameters
start_date = pd.Timestamp("2024-02-24 05:45")
time_interval = 15  # in minutes
daily_time_steps = 73
total_days = 6

# Extract Real Data (21 - 31 January)
total_time_steps = daily_time_steps * total_days
df_real_period = df_real.iloc[-total_time_steps:]

# Generate Time Steps for Real Data
time_steps_real = [start_date + pd.Timedelta(minutes=time_interval * i) for i in range(total_time_steps)]

# Extract Prediction Data (Last 9 Hours of 31 January)
# last_9_hours_steps = 36  # 9 hours x 4 (15-min intervals per hour)
# df_pred_last_9_hours = df_pred[df_pred['location'] == 0].iloc[-last_9_hours_steps:]

# # Generate Time Steps for Prediction Data
# start_pred_time = pd.Timestamp("2024-01-31 00:00") + pd.Timedelta(hours=24 - 9)
# time_steps_pred = [start_pred_time + pd.Timedelta(minutes=time_interval * i) for i in range(last_9_hours_steps)]

df_pred_location = df_pred[df_pred['location'] == 0].iloc[-total_time_steps:]
# Generate Time Steps for Prediction Data
start_pred_time = pd.Timestamp("2024-02-24 05:45") 
#- pd.Timedelta(minutes=(len(df_pred_location) - 1) * time_interval)
time_steps_pred = [start_pred_time + pd.Timedelta(minutes=time_interval * i) for i in range(len(df_pred_location))]

# Plot Both Datasets
plt.figure(figsize=(14, 8))

# Real Data
plt.plot(time_steps_real, df_real_period['flow'], label="Real Traffic Flow", color="blue")

# Prediction Data
plt.plot(time_steps_pred, df_pred_location['flow'], label="Predicted Traffic Flow", color="orange", linestyle="--")

# Customize Graph
plt.xlabel("Time")
plt.ylabel("Traffic Flow")
plt.title("Comparison of Real and Predicted Traffic Flow")
plt.legend(loc="upper right")
plt.grid()
plt.tight_layout()

# Display the Plot
plt.show()
