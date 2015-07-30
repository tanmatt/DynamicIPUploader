__author__ = 'tanmaythakur.com'
import urllib2, urllib, time


def send_text(cell_num, msg):
    '''
    Input:
        cell_num: Without special characters in string format (ex: cell_num= '1234567890')
        msg: Message to send as text in string format (ex: msg = 'This msg is less than 140 chars')
    Output:
        text message on provided cellphone number
    '''
    txturl_plain = 'http://textbelt.com/text'
    values = {'number': cell_num, 'message': msg}
    try:
        data = urllib.urlencode(values)
        req = urllib2.Request(txturl_plain, data)
        response = urllib2.urlopen(req)
    except Exception, ex:
        print '%s - Err in send_text : %s' % (time.strftime("%D"), str(ex))
