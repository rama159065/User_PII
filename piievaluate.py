from PIIModelSerialize import *
from PIIEvaluateModel import *
from piiFeatureCreation import *

fileName = "generic_model.pkl"
filePath = "D:\python_examples\PII_DATA\pickle\\"

testDir = 'D:\\python_examples\\PII_DATA\\test\\data\\'
ser = PIIModelSerialize()
model = ser.load(filePath, fileName)
cols, df = prepareData(testDir)
df.drop(['label'], axis=1, inplace=True)
evaluate = PIIEvaluateModel()
predictions_proba_eval = evaluate.predict_proba(model, df)
predictions_eval = evaluate.predict(model, df)
dr = DataReader()
actual_df = dr.mergeData(testDir)
print("actual df is ", actual_df)

prob_df = pd.DataFrame.from_records(predictions_proba_eval, columns=['email_prob',  'guid_prob',  'ip_prob',  'phone_prob'])
print("prob df is", prob_df)

pred_df = pd.DataFrame(predictions_eval, columns=['prediction'])

input_data_columns=['email','gid','ip','phone']
pred_df['label'] = pd.Categorical.from_codes(predictions_eval,input_data_columns)

final_df = pd.concat([actual_df, prob_df, pred_df], axis=1)
print("final df is ", final_df)

#writing test data,prediction prob, prediction, prediction label to csv file
final_df.to_csv('D:\\python_examples\\PII_DATA\\predict_proba\\pii_prob.csv',index=False, header=True, decimal='.', sep=',', float_format='%.2f')

#writing test data,prediction prob, prediction, prediction label to excel file
writer = pd.ExcelWriter('D:\\python_examples\\PII_DATA\\predict_proba\\pii_prob_xl.xlsx', engine='xlsxwriter')
final_df.to_excel(writer, float_format='%0.2f', sheet_name='prediction_report', index=False)
writer.save()

