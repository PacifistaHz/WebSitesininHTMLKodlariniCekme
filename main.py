import urllib.request

URL=input("Enter the URL of the website: ")
html = urllib.request.urlopen(URL)
htmlText = str(html.read())
f=open("html_metin.txt","w")
f.write(htmlText)
f.close()