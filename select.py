#!/usr/bin/env python
import random
import csv
import smtplib

def pairer():
    dictionary = {}
    names = []
    with open('testing.csv', 'r', encoding="utf-8-sig") as info:
        data = csv.reader(info)
        for each in data:
    		dictionary[each[0]] = each[1]
    		names.append(each[0])

    while 1:
        names2 = names[:]
        matches = []

        for name in names:
            randomSelector = random.randint(0, len(names2) -1)

            if (name == names2[randomSelector]) and (len(names2) == 1):
                break

            while(name == names2[randomSelector]):
                randomSelector = random.randint(0, len(names2) -1)
                        
            matches.append(([name, names2[randomSelector]]))
            names2.remove(names2[randomSelector])

        if not names2:
            break

    return dictionary, matches

def gmailsending():
    dictionary, matches = pairer()
#        print(matches)

    for ea in matches:
        sendEmail = dictionary[ea[0]]
        email = 'foobar@gmail.com'
        password = 'password'
        msg = 'Subject: Secret Santa\nYour secret santa is - ' + ea[1] + '!'
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(email, password)
        smtpObj.sendmail(email, sendEmail, msg)
        smtpObj.quit()


if __name__ == '__main__':
    gmailsending()
