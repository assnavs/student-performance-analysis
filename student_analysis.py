import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students_from_sql.csv")

# Average math score by gender
df.groupby('gender')['math score'].mean().plot(kind='bar')
plt.title("Average Math Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Math Score")
plt.show()

# Test preparation impact
df.groupby('test preparation course')['math score'].mean().plot(kind='bar')
plt.title("Test Preparation vs Math Score")
plt.xlabel("Test Preparation")
plt.ylabel("Math Score")
plt.show()

# Parental education impact
df.groupby('parental level of education')['math score'].mean().plot(kind='bar')
plt.title("Parental Education vs Math Score")
plt.xlabel("Parental Education")
plt.ylabel("Math Score")
plt.xticks(rotation=45)
plt.show()
