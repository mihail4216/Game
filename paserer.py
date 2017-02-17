

################################################
# import bs4 as bs
# import urllib2
# dicture = set()
# list1=str()
# k=192
# while k<=223:
#     sas = urllib2.urlopen('http://slovardalja.net/letter.php?charkod='+str(k))
#     soup = bs.BeautifulSoup(sas,'lxml')
#     a=soup.find_all('table')[4]
#     a=a.find_all('strong')
#     for i in a:
#         # i=unicode(i.text,'unicode-escape')
#         i=i.string
#         list1=list1+' ' + i
#
#     k+=1
#
#
# print list1
##############################################
def dicture():
    f = open('text.txt','r')
    q=f.read()
    a=q.split()
    return a