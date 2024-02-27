# Compare values in two pandas dataframes

from tabulate import tabulate
import pandas as pd
import numpy as np

# Elements for Expected value dataset
Expectedset = {'Keys1': ['account', 'clordid', 'custorderhandlinginst', 'executionid', 'executiontype',
                         'lastshares', 'operatorid', 'orderid', 'orderquantity', 'price', 'securitytype',
                         'sequencenumber', 'side', 'symbol', 'targetcomputerid', 'targetsubid', 'transacttime'],
               'Expected': ['BATS', 'None', 'Y', 'S1000000FDR', '4', '0', '148', '172H1JDVCPWV', '10',
                            '11.00', 'FUT', '0', '2', '000001', 'FOOA', '0003', '2022-02-02T14:12:02:97900']}

# Create dataframe1 for Expected value dataset
df1 = pd.DataFrame(Expectedset, columns=['Keys1', 'Expected'])
# print Expected value table
# print(df1)

# Elements for Actual value dataset
Actualset = {'Keys2': ['account', 'clordid', 'custorderhandlinginst', 'executionid', 'executiontype',
                       'lastshares', 'operatorid', 'orderid', 'orderquantity', 'price', 'securitytype',
                       'sequencenumber', 'side', 'symbol', 'targetcomputerid', 'targetsubid', 'transacttime'],
             'Actual': ['BATS', 'restingSellOrder_GVB', 'Y', 'S100000FE0', '4', '0', 'CFE', '172H1JDVCPWV', '10',
                        '11.00', 'FUT', '1822', '2', '000001', 'FOOA', '0001', '2022-02-02T15:12:02:97900']}

# Create dataframe2 for Expected value dataset
df2 = pd.DataFrame(Actualset, columns=['Keys2', 'Actual'])
#print(df2)

# Add actual column into dataframe1
df1.insert(2,"Actual",df2['Actual'])

# Create a new column in dataframe1 to check which keys match
df1['Matching Values'] = np.where(df1['Expected'] == df2['Actual'], 'Match', 'No Match')

df1['Expected'] = df2['Actual']

#Print table using tabulate
print(tabulate(df1,headers='keys',tablefmt='psql'))
