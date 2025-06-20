from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes 
import sys


target_file = sys.argv[1]
pub_key = input("enter the public key file path:\n")


def main():
	symmetricKey = Fernet.generate_key()
	fernet = Fernet(symmetricKey)

	with open(pub_key, "rb") as key_file:
		public_key = serialization.load_pem_public_key(
			key_file.read(),
			backend=default_backend()
			)

	encryptedSymmetricKey = public_key.encrypt(
		symmetricKey,
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA256(),
			label=None
			)
		)

	file_path = target_file
	with open(file_path, "rb") as file:
		file_data=file.read()
		encrypted_data=fernet.encrypt(file_data)
	with open(file_path, "wb") as file:
		file.write(encrypted_data)

	quit()


main()
