import unittest
import pandas as pd
import numpy as np

uno = pd.read_excel('C:\\Users\\kevin\\OneDrive\\Escritorio\\uno.xls', sheet_name='Contactos')

class MyTestCase(unittest.TestCase):
    def checkID12HaveEmail(self):
        val = 'africa@altecom.es' in uno[uno['ID'] == 12]['Email'].values
        self.assertEqual(True, val)  # add assertion here

    def test_something_else(self):
        uno = pd.read_excel('C:\\Users\\kevin\\OneDrive\\Escritorio\\uno.xls', sheet_name='Contactos')

        uno.drop_duplicates(subset=['Email','ID'], inplace=True)
        uno.drop(columns=['Email'], inplace=True)

        dos = pd.DataFrame(uno)
        print(dos)

        dos.to_csv('C:\\Users\\kevin\\PycharmProjects\\EmailAnalyse\\newFile.csv', index=False, encoding="latin1")

if __name__ == '__main__':
    unittest.main()
