import  hashlib


password='123456'
md5 = hashlib.md5()
md5.update(password.encode('utf-8'))

password=md5.hexdigest()
print(password)