from lib2to3.pgen2 import token
from msilib.schema import FeatureComponents
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f= Fernet(key)
token = f.encrypt(b"hola")
print(token)
token = f.decrypt(token)
print(token)