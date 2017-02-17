import urllib2

while True:
    k=192
    while k<=223:
        sas = urllib2.urlopen('http://slovardalja.net/letter.php?charkod='+str(k))