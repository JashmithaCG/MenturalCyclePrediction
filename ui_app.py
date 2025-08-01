import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import timedelta

# ---------------------- PAGE CONFIG & STYLING ----------------------
st.set_page_config(page_title="Menstrual Cycle Predictor", layout="centered")

st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background-color: #ffe6ec;
    background-image: url('https://www.transparenttextures.com/patterns/pink-flowers.png');
    background-size: auto;
    background-repeat: repeat;
    background-attachment: fixed;
}

.stApp {
    padding-top: 0rem !important;
}

[data-testid="stHeader"] {
    background: transparent;
    height: 0rem;
    visibility: hidden;
}

h1, h2, h3, h4, h5 {
    color: #9c3d5f;
    text-align: center;
}

.stButton>button {
    background-color: #ffb6c1;
    color: white;
    border-radius: 10px;
    padding: 0.5em 1.2em;
    font-weight: bold;
    border: none;
}

.stDownloadButton>button {
    background-color: #e75480;
    color: white;
    border-radius: 10px;
    font-weight: bold;
}

hr {
    border: 1px solid #e88ca0;
}
</style>
""", unsafe_allow_html=True)

# ---------------------- APP TITLE ----------------------
st.markdown("<h1>🌸 Menstrual Cycle Predictor</h1>", unsafe_allow_html=True)
st.write("Upload your past period data (CSV with a `period_date` column). We'll predict your next 12 periods!")

# ---------------------- FILE UPLOAD ----------------------
uploaded_file = st.file_uploader("Upload your cycle data CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        df['period_date'] = pd.to_datetime(df['period_date'])
        df = df.sort_values(by='period_date')

        # ---------------------- ANALYZE CYCLE ----------------------
        df['cycle_length'] = df['period_date'].diff().dt.days
        avg_cycle = int(df['cycle_length'].mean())
        st.success(f"✅ Average Cycle Length: **{avg_cycle} days**")

        # ---------------------- PREDICT NEXT 12 DATES ----------------------
        df['ordinal'] = df['period_date'].map(pd.Timestamp.toordinal)
        X = np.array(range(len(df))).reshape(-1, 1)
        y = df['ordinal'].values
        model = LinearRegression().fit(X, y)

        future_indices = np.array(range(len(df), len(df) + 12)).reshape(-1, 1)
        predicted_ordinals = model.predict(future_indices)
        predicted_dates = [pd.Timestamp.fromordinal(int(day)) for day in predicted_ordinals]

        prediction_df = pd.DataFrame(predicted_dates, columns=['Predicted Period Date'])

        # ---------------------- DISPLAY RESULTS ----------------------
        st.subheader("📅 Next 12 Predicted Period Dates")
        st.dataframe(prediction_df)

        # ---------------------- DOWNLOAD BUTTON ----------------------
        csv = prediction_df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇ Download Predictions as CSV", data=csv, file_name='predicted_periods.csv', mime='text/csv')

        # ---------------------- PLOT TIMELINE ----------------------
        st.subheader("🩸 Visual Timeline of Periods (Past + Predicted)")

        all_dates = pd.concat([
            pd.Series(df['period_date']),
            pd.Series(predicted_dates)
        ], ignore_index=True)

        types = ['Past'] * len(df['period_date']) + ['Predicted'] * len(predicted_dates)
        timeline_df = pd.DataFrame({'Date': all_dates, 'Type': types})

        fig, ax = plt.subplots(figsize=(10, 2))
        colors = {'Past': '#de3163', 'Predicted': '#ffa6c9'}
        ax.scatter(timeline_df['Date'], [1]*len(timeline_df), c=timeline_df['Type'].map(colors), label=timeline_df['Type'])
        ax.set_yticks([])
        ax.set_title("Period Timeline", fontsize=14)
        ax.set_xlabel("Date")
        ax.grid(True, axis='x', linestyle='--', alpha=0.5)
        plt.tight_layout()
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Something went wrong: {e}")

else:
    st.info("👆 Please upload a CSV file with a 'period_date' column (YYYY-MM-DD format)")
