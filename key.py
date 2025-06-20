from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def main():
	# step1 load the privatekey.pem file 
	private = input ("Enter the path to the private key file: \n")
	password = input("Enter the password to the private key: \n").encode()
	with open(private, "rb") as key_file:
		private_key = serialization.load_pem_private_key(
			key_file.read(),
			password = password,
			backend = default_backend()
			)

	#step2 load the encryptedSemmetric file
	symmetric = input("Enter the path to the symmetric key:\n")
	with open(symmetric, "rb") as key_file:
		encrypted_symmetric_key = key_file.read()

	#step3 decrypt the symmetric key using the private key
	symmetric_key = private_key.decrypt(
		encrypted_symmetric_key,
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA256(),
			label=None
			)
		)

	#step 4 use the decrypted key to decrypt the content of the encrypted file
	file_path = input("Enter the path to the file u want to decrypt:\n")
	with open(file_path, "rb") as file:
		encrypted_data = file.read()
	fernet = Fernet(symmetric_key)
	decrypted_data = fernet.decrypt(encrypted_data)

	#step5 load the decrypted data back to the target file
	with open(file_path, "wb") as file:
		file.write(decrypted_data)

	print(f"the data that was decrypted is {decrypted_data}")
	print("[*]Decryption completed successfuly")

if __name__ =="__main__":
	main()