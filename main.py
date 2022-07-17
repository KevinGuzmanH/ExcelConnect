import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    usersMails = []

    def countEmails(ID):
        emailCount = 0
        for user in usersMails:
            if user.ID == ID:
                emailCount += 1
        return emailCount


    def checkIDPosition(ID):
        for i in range(len(usersMails)):
            if usersMails[i].ID == ID:
                return i
        return -1


    def clearMoreThanThreeEmailsByUser():
        for user in usersMails:
            while countEmails(user.ID) > 3:
                usersMails.pop(checkIDPosition(user.ID))


    uno = pd.read_excel('C:\\Users\\kevin\\OneDrive\\Escritorio\\uno.xls', sheet_name='Contactos')

    IDList = uno['ID'].unique().tolist()
    EmailList = uno['Email'].unique().tolist()

    class User():
        def __init__(self, ID, Field, FieldCount):
            self.ID = ID
            self.Field = Field
            self.FieldCount = FieldCount


    for id in IDList:
        for email in EmailList:
            if email in uno[uno['ID'] == id]['Email'].values:
                # add in the first position of the list
                usersMails.insert(0, User(id, email, uno[uno['ID'] == id]['Email'].value_counts()[email]))

    usersMails.sort(key=lambda x: x.FieldCount, reverse=False)
    clearMoreThanThreeEmailsByUser()

    uno.drop(columns=['Email'], inplace=True)

    dos = pd.DataFrame(uno)
    dos.drop_duplicates(subset=['ID'], inplace=True)

    usersMails.sort(key=lambda x: x.FieldCount, reverse=True)

    for id in IDList:
        aux = 1;
        while checkIDPosition(id) != -1:
            dos.loc[dos['ID'] == id, 'Email_'+str(aux)] = usersMails[checkIDPosition(id)].Field
            usersMails.pop(checkIDPosition(id))
            aux += 1

    dos.to_csv('new.csv', index=False, encoding="latin1")

# create a list with the ID and the email and name
