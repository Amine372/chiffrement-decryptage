import hashlib
m = hashlib.md5()
m.update("Nobody inspects")
m.digest()
