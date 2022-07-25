import unittest
import pandas as pd

uno = pd.read_excel('C:\\Users\\kevin\\OneDrive\\Escritorio\\uno.xls', sheet_name='Contactos')

class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(uno.groupby('Email')['ID'].value_counts())

if __name__ == '__main__':
    unittest.main()
