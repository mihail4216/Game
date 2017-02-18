# -*- coding: utf-8 -*-

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
# import bs4 as bs
# import urllib2
# qwe=('А Б В Г Д Е Ж З И К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Э Ю')
# q=qwe.split()
#
# # for i in qwe:
# sas = urllib2.urlopen('http://www.ruslo.net/index.php/list/19-vse-suschestvitel-nye-russkogo-yazyka/,'+'А'+'.xhtml')
# soup = bs.BeautifulSoup(sas,'lxml')
# a = soup.find_all('td')
# print a
#
#

#################################################
def dicture():
    f = open('word_rus.txt','r')
    q=f.read()
    a=q.split()
    f.close()
    return a


