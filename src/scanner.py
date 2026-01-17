import socket, ctypes
from concurrent.futures import ThreadPoolExecutor, as_completed

class scanner:
    def __init__(self, ports, timeout=1.3, workers=300, services=None):
        self.ports = ports
        self.timeout = timeout
        self.workers = workers
        self.services = services or {}
        self.found = 0
        self.scanned = 0

        try:
            self.c_lib = ctypes.CDLL('./lib/fastConnect.so')
            self.c_lib.fastConnect.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_float]
            self.c_lib.fastConnect.restype = ctypes.c_int
            self.use_c = True
        except:
            self.use_c = False

    def fastConnect(self, ip, port):
        if self.use_c:
            return self.c_lib.fastConnect(ip.encode('utf-8'), port, ctypes.c_float(self.timeout)) == 1
        else:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(self.timeout)
                result = s.connect_ex((ip, port))
                s.close()
                return result == 0
            except:
                return False

    def getServiceName(self, port):
        return self.services.get(port, "Unknown")

    def scanIp(self, ipStr):
        openPorts = []
        priority = [23, 80, 81, 554, 8080, 8000, 37777]

        for p in priority:
            if p in self.ports and self.fastConnect(ipStr, p):
                openPorts.append(p)

        if openPorts:
            for p in [x for x in self.ports if x not in priority]:
                if self.fastConnect(ipStr, p):
                    openPorts.append(p)
            return (ipStr, sorted(openPorts))
        return None

    def scanBatch(self, ips):
        results = []
        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = {executor.submit(self.scanIp, ip): ip for ip in ips}
            for future in as_completed(futures):
                self.scanned += 1
                result = future.result()
                if result:
                    results.append(result)
                    self.found += 1
        return results










