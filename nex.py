import argparse
from categories import tools

def main():
    parser = argparse.ArgumentParser(
        prog="nex",
        description="🧠 NexTerm v1.1 - Smart Terminal Assistant",
    )

    parser.add_argument("command", help="Tool to run (e.g., ip, hostname, info, speedtest, ipv6)")
    args = parser.parse_args()

    cmd = args.command.lower()

    if cmd == "ip":
        tools.show_ip()
    elif cmd == "hostname":
        tools.show_hostname()
    elif cmd == "info":
        tools.system__info()
    elif cmd == "speedtest":
        tools.run_speedtest()
    elif cmd == "ipv6":
        tools.get_public_ip()
    else:
        print("❌ Unknown command.")
if __name__ == "__main__":
    main()