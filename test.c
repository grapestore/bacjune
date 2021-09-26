/* Master version
 * 15213 2013 Fall
 * Proxy Lab
 * Name: Enze Li
 * Andrew id: enzel
 * ----------------------
 * 
 *
 *
 */

#include <stdio.h>
#include "csapp.h"

/* Recommended max cache and object sizes */
#define MAX_CACHE_SIZE 1049000
#define MAX_OBJECT_SIZE 102400
#define LRU_MAGIC_NUMBER 9999
#define CACHE_OBJS_COUNT 10

#define DEFAULT_PORT 80

/* You won't lose style points for including these long lines in your code */
static const char *user_agent = "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:10.0.3) Gecko/20120305 Firefox/10.0.3\r\n";
static const char *accept_ = "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n";
static const char *accept_encoding = "Accept-Encoding: gzip, deflate\r\n";
static const char *connection = "Cnnection: close\r\n";
static const char *proxy_connection = "Proxy-connection: close\r\n";

void *proxy_thread(void *vargp);
void doit(int cliendfd);
// void write_requesthdrs(rio_t *rp, char *newreq);
void write_requesthdrs(char *newreq, char *host);
int parse_uri(char *uri, char *host, char *file);
void clienterror(int fd, char *cause, char *errnum, 
         char *shortmsg, char *longmsg);

int main(int argc, char **argv)
{
    int listenfd, *connfdp, port;
    socklen_t clientlen;
    struct sockaddr_in clientaddr;
    pthread_t tid;    

    if (argc != 2){
    	fprintf(stderr, "Proxy usage: %s <port>\n", argv[0]);
    }

    /* Ignore broken pipe) */
    Signal(SIGPIPE, SIG_IGN);

    /* parse port */
    port = atoi(argv[1]);

    /* listen for connection */
    if ((listenfd = Open_listenfd(port)) < 0) {
        fprintf(stderr, "Open_listenfd error: %s\n", strerror(errno));
        return 0;
    }

    while (1) {
    	clientlen = sizeof(clientaddr);
      

        connfdp = Malloc(sizeof(int));
        *connfdp = Accept(listenfd, (SA *)&clientaddr, &clientlen);
        Pthread_create(&tid, NULL, proxy_thread, connfdp);

    }


    return 0;
}

/*
 * proxy_thread - proxy multi threading
 */
 
void *proxy_thread(void *vargp) {
    int connfd = *((int *)vargp);
    // 다른 쓰레드들과 분리하기 위해 detach
    Pthread_detach(pthread_self());
    // connect malloc 저장한거 free 해줘야됨
    // 왜냐하면 특정한 경우에 순서가 꼬이면서 동적할당을 안하고 같은 변수를 이용하여 쓰레드가 connfd socket을 공유해버리는 경우가 생긴다
    Free(vargp);
    // 쓰레드가 실행할 함수
    doit(connfd);
    // 끝나고 socket close
    Close(connfd);
    return NULL;
}


/*
 * proxy - handle the proxy operations for a client 
 * 1. Get HTTP request and header information from client
 * 2. Forward the request and header information to the server
 * 3. Get response from server and forward it back to client
 */
void doit(int cliendfd)
{
	int hostport, serverfd;
	char buf[MAXLINE], method[MAXLINE], uri[MAXLINE], version[MAXLINE];
    char host[MAXLINE], file[MAXLINE], newreq[MAXLINE], response[MAXLINE];
	rio_t client_rio, server_rio;
    size_t n;

	/* get request for client */
  // read ready -> read -> sscanf set method uri version(header)
    rio_readinitb(&client_rio, cliendfd);
    if (rio_readlineb(&client_rio, buf, MAXLINE) < 0) {
        fprintf(stderr, "Error reading from client.");
        return;
    }

    if (sscanf(buf, "%s %s %s", method, uri, version) != 3) {
        fprintf(stderr, "HTTP request error.");
        return;
    }
  // 서버에 저장된 method만 요구했는지 check
    if (strcasecmp(method, "GET") != 0) {
        clienterror(cliendfd, method, "501", "Not Implemented",
                "Proxy only supports GET method");
        return;
    }

    /* write up the new http request */
    hostport = parse_uri(uri, host, file);
    sprintf(newreq, "GET %s HTTP/1.0\r\n", file);
    // write_requesthdrs(&client_rio, newreq);
    // newreq에 host header 정보 쌓아줌
    write_requesthdrs(newreq, host); 
    // printf("The request sent to sever is:\n%s\n", newreq);


    /* Forward the request to the server */
    // 서버와 연결해주기 위해 proxy(client) <-----> tiny(server)  client socket 준비 및 connect 시도
    if ((serverfd = Open_clientfd(host, hostport)) == -1){
        printf("Cannot connect to web server.\n");
        // 연결 안됐으니까 client에게 보내줘야됨
    	clienterror(cliendfd, host, "400", "Bad Request",
                    "The host name or port number maybe invalid");
        return;
    }
    // client로 부터 받은 header 정보를 tiny web server로 보내줌
    rio_writen(serverfd, newreq, strlen(newreq));

    /* Forward response from server to client */
    // tiny 서버로부터 read 준비
    rio_readinitb(&server_rio, serverfd);

    // tiny server로부터 받은 response를 그대로 다시 client한테 보내준다
    while ((n = rio_readlineb(&server_rio, response, MAXLINE)) > 0){
        rio_writen(cliendfd, response, n);
    }
// 이번 쓰레드가 생성한 server socket은 여기서 닫아주며 conn socket은 thread 함수에서 열렸으므로 거기서 닫아줌
    Close(serverfd);
}


/*
 * write_requesthdrs - write required HTTP request headers
 */

void write_requesthdrs(char *newreq, char *host) 
{
    sprintf(newreq, "%sHost: %s\r\n",newreq, host);
    sprintf(newreq, "%s%s", newreq, user_agent);
    sprintf(newreq, "%s%s", newreq, accept_);
    sprintf(newreq, "%s%s", newreq, accept_encoding);
    sprintf(newreq, "%s%s", newreq, connection);
    sprintf(newreq, "%s%s\r\n", newreq, proxy_connection);
    return;
}

/*
 * parse_uri - get host, file path from uri
 *        return port if specified, else return 80
 */
int parse_uri(char *uri, char *host, char *file) 
{
    int port;
    char buf[MAXLINE];
/*sscanf는 [ ]대괄호 안에 값을 넣어 읽을 문자열을 선택적으로 문자열에 저장하는 기능도 제공한다.*/
    sscanf(uri, "%*[^:]://%[^/]%s", host, file);
    if (strstr(host, ":")) {
        strcpy(buf, host);
        sscanf(buf, "%[^:]:%d", host, &port);
        return port;
    }

    return DEFAULT_PORT;
}

/*
 * clienterror - returns an error message to the client
 */
void clienterror(int fd, char *cause, char *errnum, 
		 char *shortmsg, char *longmsg) 
{
    char buf[MAXLINE], body[MAXBUF];

    /* Build the HTTP response body */
    sprintf(body, "<html><title>Tiny Error</title>");
    sprintf(body, "%s<body bgcolor=""ffffff"">\r\n", body);
    sprintf(body, "%s%s: %s\r\n", body, errnum, shortmsg);
    sprintf(body, "%s<p>%s: %s\r\n", body, longmsg, cause);
    sprintf(body, "%s<hr><em>The Tiny Web server</em>\r\n", body);

    /* Print the HTTP response */
    sprintf(buf, "HTTP/1.0 %s %s\r\n", errnum, shortmsg);
    Rio_writen(fd, buf, strlen(buf));
    sprintf(buf, "Content-type: text/html\r\n");
    Rio_writen(fd, buf, strlen(buf));
    sprintf(buf, "Content-length: %d\r\n\r\n", (int)strlen(body));
    Rio_writen(fd, buf, strlen(buf));
    Rio_writen(fd, body, strlen(body));
}