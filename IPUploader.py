___author__ = 'tanmaythakur.com'

import requests, os
from time import strftime, gmtime


GIT_BRANCH_NAME = "master"

def _get_old_ip():
    with open('current_IP', 'r') as fp:
        old_ip = fp.read().strip()
    return old_ip


def _save_new_ip(ip):
    with open('current_IP', 'w') as fp:
        fp.write(ip)


def _upload_on_git(ip):
    try:
        # confirm the correct branch
        os.system("git checkout " + GIT_BRANCH_NAME)

        # send it back to github
        os.system("git add -A")
        os.system("git commit -m \"Recorded new ip " + str(ip) + "\" ")
        os.system("git push origin " + GIT_BRANCH_NAME)
    except Exception, ex:
        print ex


if __name__ == '__main__':
    try:
        ip = requests.get('http://httpbin.org/ip').json()['origin']
        old_ip = _get_old_ip()
        if old_ip != ip:
            _save_new_ip(ip)
            _upload_on_git(ip)
    except Exception, ex:
        msg = '%s - Error: %s' % (strftime("%m-%d-%Y %H:%M:%S", gmtime()), str(ex))
        print msg
