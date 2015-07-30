___author__ = 'tanmaythakur.com'

import requests
import messenger
from time import strftime, gmtime

cell_number = '1234567890'



def _get_old_ip():
    with open('current_IP', 'r') as fp:
        old_ip = fp.read().strip()
    return old_ip


def _save_new_ip(ip):
    with open('current_IP', 'w') as fp:
        fp.write(ip)


if __name__ == '__main__':
    try:
        ip = requests.get('http://httpbin.org/ip').json()['origin']
        old_ip = _get_old_ip()
        if old_ip != ip:
            messenger.send_text(cell_number, "\n\nNew IP is: " + ip)
            _save_new_ip(ip)
    except Exception, ex:
        msg = '%s - Error: %s' %(strftime("%m-%d-%Y %H:%M:%S", gmtime()), str(ex))
        print msg
        messenger.send_text(cell_number, msg)