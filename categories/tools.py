import socket
import platform
import speedtest

# ipv4 default
def show_ip():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"🌐 IP Address: {ip_address}")
    except Exception as e:
        print("❌ Error getting IP:", e)

def show_hostname():
    hostname = socket.gethostname()
    print(f"🖥️  Hostname: {hostname}")

# fetch sys info
def system__info():
    print("🛠️ System Info:")
    print(f"OS: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

# IPV6
def get_public_ip():
    import urllib.request
    try:
        external_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
        print(f"🌍 Public IP Address: {external_ip}")
    except Exception as e:
        print("❌ Error fetching public IP:", e)

# run speed test
def run_speedtest():
    print("🚀 Running speed test. Please wait...")
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000
        ping = st.results.ping

        print(f"📥 Download Speed: {download_speed:.2f} Mbps")
        print(f"📤 Upload Speed: {upload_speed:.2f} Mbps")
        print(f"🏓 Ping: {ping:.0f} ms")
    except Exception as e:
        print("❌ Speed test failed:", e)