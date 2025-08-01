# MenturalCyclePrediction
A Streamlit-based Menstrual Cycle Predictor that uses machine learning to forecast future periods based on past data. Features include yearly predictions, visual timeline, download option, and a soft, floral-themed UI designed for user comfort and clarity

# 🌸 Menstrual Cycle Predictor

This project is a Streamlit-based web application designed to help users track and predict their menstrual cycles using past period data. It provides a clean and empathetic user interface with a floral theme and includes features for personalized prediction, visualization, and data download.

## ✨ Features

- 📅 Predicts menstrual cycle dates for up to 1 year.
- 📈 Visual timeline of both past and upcoming periods.
- 📥 Option to download predictions as a CSV file.
- 💄 Beautiful blush-pink background with a soft floral design.
- 🤖 Machine Learning-based prediction using linear regression.

## 🛠️ Technologies Used

- Python (Pandas, NumPy, scikit-learn)
- Streamlit
- Matplotlib
- Custom CSS for themed styling

## 📂 Project Structure

📁 MenturalCyclePredictor/
├── data_analysis_train.py # Model training and analysis
├── predict_cycle.py # Logic to predict future dates
├── ui_app.py # Streamlit web app
├── model.pkl # Trained regression model
└── period_data.csv # Input dataset (user’s personal data)

## 📊 Dataset

This project uses a **personal dataset** containing the user’s past menstrual cycle dates.  
**⚠️ Due to privacy reasons, this dataset is not shareable.**

## 🚀 Running the App

Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run ui_app.py

## 📸 UI Preview  
Gentle, floral blush-pink background  
Responsive and clear layout for ease of use  
Designed for emotional comfort and user confidence  

## 🙋‍♀️ Purpose  
To help menstruators confidently anticipate future periods, improve planning, and better understand their cycle using personal data and ML insights.  

## 📤 Output  
📊 Chart: Timeline of past & predicted periods  
🧾 Table: Lists predicted period dates for next 12 months  
📁 Download: Option to save predictions as CSV  
🔄 Cycle Info: Displays calculated average cycle length  


<img width="427" height="575" alt="image" src="https://github.com/user-attachments/assets/c8affd18-54d7-4c99-a288-d54ca6e1c6e6" />
