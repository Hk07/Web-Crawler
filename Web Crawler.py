import requests
import sys
from bs4 import BeautifulSoup

link = []
flags = []

with requests.Session() as session:
        web ='URL'
        USERNAME = sys.argv[1]
        PASSWORD = sys.argv[2]
        session.get(web)
        csrftoken=session.cookies['csrftoken']
        login_data = dict(csrfmiddlewaretoken=csrftoken, username=USERNAME, password=PASSWORD, next='/')
        session.post(url, data=login_data, headers={"Referer": "URL"})
        page = session.get('URL')
        #print page.content





        soup = BeautifulSoup(page.content,"lxml")
        for j in soup.find_all('a'):
         res = (j.get('href'))
         if res not in link:
          link.append(res)

        def craw(rest):
         page1 = session.get(rest)
         soup1 = BeautifulSoup(page1.content,"lxml")
         for sec_flag in soup1.findAll('h2',{'class','secret_flag'}):
          flags.append(sec_flag.string)
         for j in soup1.find_all('a'):
          res = (j.get('href'))
          if res not in link:
                #print res
                link.append(res)

        for k in link:
          rest = k
          
           si = "URL" + rest
           craw(si)
          #print rest
        print flags
