import unittest
import pandas as pd
import numpy as np

uno = pd.read_excel('C:\\Users\\kevin\\OneDrive\\Escritorio\\uno.xls', sheet_name='Contactos')

class MyTestCase(unittest.TestCase):
    def test_something(self):
        #check if the ID have one email
        val = 'africa@altecom.es' in uno[uno['ID'] == 12]['Email'].values
        # value = uno[uno['ID'] == 2]['Email'].value_counts()['agata@hotmail.com'] > 0
        self.assertEqual(True, val)  # add assertion here

    def test_something_else(self):
        uno = pd.read_excel('C:\\Users\\kevin\\OneDrive\\Escritorio\\uno.xls', sheet_name='Contactos')

        ids = uno['ID'].unique()

        # get just one row for each ID
        dos = open('new.csv', 'w', encoding="utf-8")

        uno.drop_duplicates(subset=['Email','ID'], inplace=True)
        uno.drop(columns=['Email'], inplace=True)


        dos = pd.DataFrame(uno)
        print(dos)
        #
        # for id in ids:
        #     dos.write(uno.columns)
        #     dos.write(uno[uno['ID'] == id].head(1).values.tostring())
        #     dos.write('\n')
        # dos.close()
        # # self.assertEqual(True, value)  # add assertion here
        #
        # print(dos.head())
        # print(ids)
        #
        #
        # print(uno[uno['ID'] == 20].head(1))

if __name__ == '__main__':
    unittest.main()
