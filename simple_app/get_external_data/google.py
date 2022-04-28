from urllib import request

req = request.urlopen('http://www.google.com')


print(req.getcode())
print(req.read())