# Loan Approval Prediction

## 📌 Project Overview
This is a Machine Learning project that predicts whether a loan application will be **approved** or **not approved** based on an applicant's **income** and **credit score**.

The project includes both a basic Python prediction script and a Flask web application interface.

## 🎯 What This Project Does
- Uses applicant income and credit score as input features
- Handles missing values in the dataset
- Trains a Logistic Regression classification model
- Predicts loan approval status
- Displays prediction results through a simple Flask web app

## 🧠 Machine Learning Approach
This project uses **Logistic Regression**, which is suitable for binary classification problems.

Prediction output:
- `1` → Loan Approved
- `0` → Loan Not Approved

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Jupyter Notebook
- HTML
- CSS

## 📂 Project Structure
```text
loan-approval-prediction/
│── README.md
│── requirements.txt
│── .gitignore
│── data/
│   └── loan_data.csv
│── src/
│   ├── app.py
│   ├── MLmodel.ipynb
│   ├── model.pkl
│   ├── pyproject.toml
│   ├── poetry.lock
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
  
```

## 📊 Dataset
The dataset contains the following columns:

| Column | Description |
|---|---|
| income | Applicant income |
| credit_score | Applicant credit score |
| loan_status | Loan approval result, where 1 = approved and 0 = not approved |

Missing values are handled using:
- Median value for `income`
- Mean value for `credit_score`

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/loan-approval-prediction.git
cd loan-approval-prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Python prediction script
```bash
python src/app.py
```

### 4. Run the Flask web app
Because `app.py` loads `model.pkl` from the current folder, run the app from inside the `src` folder:

```bash
cd src
python app.py
```

Then open the local Flask link shown in the terminal, usually:

```text
http://127.0.0.1:5000/
```

## ✅ Example Input
```text
Income: 49000
Credit Score: 650
```

## ✅ Example Output
```text
Loan Approved
```

or

```text
Loan Not Approved
```

## 🚀 Future Improvements
- Use a larger real-world loan dataset
- Add more features such as age, employment status, debt amount, and loan amount
- Improve model accuracy using Random Forest or XGBoost
- Add model evaluation metrics such as accuracy, precision, recall, and confusion matrix
- Improve the web app UI and deploy it online

## 👨‍💻 Author
**Chanuuj Navaretnam**
