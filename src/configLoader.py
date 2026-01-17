#!/usr/bin/env python3

import json
from pathlib import Path
from typing import List, Dict

class configLoad:
    def __init__(self, configDir: str = "config"):
        self.configPath = Path(configDir)
    def loadPorts(self) -> List[int]:
        # see ports.txt: [23, 80, 88]
        ports = []
        portsFile = self.configPath / "ports.txt"

        with open(portsFile, 'r') as f:
            for line in f:
                line = line.split('#')[0].strip()
                if line.isdigit():
                    ports.append(int(line))
        return ports

    def loadRanges(self) -> List[str]:
        ranges = []
        rangesFile = self.configPath / "ranges.txt"

        with open(rangesFile, 'r') as f:
            for line in f:
                line = line.split('#')[0].strip()
                if '/' in line:
                    ranges.append(line)
        return ranges

    def loadServices(self) -> Dict[int, str]:
        services = []
        servicesFile = self.configPath / "services.json"

        with open(servicesFile, 'r') as f:
            data = json.load(f) # convert claves str to int
            return {int(k): v for k, v in data.items()}




































