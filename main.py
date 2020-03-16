import bs4 as bs
import requests
from pip._vendor.distlib.compat import raw_input
import string


def convertASCII(TEXT):
    return ''.join(filter(lambda x: x in string.printable, TEXT))


def urlGen(USERNAME):
    URL = 'http://gettwitterid.com/?user_name=' + USERNAME + '&submit=GET+USER+ID'
    return URL


def urlGen2(USERID, MESSAGE):
    URL2 = 'https://twitter.com/messages/compose?text=' + \
        MESSAGE + '&recipient_id=' + USERID
    return URL2


userName = input('Username: ')
url = urlGen(userName)

sauce = requests.get(url)
soup = bs.BeautifulSoup(sauce.text, 'lxml')

AccountInfo = soup.findAll('p', class_='')

UserID = AccountInfo[1].text
ScreenName = AccountInfo[3].text

print('\n\nUSER: ' + convertASCII(ScreenName))
print('USER ID: ' + UserID + '\n\n')


UserMessage = input('Enter a message: ')
UserMessage = UserMessage.replace(' ', '%20')

FinalURL = urlGen2(UserID, UserMessage)

print(FinalURL)
