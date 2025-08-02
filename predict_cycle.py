<<<<<<< HEAD
import pandas as pd
import numpy as np
import joblib
from datetime import timedelta

# Load dataset & model
df = pd.read_csv('dataset.csv', parse_dates=['period_date'])
model = joblib.load('model.pkl')

# Prepare data
df['cycle_num'] = np.arange(len(df))
last_cycle_num = df['cycle_num'].iloc[-1]
last_period_date = df['period_date'].iloc[-1]

# Predict next 3 period dates
predicted_dates = []
for i in range(1, 4):
    next_cycle_num = last_cycle_num + i
    # FIX: Pass feature name to avoid sklearn warning
    predicted_days = model.predict(pd.DataFrame([[next_cycle_num]], columns=['cycle_num']))[0]
    last_period_date += timedelta(days=int(round(predicted_days)))
    predicted_dates.append(last_period_date)

# Display results
print("Next predicted period dates:")
for date in predicted_dates:
    print(date.strftime("%Y-%m-%d"))
=======
import pandas as pd
import numpy as np
import joblib
from datetime import timedelta

# Load dataset & model
df = pd.read_csv('dataset.csv', parse_dates=['period_date'])
model = joblib.load('model.pkl')

# Prepare data
df['cycle_num'] = np.arange(len(df))
last_cycle_num = df['cycle_num'].iloc[-1]
last_period_date = df['period_date'].iloc[-1]

# Predict next 3 period dates
predicted_dates = []
for i in range(1, 4):
    next_cycle_num = last_cycle_num + i
    # FIX: Pass feature name to avoid sklearn warning
    predicted_days = model.predict(pd.DataFrame([[next_cycle_num]], columns=['cycle_num']))[0]
    last_period_date += timedelta(days=int(round(predicted_days)))
    predicted_dates.append(last_period_date)

# Display results
print("Next predicted period dates:")
for date in predicted_dates:
    print(date.strftime("%Y-%m-%d"))
>>>>>>> aef99c334d6f5e26c0cfce7dbaae6bbff9702af6
