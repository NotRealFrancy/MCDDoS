import requests
import settings
import fields
import paths

def send_bot(ip: str, host: str, fakehost: str|None, port: str, username: str, version: str|None):
    try:
        headers = {}
        headers[fields.host] = host
        headers[fields.fakehost] = fakehost
        headers[fields.port] = port
        headers[fields.username] = username
        headers[fields.version] = version
        headers['authorization'] = f'Bearer {settings.token}'
        requests.get(f'http://{ip}{paths.createbot}', headers=headers)
    except Exception as err:
        print(f'Cannot connect to {ip} for "{err}".')

def send_bots(host: str, fakehost: str|None, port: str, username: str, version: str|None):
    for ip in settings.ips:
        send_bot(ip, host, fakehost, port, username, version)