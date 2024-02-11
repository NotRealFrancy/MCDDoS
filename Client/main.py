import utils.platformutils as platformutils
from sys import exit
import api
import os

def clear_console():
    if platformutils.get_system() == 'Windows': os.system('cls')
    else: os.system('clear')
    with open('title.txt', 'r') as f:
        print(f.read())

def run():
    try:
        clear_console()

        while True:
            prompt = input('>> ')
            args = prompt.split(' ')

            if len(args) < 1:
                break

            if args[0].lower() == 'help':
                print('\n"run": Start the application.\n"set": Adds a variable to environment.\n"values": Get the list of all environment variables.\n"clear" (or "cls"): Clears the console.\n"exit" (or "quit"): Close the application.\n')
            elif args[0].lower() == 'run':
                try:
                    host = os.environ['MCDDOS_HOST']

                    try:
                        fakehost = os.environ['MCDDOS_FAKEHOST']
                    except Exception as err:
                        fakehost = host

                    try:
                        port = os.environ['MCDDOS_PORT']

                        try:
                            username = os.environ['MCDDOS_USERNAME']

                            try:
                                version = os.environ['MCDDOS_VERSION']
                            except Exception as err:
                                version = '1.8.9'

                            api.send_bots(host, fakehost, port, username, version)
                        except Exception as err:
                            print('\n"USERNAME" value isn\'t initialized. Use "set USERNAME [bots username]"\n')
                    except Exception as err:
                        print('\n"PORT" value isn\'t initialized. Use "set PORT [target port]"\n')
                except Exception as err:
                    print('\n"HOST" value isn\'t initialized. Use "set HOST [target server]"\n')
            elif args[0].lower() == 'set':
                if len(args) > 2:
                    variable_name = args[1]
                    variable_value = args[2]

                    os.environ[f'MCDDOS_{variable_name}'] = variable_value
                    print(f'\n{variable_name}=>{variable_value}\n')
                else:
                    print('\nSyntax: set [name] [value]\n')
            elif args[0].lower() == 'values':
                print()
                for key in os.environ.keys():
                    if key.startswith('MCDDOS_'):
                        name = key[7:len(key)]
                        value = os.environ[key]
                        print(f'{name}=>{value}')
                print()
            elif args[0].lower() == 'clear' or args[0].lower() == 'cls':
                clear_console()
            elif args[0].lower() == 'quit' or args[0].lower() == 'exit':
                raise KeyboardInterrupt()
    except KeyboardInterrupt as e:
        print('Stopping...')
        exit()

if __name__ == '__main__':
    run()