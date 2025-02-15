import requests
#request http request---->get,post
# urls=['https://www.google.com/','https://www.twitter.com/']
# urls='https://www.google.com/'

def checkurl(url):
    try:
            #httprequest--->respnse-->(html,css,js,str),statuscode
            #send http request method get ,set timeout 10 s
            response=requests.get(url,timeout=10)
            print(type(response))
            # property,public instance
            if(response.status_code==200):
                print(f'{url} is opend')
            else:
                print(f'{url} closed')
    except requests.exceptions.ConnectionError:
            print(f'{url} not found')

def checkurls(urls):
    for url in urls:
        try:
            #httprequest--->respnse-->(html,css,js,str),statuscode
            #send http request method get ,set timeout 10 s
            response=requests.get(url,timeout=10)
            print(type(response))
            # property,public instance
            if(response.status_code==200):
                print(f'{url} is opend')
            else:
                print(f'{url} closed')
        except requests.exceptions.ConnectionError:
            print(f'{url} not found')
