#!/usr/bin/env python3

import os
import sys
import platform
import subprocess
import requests
import psutil
import datetime
import time
import random
import string
import socket
import threading
import speedtest
import winsound  # Windows sound module
from rich.console import Console
from rich.text import Text
from art import text2art  # ASCII art module

console = Console()

APP_PATHS = {
    "spotify": "C:\\Users\\Public\\Spotify.exe",
    "notepad": "C:\\Windows\\System32\\notepad.exe",
    "calc": "C:\\Windows\\System32\\calc.exe"
}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = Text("""
  ███╗   ██╗███████╗██╗  ██╗
  ████╗  ██║██╔════╝╚██╗██╔╝
  ██╔██╗ ██║█████╗   ╚███╔╝ 
  ██║╚██╗██║██╔══╝   ██╔██╗ 
  ██║ ╚████║███████╗██╔╝ ██╗
  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
    """, style="bold cyan")
    
    console.print(banner)
    console.print("🚀 [bold magenta]Nex CLI v1.2[/bold magenta] - Smart Terminal Assistant\n")

def loading(text, delay=0.1, dots=5):
    console.print(f"{text}", end="", style="bold yellow")
    for _ in range(dots):
        time.sleep(delay)
        console.print(".", end="", style="bold yellow")
    console.print("\n")

def get_ip():
    try:
        loading("Fetching your public IP")
        ip = requests.get("https://api64.ipify.org").text
        console.print(f"🌍 Your Public IP: [bold cyan]{ip}[/bold cyan]")
    except Exception:
        console.print("[red]⚠ Error fetching IP.[/red]")

def get_system_info():
    loading("Gathering system info")
    info = {
        "🖥 OS": platform.system(),
        "🔢 Version": platform.version(),
        "📅 Release": platform.release(),
        "💻 Machine": platform.machine(),
        "⚙ Processor": platform.processor(),
        "🛑 RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "⏳ Uptime": get_uptime()
    }
    for k, v in info.items():
        console.print(f"{k}: [bold cyan]{v}[/bold cyan]")

def get_uptime():
    uptime_seconds = int(time.time() - psutil.boot_time())
    uptime = datetime.timedelta(seconds=uptime_seconds)
    return str(uptime).split('.')[0]

def get_hostname():
    hostname = socket.gethostname()
    console.print(f"🏠 Hostname: [bold cyan]{hostname}[/bold cyan]")

def system_sleep():
    console.print("😴 Putting system to sleep...")
    if platform.system() == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
    else:
        os.system("systemctl suspend")

def system_shutdown():
    console.print("🔌 Shutting down system...")
    if platform.system() == "Windows":
        os.system("shutdown /s /t 0")
    else:
        os.system("shutdown now")

def open_application(app):
    if app in APP_PATHS:
        console.print(f"🚀 Opening {app}...")
        os.startfile(APP_PATHS[app])
    else:
        console.print("[red]❌ Application not found![/red]")

def run_speedtest():
    console.print("🚀 Running speed test...")
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000
        console.print(f"📥 Download Speed: [bold cyan]{download_speed:.2f} Mbps[/bold cyan]")
        console.print(f"📤 Upload Speed: [bold cyan]{upload_speed:.2f} Mbps[/bold cyan]")
    except Exception as e:
        console.print(f"[red]⚠ Error running speed test: {e}[/red]")

def reminder(task, seconds):
    time.sleep(seconds)
    console.print(f"[bold yellow]🔔 Reminder:[/bold yellow] {task}")
    winsound.MessageBeep()

def set_reminder(task, time_value):
    time_unit = time_value[-1]
    time_amount = int(time_value[:-1])
    seconds = time_amount * 60 if time_unit == 'm' else time_amount * 3600
    console.print(f"⏰ Reminder set for '{task}' in {time_amount} {'minutes' if time_unit == 'm' else 'hours'}.")
    threading.Thread(target=reminder, args=(task, seconds), daemon=True).start()

def fetch_joke():
    try:
        joke = requests.get("https://v2.jokeapi.dev/joke/Any?format=txt").text
        console.print(f"🤣 Random Joke: [bold cyan]{joke}[/bold cyan]")
    except Exception:
        console.print("[red]⚠ Error fetching joke.[/red]")

def fetch_quote():
    try:
        quote = requests.get("https://programming-quotes-api.herokuapp.com/quotes/random").json()
        console.print(f"💡 Dev Quote: [bold cyan]{quote['en']} - {quote['author']}[/bold cyan]")
    except Exception:
        console.print("[red]⚠ Error fetching quote.[/red]")

def main():
    clear_console()
    print_banner()
    
    if len(sys.argv) < 2:
        console.print("[red]❌ Usage: nex <command> [arguments][/red]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "info":
        get_system_info()
    elif command == "ip":
        get_ip()
    elif command == "hostname":
        get_hostname()
    elif command == "sleep":
        system_sleep()
    elif command == "shut":
        system_shutdown()
    elif command == "open" and args:
        open_application(args[0])
    elif command == "speedtest":
        run_speedtest()
    elif command == "rm" and len(args) == 2:
        set_reminder(args[0], args[1])
    elif command == "joke":
        fetch_joke()
    elif command == "quote":
        fetch_quote()
    else:
        console.print("[red]❌ Unknown command! Try:[/red] info, ip, hostname, sleep, shut, open <app>, speedtest, rm <task> <time>, joke, quote.")

if __name__ == "__main__":
    main()
