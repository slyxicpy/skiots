#!/usr/bin/env python3

import time, argparse
from datetime import datetime

from src.configLoader import configLoad
from src.ipGen import ipGen
from src.scanner import scanner
from src.bannerGrabber import BannerGrabber
from src.fileSaver import fileSaver

RS = "\033[0m"
WHITE = "\033[1;97m"
CYAN = "\033[38;5;37m"
B_RED = "\033[38;5;196m"
N_CYAN = "\033[38;5;51m"
N_RED = "\033[38;5;9m"
GRAY = "\033[38;5;244m"
BLUE = "\033[1;34m"
PURPLE = "\033[38;5;141m"


def banner():
    print(f"""
{PURPLE}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠇⣿⠟⠻⢿⣿⠿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡗⠀⠀⠀⠀⠀⣿⣿⡿⢏⣞⠁⠀⠀⢸⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⠀⠹⣧⠚⠻⣿⣧⣴⣶⠋⠉⣶⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢐⢀⡀⠀⠀⠀⠀⠀⠙⠐⣶⡆⠀⢹⣿⣶⣶⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢫⡇⠾⢸⡇⡇⠀⠀⠀⠀⠀⠀⣿⣿⣄⣀⣀⣈⣈⠀⠀⠀⠀⠀⠀⠀⢀⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡜⠇⡇⡸⢰⠇⠀⠀⠀⠀⠀⠀⠀⣉⣛⣛⠻⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀⠶⣍⡑⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡀⠠⠀⠃⠀⠀⠀⠀⠀⠀⠀⣐⣒⣚⡙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡶⠀⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⢠⣥⢀⣀⠀⠀⠀⢀⠄⠀⣚⠛⠉⢉⡀⠒⠤⡀⠀⠀⠀⠀⠀⠀⠈⠉⢰⣿⠹⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣿⢁⠈⣩⣭⢩⡀⠀⢀⣠⣤⣤⠶⢠⣤⣦⡐⣂⡀⠡⣦⢠⣤⣥⡀⠀⢀⣍⣀⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⡇⡿⢡⠈⠷⣄⡀⠉⠉⠉⠁⠈⠻⣿⠃⠈⠀⢀⠀⡘⢿⣿⠃⠀⠈⠻⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡟⢰⠇⠈⢧⣀⠈⠉⠛⠛⠛⠛⢋⡀⢻⣧⠀⠀⠉⢀⡹⠌⢻⣧⠀⠀⢸⡎⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡏⠁⠈⠀⢦⡀⠉⠛⠷⠶⠶⠶⠞⠋⠁⠻⣿⡆⠉⠒⠚⠀⡀⠀⠹⣷⡀⠸⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠐⣌⠛⢶⣤⣄⣀⣀⣀⣀⣤⠞⠀⢿⣧⠑⠦⠤⠴⠃⠀⠀⠙⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣤⣈⠉⠛⠛⠋⠉⣀⣤⠞⢸⣧⠑⢄⡀⠀⢀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⠿⠿⠛⠋⠁⠀⠀⠉⠀⠀⠈⠉⠉⠀
{RS}
{WHITE}      Version{RS}{GRAY} ::{RS} {CYAN}0.69{RS}  {WHITE}DateUp{RS} {GRAY}::{RS} {CYAN}17/01/26 02:36am{RS}
{WHITE}      Author{RS}{GRAY}  ::{RS} {BLUE}https://github.com/slyxicpy{RS}
{WHITE}      Desc{RS} {GRAY}   ::{RS} {WHITE}{GRAY}This program is designed for parsing/searching for active hosts
                 specifically focused on IoT devices exposed to the net.
                 This version is being developed with a focus on scan speed
                 The author is not responsible for the use.{RS}{GRAY} ::{RS} {B_RED}{datetime.now().date()}{RS}
""")

def main():
    parser = argparse.ArgumentParser(description=f"""This is a search engine for active hosts
    Especially focused on IoT devices :: Version: 0.69 :: {datetime.now().date()}""")
    parser.add_argument("-c", "--count", type=int, default=50, help="Counter hosts")
    parser.add_argument("-H", "--hilos", type=int, default=300, help="Counter Threads")
    parser.add_argument("-t", "--timeout", type=float, default=1.3, help="Timeout Scann")
    parser.add_argument("-p", "--port", type=str, default=None, help="Ports specifically")
    parser.add_argument("-o", "--output", type=str, help="File save output")
    parser.add_argument("-i", "--info", action="store_true", help="Name services")
    args = parser.parse_args()

    banner()

    # load config
    config = configLoad()
    ports = config.loadPorts() if not args.port else [int(p.strip()) for p in args.port.split(",")]
    ranges = config.loadRanges()
    services = config.loadServices()

    infoColor = PURPLE if args.info else B_RED
    infoTxt = "ON" if args.info else "OFF"
    print(f"{WHITE}Targets{RS} {GRAY}::{RS} {PURPLE}{args.count}{RS}")
    print(f"{WHITE}Threads{RS} {GRAY}::{RS} {B_RED}{args.hilos}{RS} {WHITE}| Timeout{RS} {GRAY}::{RS} {CYAN}{args.timeout}{RS} {WHITE}| Ports{RS} {GRAY}::{RS} {B_RED}{len(ports)}{RS} {WHITE}| Info{RS} {GRAY}::{RS} {infoColor}{infoTxt}{RS}\n")
    #print(f"{WHITE}Ports{RS} {GRAY}::{RS} {N_CYAN}{ports}{RS}\n\n")

    # ipGen module
    ipgen = ipGen(ranges)
    targets = ipgen.genInitial(8000)

    # scanner module
    scan = scanner(ports, args.timeout, args.hilos, services)
    bannerGrab = BannerGrabber() if args.info else None

    results = []
    startTime = time.time()

    while scan.found < args.count:
        currentBatch = targets[:3000]
        targets = targets[3000:]

        if len(currentBatch) < 2000 and ipgen.pendingRanges:
            extra = ipgen.genFromRanges()
            currentBatch.extend(extra)
            targets.extend(extra)

        if not currentBatch:
            break

        batchResults = scan.scanBatch(currentBatch)

        for ipStr, openPorts in batchResults:
            if args.info:
                portInfo = []
                for p in openPorts:
                    svc = scan.getServiceName(p)
                    bnr = bannerGrab.grabBanner(ipStr, p) if bannerGrab else ""
                    if bnr:
                        portInfo.append(f"{p}/{svc}[{bnr[:40]}]")
                    else:
                        portInfo.append(f"{p}/{svc}")
                print(f"{ipStr:>15} | {' | '.join(portInfo)}")
                results.append(f"{ipStr}|{';'.join(portInfo)}")
            else:
                print(f"{ipStr:>15}:{', '.join(map(str, openPorts))}")
                results.append(f"{ipStr}:{','.join(map(str, openPorts))}")

            ipgen.addHostRange(ipStr)

        if scan.scanned % 1500 == 0:
            elapsed = time.time() - startTime
            rate = scan.scanned / elapsed if elapsed > 0 else 0
            #print(f"[Scanned]:: {scan.scanned} | Found: {scan.found} | Rate: {rate:.0f}/s]")

        if scan.found >= args.count:
            print(f"\n{GRAY}[Scanned] :: {B_RED}{scan.scanned}{RS} {GRAY}| Found's :: {BLUE}{scan.found}{RS} {GRAY}| Rate :: {PURPLE}{rate:.0f}/s]{RS}")
            break

    if args.output:
        saver = fileSaver()
        saver.saverResults(args.output, results, args.info)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nStopped!")
