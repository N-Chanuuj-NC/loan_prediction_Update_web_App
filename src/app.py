import numpy as np 
from flask import Flask, render_template,request
import pickle

app=Flask(__name__)

model2=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features=[int(i) for i in request.form.values()]
    final_feature=np.array(int_features).reshape(1,-1)
    
    prediction = model2.predict(final_feature) 
    output = (prediction[0])
    
    if(output ==1):
         return render_template('index.html',predict_text='Loan Approved')
    else:         
         return render_template('index.html',predict_text='Loan Not Approved')
        
    
      
if __name__=='__main__':
    app.run(debug=True)
    
    

