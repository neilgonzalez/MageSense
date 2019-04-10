import urllib2
import sys
from bs4 import BeautifulSoup

xmrWords = ["cyberpanel-xmrig",
            "xmrig",
            "cryptonight",
            "xmr-stak-cpu",
            "pool.minexmr.com",
            "https://pastebin.com/raw/HJLMF7Es"]

count = 0
def usage():
    print "usage: python StrikeSense.py <baseurl> --checkout <checkouturl>"
if len(sys.argv) <=  1:
    usage()

#def spider_checkout_dir()

def find_base_url():
    #change this in future updates
    try:
        if sys.argv[1] == '--checkout':
            #when no base url is passedoinhive_finder(find_base_url())
            return 0
    except:
        usage()
    return sys.argv[1]

#looks for docker containers infected with miners
def compromised_docker(url): 
init_page = base_url
    try:
        page= urllib2.urlopen(init_page)
    
    except urllib2.HTTPError, e:
       raise ValueError(str(e.code) + ' ' + str(e.reason))
    except urllib2.URLError, e:
       raise ValueError(str(e.code) + ' ' + str(e.reason))
    except httplib.HTTPException, e:
       raise ValueError(str(e.code) + ' ' + str(e.reason))

    soup = BeautifulSoup(page, 'html.parser')
    for x in xmrWords:
        if soup.find(x):
            print("Docker miner found\n")
            print(soup.find(x).text.strip())
   
    except:
        print("no coinhive miner found...\n")

#looks for coinhive javascript injections
def coinhive_finder(base_url):
    init_page = base_url
    try:
        page= urllib2.urlopen(init_page)
    
    except urllib2.HTTPError, e:
       raise ValueError(str(e.code) + ' ' + str(e.reason))
    except urllib2.URLError, e:
       raise ValueError(str(e.code) + ' ' + str(e.reason))
    except httplib.HTTPException, e:
       raise ValueError(str(e.code) + ' ' + str(e.reason))

    soup = BeautifulSoup(page, 'html.parser')
    coinhive = soup.find('script', attrs={'src': 'https://coinhive.com/lib/coinhive.min.js'})
    try:
        coinhive = coinhive.text.strip()
    except:
        print("no coinhive miner found...\n")

#parse arguments for to initiate page cart search
def parse_args_checkout():
    global count
    for x in sys.argv:
        
        if x == "--checkout":
            count+=1
            checkoutUrl = sys.argv[count]
            return checkoutUrl
        count+=1
    return 0

#injection into the page itself
def find_opcodes():
    #look for javascript miners instead of cart attacks
    if parse_args_checkout() == 0 and find_base_url() != 0:
        coinhive_finder(find_base_url())
    checkout = parse_args_checkout()
    page = urllib2.urlopen(checkout)
    html = BeautifulSoup(page, 'html.parser')
    ops = soup.find('\\x')
    try:
        ops = ops.text.strip()
    except:
        print("no opcodes found...\n")

find_opcodes()