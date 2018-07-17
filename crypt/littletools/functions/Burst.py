import requests,re,os,json
from urllib import quote

def request_ajax_url(url,data):

    headers = {'content-type': 'application/json','X-Requested-With':'XMLHttpRequest'}
    requests.post(url, data=json.dumps(data), headers=headers)

def getfilelist(filepath):
    dirstr = ''
    filelist = os.listdir(filepath)
    for num in range(len(filelist)):
        filename=filelist[num]
        if os.path.isdir(filepath+filename):
            getfilelist(filepath+filename)
        else:
            dirstr += filename+':'
    return dirstr

def backdict(msg):
    path = 'files/list/webback/'
    return getfilelist(path)

def burstback(msg):
    url = msg['url']
    txt = msg['dict']
    anwser = ''
    if(not re.match('^http:\/\/',url)):
        url = 'http://' + url
        f = open('files/list/webback/'+txt,'r')
        text = f.readline()
        while text:
            request = requests.get(url+quote(text),timeout=10)
            if request.status_code == 200:
                anwser += text
            text = f.readline()

    if anwser:
        return anwser
    else:
        return "NO Result"



#burstback({"url":"http://www.cn-heli.cn","dict":"all.txt"})