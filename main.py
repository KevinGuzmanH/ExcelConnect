import pandas as pd

if __name__ == '__main__':

    usersMails = []
    usersPhones = []

    def countEmails(ID):
        emailcount = 0
        for user in usersMails:
            if user.ID == ID:
                emailcount += 1
        return emailcount

    def countPhones(ID):
        phonecount = 0
        for user in usersPhones:
            if user.ID == ID:
                phonecount += 1
        return phonecount

    def checkIDPositionInMails(ID):
        for i in range(len(usersMails)):
            if usersMails[i].ID == ID:
                return i
        return -1

    def checkIDPositionInPhones(ID):
        for i in range(len(usersPhones)):
            if usersPhones[i].ID == ID:
                return i
        return -1

    def clearMoreThanThreeEmailsByUser():
        for user in usersMails:
            while countEmails(user.ID) > 3:
                usersMails.pop(checkIDPositionInMails(user.ID))

    def clearMoreThanThreePhonesByUser():
        for user in usersPhones:
            while countPhones(user.ID) > 3:
                usersPhones.pop(checkIDPositionInPhones(user.ID))

    uno = pd.read_excel('C:\\Users\\kevin\\OneDrive\\Escritorio\\uno.xls', sheet_name='Contactos')

    idList = uno['ID'].unique().tolist()
    emailList = uno['Email'].unique().tolist()
    phoneList = uno['Teléfono'].unique().tolist()

    class User():
        def __init__(self, ID, Field, FieldCount):
            self.ID = ID
            self.Field = Field
            self.FieldCount = FieldCount


    # add emails to the email list
    for id in idList:
        for email in emailList:
            if email in uno[uno['ID'] == id]['Email'].values:
                usersMails.insert(0, User(id, email, uno[uno['ID'] == id]['Email'].value_counts()[email]))

    # add phones to the phones list
    for id in idList:
        for phone in phoneList:
            if phone in uno[uno['ID'] == id]['Teléfono'].values:
                usersPhones.insert(0, User(id, phone, uno[uno['ID'] == id]['Teléfono'].value_counts()[phone]))

    usersMails.sort(key=lambda x: x.FieldCount, reverse=False)
    usersPhones.sort(key=lambda x: x.FieldCount, reverse=False)

    clearMoreThanThreeEmailsByUser()
    clearMoreThanThreePhonesByUser()

    uno.drop(columns=['Email'], inplace=True)
    uno.drop(columns=['Teléfono'], inplace=True)

    dos = pd.DataFrame(uno)
    dos.drop_duplicates(subset=['ID'], inplace=True)

    usersMails.sort(key=lambda x: x.FieldCount, reverse=True)
    usersPhones.sort(key=lambda x: x.FieldCount, reverse=True)

    for id in idList:
        aux = 1;
        while checkIDPositionInMails(id) != -1:
            dos.loc[dos['ID'] == id, 'Email_'+str(aux)] = usersMails[checkIDPositionInMails(id)].Field
            usersMails.pop(checkIDPositionInMails(id))
            aux += 1

    for id in idList:
        aux = 1;
        while checkIDPositionInPhones(id) != -1:
            dos.loc[dos['ID'] == id, 'Teléfono_'+str(aux)] = usersPhones[checkIDPositionInPhones(id)].Field
            usersPhones.pop(checkIDPositionInPhones(id))
            aux += 1

    dos.to_csv('C:\\Users\\kevin\\PycharmProjects\\EmailAnalyse\\newFile.csv', index=False, encoding="latin1")

    print('Listo')