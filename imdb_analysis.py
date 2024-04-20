import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data, handling bad lines
df = pd.read_csv('name.basics.tsv', sep='\t', on_bad_lines='skip')

# Convert 'birthYear' to numeric, coercing errors
df['birthYear'] = pd.to_numeric(df['birthYear'], errors='coerce')

# Remove rows with NaN in 'birthYear'
df = df.dropna(subset=['birthYear'])

# Convert 'birthYear' from float to int
df['birthYear'] = df['birthYear'].astype(int)

# Print basic statistics of birth years
print(df['birthYear'].describe())

# Visualization of birth year distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['birthYear'], bins=30, color='blue', kde=True)
plt.title('Distribution of Birth Years in IMDb Data')
plt.xlabel('Birth Year')
plt.ylabel('Frequency')
plt.show()

# Handling the primaryProfession column
# Split primaryProfession into individual professions and explode into a new row for each profession
professions = df['primaryProfession'].str.split(',', expand=True).stack()
professions = professions.reset_index(drop=True)

# Count the frequency of each profession
profession_counts = professions.value_counts().head(10)  # top 10 professions

# Plotting the top 10 professions
plt.figure(figsize=(10, 6))
sns.barplot(x=profession_counts.values, y=profession_counts.index, palette='viridis')
plt.title('Top 10 Primary Professions in IMDb Data')
plt.xlabel('Count')
plt.ylabel('Profession')
plt.show()
