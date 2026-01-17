#include "fastConnect.h"

int fastConnect(const char *ip, int port, float timeout){
    int sock;
    struct sockaddr_in server;

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if(sock == -1) return 0;

    int flags = fcntl(sock, F_GETFL, 0);
    fcntl(sock, F_SETFL, flags | O_NONBLOCK);

    memset(&server, 0, sizeof(server));
    server.sin_family = AF_INET;
    server.sin_port = htons(port);

    if(inet_pton(AF_INET, ip, &server.sin_addr) <= 0){
        close(sock);
        return 0;
    }

    int result = connect(sock, (struct sockaddr *)&server, sizeof(server));

    if(result < 0){
        if(errno == EINPROGRESS){
            fd_set fdset;
            struct timeval tv;
            FD_ZERO(&fdset);
            FD_SET(sock, &fdset);
            tv.tv_sec = (long)timeout;
            tv.tv_usec = (long)((timeout - tv.tv_sec) * 1000000);

            if(select(sock + 1, NULL, &fdset, NULL, &tv) > 0){
                int error = 0;
                socklen_t len = sizeof(error);
                getsockopt(sock, SOL_SOCKET, SO_ERROR, &error, &len);
                close(sock);
                return (error == 0) ? 1 : 0;
            } else{
                close(sock);
                return 0;
            }
        } else{
            close(sock);
            return 0;
        }
    }

    close(sock);
    return 1;
}
