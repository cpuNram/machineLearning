import ssl
import urllib
from bs4 import BeautifulSoup

def lookupAbstract(name):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    arxivURL = "https://arxiv.org//find/grp_eess,grp_cs,grp_econ,grp_math/1/au:+" + name + "/0/1/0/all/0/1?per_page=1000"
    #print arxivURL
    sock = urllib.urlopen(arxivURL, context=ctx)
    htmlSource = sock.read()
    sock.close()
    soup = BeautifulSoup(htmlSource, 'html.parser')
    for line in soup.select('div.list-title span.descriptor'):
        print line.nextSibling.strip()


def scapeName():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    sock = urllib.urlopen("https://www.eecs.mit.edu/people/faculty-advisors", context=ctx)
    htmlSource = sock.read()
    sock.close()
    soup = BeautifulSoup(htmlSource, 'html.parser')
    for line in soup.select('div.views-field.,span.field-content.card-title'):
        if line.find('a'):
            profName =line.find('a').text.encode('utf-8')
            My = profName.split( )
            if len(My) > 1:
                firstName = My[0]
                secondName = My[1]
                if My[0][len(My[0])-1] == '.':
                    firstName = My[0][:len(My[0])-1]
                if My[1][len(My[1])-1] == '.':
                    secondName = My[1][:len(My[1])-1]
                lookupAbstract(secondName+'_'+firstName)

scapeName()
