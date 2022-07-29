import numpy as np
import pandas as pd
from argparse import ArgumentParser
from tqdm import tqdm

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filepath",
                    help="Where is the old excel file")

parser.add_argument("-i", "--id", dest="idcolumn",
                    help="The name of the column with the ID's")

parser.add_argument("-p", "--phone", dest="phonecolumn",
                    help="The name of the column with the phone numbers")

parser.add_argument("-e", "--email", dest="emailcolumn",
                    help="The name of the column with the email addresses")

parser.add_argument("-s", "--sheet", dest="sheetname",
                    help="The name of the sheet in the excel file")

args = parser.parse_args()

if __name__ == '__main__':

    class UserInfo():
        def __init__(self, id, field, fieldcount):
            self.id = id
            self.field = field
            self.fieldcount = fieldcount

    usersMails = []
    usersPhones = []

    def countEmails(id):
        emailcount = 0
        for user in usersMails:
            if user.id == id:
                emailcount += 1
        return emailcount


    def countPhones(id):
        phonecount = 0
        for user in usersPhones:
            if user.id == id:
                phonecount += 1
        return phonecount


    def checkIDPositionInMails(id):
        for i in range(len(usersMails)):
            if usersMails[i].id == id:
                return i
        return -1


    def checkIDPositionInPhones(id):
        for i in range(len(usersPhones)):
            if usersPhones[i].id == id:
                return i
        return -1


    def clearMoreThanThreeEmailsByUser():
        for user in usersMails:
            while countEmails(user.id) > 3:
                usersMails.pop(checkIDPositionInMails(user.id))


    def clearMoreThanThreePhonesByUser():
        for user in usersPhones:
            while countPhones(user.id) > 3:
                usersPhones.pop(checkIDPositionInPhones(user.id))


    # Read the excel file to use
    PATH = args.filepath
    IDCOLUMN = args.idcolumn
    PHONECOLUMN = args.phonecolumn
    EMAILCOLUMN = args.emailcolumn
    SHEET = args.sheetname

    oldEx = pd.read_excel(PATH, sheet_name=SHEET)

    # get the ids, emails and phones without repetitions
    idList = oldEx[IDCOLUMN].unique().tolist()
    emailList = oldEx[EMAILCOLUMN].unique().tolist()
    phoneList = oldEx[PHONECOLUMN].unique().tolist()

    # add emails to the email list
    for id in idList:
        emailsForThisID = oldEx[oldEx[IDCOLUMN] == id][EMAILCOLUMN]
        for email in emailList:
            if email in emailsForThisID.values:
                usersMails.insert(0,
                                  UserInfo(id, email, emailsForThisID.value_counts()[email]))

    # add phones to the phones list
    for id in idList:
        phonesForThisID = oldEx[oldEx[IDCOLUMN] == id][PHONECOLUMN]
        for phone in phoneList:
            if phone in phonesForThisID.values:
                usersPhones.insert(0,
                                   UserInfo(id, phone, phonesForThisID.value_counts()[phone]))

    # organize the emails and phones lists by least repetitions to delete the least repeated
    usersMails.sort(key=lambda x: x.fieldcount, reverse=False)
    usersPhones.sort(key=lambda x: x.fieldcount, reverse=False)

    # remove emails and phones with more than three repetitions
    clearMoreThanThreeEmailsByUser()
    clearMoreThanThreePhonesByUser()

    # remove the emails and phones columns from the oldEx dataframe
    oldEx.drop(columns=[EMAILCOLUMN], inplace=True)
    oldEx.drop(columns=[PHONECOLUMN], inplace=True)

    # create a new dataframe with the same columns and rows as the new dataframe without ID repetitions
    newEx = pd.DataFrame(oldEx)
    newEx.drop_duplicates(subset=[IDCOLUMN], inplace=True)

    # organize the emails and phones lists by highest repetitions to take first the most repeated
    usersMails.sort(key=lambda x: x.fieldcount, reverse=True)
    usersPhones.sort(key=lambda x: x.fieldcount, reverse=True)

    # add the emails and phones columns to the new dataframe
    for id in idList:
        aux = 1;
        while checkIDPositionInMails(id) != -1:
            newEx.loc[newEx[IDCOLUMN] == id, 'Email_' + str(aux)] = usersMails[checkIDPositionInMails(id)].field
            usersMails.pop(checkIDPositionInMails(id))
            aux += 1

    for id in idList:
        aux = 1;
        while checkIDPositionInPhones(id) != -1:
            newEx.loc[newEx[IDCOLUMN] == id, 'Teléfono_' + str(aux)] = usersPhones[checkIDPositionInPhones(id)].field
            usersPhones.pop(checkIDPositionInPhones(id))
            aux += 1


    # save the new dataframe to a csv file
    try:
        print("Saving the new csv file...")
        chunks = np.array_split(newEx.index, 100)  # chunks of 100 rows

        for chunck, subset in enumerate(tqdm(chunks)):
            if chunck == 0:  # first row
                newEx.loc[subset].to_csv('data.csv', mode='w', index=False, encoding="latin1")
            else:
                newEx.loc[subset].to_csv('data.csv', header=None, mode='a', index=False, encoding="latin1")

        print('Done!')
    except PermissionError:
        print('Error: The file is open, please close it and try again')
