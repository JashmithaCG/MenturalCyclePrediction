<<<<<<< HEAD
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv('dataset.csv', parse_dates=['period_date'])

# Calculate cycle lengths in days
df['cycle_length'] = df['period_date'].diff().dt.days
df = df.dropna().reset_index(drop=True)

# Create X as cycle number, y as cycle length
df['cycle_num'] = np.arange(len(df))
X = df[['cycle_num']]
y = df['cycle_length']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model.pkl')
print("Model trained and saved as model.pkl")
=======
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv('dataset.csv', parse_dates=['period_date'])

# Calculate cycle lengths in days
df['cycle_length'] = df['period_date'].diff().dt.days
df = df.dropna().reset_index(drop=True)

# Create X as cycle number, y as cycle length
df['cycle_num'] = np.arange(len(df))
X = df[['cycle_num']]
y = df['cycle_length']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model.pkl')
print("Model trained and saved as model.pkl")
>>>>>>> aef99c334d6f5e26c0cfce7dbaae6bbff9702af6
