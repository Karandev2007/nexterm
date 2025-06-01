import argparse
from categories import tools, fun, ai, game

def main():
    parser = argparse.ArgumentParser(
        prog="nex",
        description="🧠 NexTerm v1.1 - Smart Terminal Assistant",
    )

    parser.add_argument("command", help="Tool to run (e.g., ip, hostname, info, speedtest, ipv6, wifi-pass, genpass, joke, ask, ipinfo, game, currency, weather)")
    parser.add_argument("extra", nargs="*", help="Optional extra input")

    args = parser.parse_args()
    cmd = args.command.lower()
    extra = args.extra

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
    elif cmd == "ipinfo":
        if extra:
            tools.ip_info(extra[0])
        else:
            print("❌ Usage: nex ipinfo <ip-address>")
    elif cmd == "joke":
        fun.joke()
    elif cmd == "ask":
        if extra:
            question = " ".join(extra)
            ai.ask(question)
        else:
            print("❌ Usage: nex ask \"your question here\"")
    elif cmd == "game":
        game.start_game()
    elif cmd == "currency":
        if len(extra) == 3:
            amount, from_currency, to_currency = extra
            tools.convert_currency(amount, from_currency, to_currency)
        else:
            print("❌ Usage: nex currency <amount> <from_currency> <to_currency>")
    elif cmd == "weather":
        if extra:
            city = " ".join(extra)
            tools.get_weather(city)
        else:
            print("❌ Usage: nex weather <city>")
    else:
        print("❌ Unknown command.")

if __name__ == "__main__":
    main()
