import socket

phttp = {80,81,82,8080,8000,8081,8888,8443,9090,8880,8181}

class BannerGrabber:
    def grabBanner(self, ip, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.2)
            s.connect((ip, port))

            if port in phttp:
                s.send(b"GET / HTTP/1.0\r\n"
                       b"Host: " + ip.encode() + b"\r\n"
                       b"User-Agent: Mozilla/5.0\r\n\r\n"
                )
            elif port == 554:
                s.send(
                    b"OPTIONS rtsp://" + ip.encode() + b":554 RTSP/1.0\r\n"
                    b"CSeq: 1\r\nUser-Agent: LibVLC/3.0\r\n\r\n"
                )
            elif port in (21, 22, 23):
                pass
            else:
                s.send(b"\r\n")

            data = b""
            for _ in range(2):
                try:
                    data += s.recv(512)
                except socket.timeout:
                    break
            banner = data.decode("utf-8", errors="ignore").strip()
            s.close()

            if banner:
                banner = banner.replace("\r\n", " ").replace("\n", " ")[:80]
            return banner
        except (socket.timeout, socket.error):
            return ""
