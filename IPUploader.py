___author__ = 'tanmaythakur.com'

import requests
import os

GIT_BRANCH_NAME = "master"


def _get_old_ip():
    with open('current_IP', 'r') as fp:
        old_ip = fp.read().strip()
    return old_ip


def _save_new_ip(ip):
    print("Writing th IP to the file.....")
    with open('current_IP', 'w') as fp:
        fp.write(ip)
    print("\rWriting th IP to the file.....Done\n\n")


def _upload_on_git(ip):
    try:
        print(" Uploading new IP...\n")
        # confirm the correct branch
        os.system("git checkout " + GIT_BRANCH_NAME)

        # send it back to github
        os.system("git add -A")
        os.system("git commit -m \"Recorded new ip " + str(ip) + "\" ")
        os.system("git push origin " + GIT_BRANCH_NAME)
        print("\rUploading new IP...Done\n\n")
    except Exception as ex:
        print("\rUploading new IP..." + ex)


if __name__ == '__main__':
    try:
        print("Program execution started...\n\n")
        ip = requests.get('http://httpbin.org/ip').json()['origin']
        old_ip = _get_old_ip()
        if old_ip != ip:
            print("Ip changed...\n")
            _save_new_ip(ip)
            _upload_on_git(ip)
        print("Program executed successfully....\n\n")
    except Exception as ex:
        print("Program execution failed...." + ex)
