import webbrowser
stdurl = "https://www.google.co.in/maps/place/"
addarr = raw_input("Enter the name of the place: ").split(' ')

furl = stdurl
for i in range(0,len(addarr)):
	if (i!=len(addarr)-1):
		furl = furl + addarr[i] + '+'
	else:
		furl = furl + addarr[i]

print furl
webbrowser.open(furl)