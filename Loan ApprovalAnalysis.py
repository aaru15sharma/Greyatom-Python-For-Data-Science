# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank=pd.DataFrame(bank_data)
categorical_var=bank.select_dtypes(include='object')
print(categorical_var)
numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var)

banks = bank.drop(['Loan_ID'], axis=1)
null=banks.isnull().sum().values.sum()
print(null)
bank_mode=banks.mode()
print(bank_mode)

avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc = 'mean')
print(avg_loan_amount)

loan_approved_se = banks[ (banks['Self_Employed'] == "Yes") & (banks['Loan_Status'] == "Y") ]

loan_approved_nse = banks[ (banks['Self_Employed'] == "No") & (banks['Loan_Status'] == "Y") ]



percentage_se = (len(loan_approved_se) / 614) * 100
percentage_nse = (len(loan_approved_nse) / 614) * 100

loan_term = banks['Loan_Amount_Term'].apply(lambda x: float(x)/12 )





big_loan_term=len(loan_term[loan_term>=25])



print(big_loan_term)

columns_to_show = ['ApplicantIncome', 'Credit_History']

 

loan_groupby=banks.groupby(['Loan_Status'])[columns_to_show]


mean_values=loan_groupby.agg([np.mean])



print(mean_values)





