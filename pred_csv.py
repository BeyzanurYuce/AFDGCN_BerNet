import pandas as pd

# Input and output file paths
input_file = '/content/AFDGCN_Garnoldi/test_results.csv'  # Replace with the path to your input file
output_file = 'test_gar.csv'  # Replace with the desired path for the output file

# Read the input CSV file
df_input = pd.read_csv(input_file, skiprows=1, names=["flow"])  # Read the file with one column named "flow"
df_input["flow"] = df_input["flow"].round().astype(int).abs()

# Create lists to hold the generated data
timesteps = []
locations = []
flows = []
occupies = []
speeds = []

# Process the data
for i in range(len(df_input)):
    timestep = i // 8 + 1  # Calculate the timestep (1-based)
    location = i % 8       # Calculate the location (0-7)
    timesteps.append(timestep)
    locations.append(location)
    flows.append(df_input.loc[i, "flow"])
    occupies.append(1)  # Occupy is always 1
    speeds.append(1)    # Speed is always 1

# Create the output DataFrame
df_output = pd.DataFrame({
    "timestep": timesteps,
    "location": locations,
    "flow": flows,
    "occupy": occupies,
    "speed": speeds
})

# Save the output DataFrame to a CSV file
df_output.to_csv(output_file, index=False)

print(f"Output file saved as {output_file}")
