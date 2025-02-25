# PREDICTING-MEDICAL-INSURANCE-CHARGE-USING-RANDOM-FOREST-MODEL

## *Overview*
This project predicts medical insurance charges based on demographic and health-related factors using a *Random Forest Regressor* model. The dataset is sourced from [Kaggle: Insurance Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance) and contains details like age, BMI, smoking status, and number of children.

The project includes:
- Data preprocessing
- Training a RandomForestRegressor
- Deploying the model using *Streamlit*

---

## *Dataset Description*
The dataset consists of the following features:

| Feature  | Description |
|----------|------------|
| age  | Age of the insured person (years) |
| sex  | Gender of the insured (male/female) |
| bmi  | Body Mass Index (BMI) |
| children  | Number of dependent children covered by insurance |
| smoker  | Whether the person is a smoker (yes/no) |
| region  | Residential area (northeast, northwest, southeast, southwest) |
| children  | Number of dependent children covered by insurance |
| smoker  | Whether the person is a smoker (yes/no) |
| region  | Residential area (northeast, northwest, southeast, southwest) |
| charges  | Final medical insurance cost (target variable) |

---

## *Installation*
To run this project locally, follow these steps:

### *1. Clone the Repository*
sh
git clone https://github.com/blessing3140/PREDICTING MEDICAL INSURANCE CHARGE USING RANDOM FOREST REGRESSOR MODEL.git
cd insurance-prediction


### *2. Install Dependencies*
sh
pip install -r requirements.txt

### *3. Download the Dataset*
- Download the dataset from [Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance).
- Place the insurance.csv file in the project directory.

---

## *Model Training*
Run the following script to train the model:

sh
python train_model.py


### *Training Steps:*
1. Load the dataset (insurance.csv).
2. Preprocess categorical features (One-Hot Encoding for sex, smoker, region).
3. Split data into training (80%) and testing (20%).
4. Train a *Random Forest Regressor*.
5. Save the trained model as random_forest_model.pkl.

## *Deploying the Model*
To deploy the model using *Streamlit*, run:

sh
streamlit run app.py


### *Streamlit UI Features:*
- Enter age, BMI, number of children, smoking status, gender, and region.
- Click "Predict" to get an estimated insurance cost.

---

## *File Structure*

📂 insurance-prediction
├── app.py               # Streamlit app for deployment
├── train_model.py       # Script to train and save the model
├── random_forest_model.pkl  # Saved RandomForestRegressor model
├── insurance.csv        # Dataset file
├── requirements.txt     # Dependencies
└── README.md            # Project documentation

## *Possible Errors and Fixes*
1. *Model Not Found*  
   - Ensure random_forest_model.pkl exists before running the app.
   - If missing, retrain the model using python train_model.py.

2. *Invalid Input Format*  
   - Ensure numerical values are entered correctly in Streamlit.

3. *Streamlit App Not Running*  
   - Install dependencies with pip install -r requirements.txt.

---

## *Future Improvements*
- Optimize hyperparameters using *GridSearchCV*.
- Deploy the model as a web using *streamlit*.
- Train on a larger dataset for better accuracy.




## *Contributor*
- *Iseguan Blessing* - Data Analyst and Scientist

---

## *License*
This project is licensed under the *MIT License*.

---






