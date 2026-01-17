#!/usr/bin/env python3

import ipaddress, random
from typing import NewType

class ipGen:
    def __init__(self, ranges):
        self.networks = [ipaddress.IPv4Network(r) for r in list(set(ranges))]
        self.pendingRanges = set()

    def genInitial(self, count):
        targets = set()
        while len(targets) < count:
            net = random.choice(self.networks)
            #offset = random.randint(1, min(65536, net.num_addresses - 10))
            offset = random.randint(1, net.num_addresses - 2) # evit trash
            ip = str(net.network_address + offset)
            #if not ipaddress.ip_address(ip).is_private:
            ipObjs = ipaddress.ip_address(ip)
            if ipObjs.is_global: # filter lookups, privates, multicast, etc [best to is.private think]
                targets.add(ip)
        return list(targets)

    def genFromRanges(self):
        newIps = []
        for _ in range(500):
            if not self.pendingRanges:
                break
            cidr = self.pendingRanges.pop()
            try:
                net = ipaddress.IPv4Network(cidr, strict=False)
                #for ip in random.sample(list(net.hosts()), min(200, net.num_addresses - 2)):

                # not gen lists extensas, less use ram, more speed in big redes
                for _ in range(min(200, net.num_addresses - 2)):
                    offset = random.randint(1, net.num_addresses - 2)
                    ip = net.network_address + offset
                    newIps.append(str(ip))
            except ValueError:
                pass

        random.shuffle(newIps)
        return newIps

    def addHostRange(self, ipStr):
        base = ".".join(ipStr.split(".")[:3]) + ".0/24"
        if base not in self.pendingRanges:
            self.pendingRanges.add(base)
