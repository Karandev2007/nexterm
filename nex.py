import argparse
from categories import tools, fun, ai

def main():
    parser = argparse.ArgumentParser(
        prog="nex",
        description="🧠 NexTerm v1.1 - Smart Terminal Assistant",
    )

    parser.add_argument("command", help="Tool to run (e.g., ip, hostname, info, speedtest, ipv6, wifi-pass, genpass, joke, ask)")
    parser.add_argument("extra", nargs="*", help="Optional extra input")

    args = parser.parse_args()
    cmd = args.command.lower()
    extra = " ".join(args.extra)

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
    elif cmd == "wifi-pass":
        tools.wifi_pass()
    elif cmd == "genpass":
        tools.generate_password()
    elif cmd == "joke":
        fun.joke()
    elif cmd == "ask":
        if extra:
            ai.ask(extra)
        else:
            print("❌ Usage: nex ask \"your question here\"")
    else:
        print("❌ Unknown command.")

if __name__ == "__main__":
    main()