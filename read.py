import json,urllib
data=urllib.urlopen("http://subhrockzz.pythonanywhere.com/").read()
output=json.loads(data)
print(output)
