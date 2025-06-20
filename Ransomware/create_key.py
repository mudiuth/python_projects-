from cryptography.hazmat.primitives.asymmetric import rsa 
from cryptography.hazmat.primitives import serialization

#generating the private key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
passphrase = b"Yasuth18"
#save private key
with open("private_key.pem", "wb") as f:
	f.write(
		private_key.private_bytes(
			encoding=serialization.Encoding.PEM,
			format=serialization.PrivateFormat.TraditionalOpenSSL,
			encryption_algorithm=serialization.BestAvailableEncryption(passphrase)
			)
		)

# xtract the public key and save it 
public_key = private_key.public_key()
with open("public_key.key", "wb") as f:
	f.write(
		public_key.public_bytes(
			encoding=serialization.Encoding.PEM,
			format=serialization.PublicFormat.SubjectPublicKeyInfo
			)
		)
