import pandas as pd
loc = 'C:\Users\Haravindan\Desktop\project.xlsx'
excelfile=pd.ExcelFile(loc)

for i in range(1,11):
    s = 'Sheet'+str(i)
    p = 'Csv'+str(i)+'.csv'
    dframe=excelfile.parse(s)
    dframe.to_csv(p, sep =',')