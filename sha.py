import hashlib

def digest(string):
    result = hashlib.sha1(string.encode())
    return result.hexdigest()
