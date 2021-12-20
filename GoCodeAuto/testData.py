import pandas
import openpyxl

excel_data_df = pandas.read_excel('Sample_Data.xlsx', sheet_name='Sheet1')

# print whole sheet data
print(excel_data_df)

