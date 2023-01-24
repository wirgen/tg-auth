import getopt
import sys

from telethon.sessions import StringSession
from telethon.sync import TelegramClient


def main(argv):
    api_id = ''
    api_hash = ''
    phone = ''
    password = ''

    try:
        opts, args = getopt.getopt(argv, "h", ["api-id=", "api-hash=", "phone=", "password="])
    except getopt.GetoptError:
        print('tg-auth --api-id <api_id> --api-hash <api_hash>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('tg-auth --api-id <api_id> --api-hash <api_hash> --phone <phone> --password <password>')
            sys.exit()
        elif opt == '--api-id':
            api_id = arg
        elif opt == '--api-hash':
            api_hash = arg
        elif opt == '--phone':
            phone = arg
        elif opt == '--password':
            password = arg

    if api_id == '' or api_hash == '':
        print('tg-auth --api-id <api_id> --api-hash <api_hash>')
        sys.exit(2)

    if phone == '':
        phone = input('Please enter your phone: ')
    if password == '':
        password = input('Please enter your password: ')

    client = TelegramClient('cli', api_id, api_hash).start(phone, password)
    print(client.get_me())

    with open('session', 'w') as file:
        file.write(StringSession.save(client.session))
        file.close()


if __name__ == "__main__":
    main(sys.argv[1:])
