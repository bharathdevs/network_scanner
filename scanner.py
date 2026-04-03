import socket
import threading
import time


# ──────────────────────────────────────────────
# Core Functions
# ──────────────────────────────────────────────

def scan_port(target, port, lock):
    """
    Attempts to connect to a single port on the target.
    If the port is open, prints the result using a thread lock
    to prevent overlapping output from multiple threads.
    """
    s = socket.socket()

    # Give up after 1 second — prevents hanging on filtered ports
    s.settimeout(1)

    try:
        result = s.connect_ex((target, port))

        if result == 0:
            # Lock ensures only one thread prints at a time
            with lock:
                print(f"  [+] Port {port:<5} is OPEN")
    finally:
        # Always close the socket regardless of outcome
        s.close()


def scan_range(target, start_port, end_port):
    """
    Scans a range of ports on the target using threading.
    Each port gets its own thread so they run simultaneously
    instead of one at a time — dramatically faster than sequential scanning.
    """
    lock = threading.Lock()
    threads = []

    print(f"\n  [*] Scanning ports {start_port} - {end_port}...\n")
    start_time = time.time()

    # Create and start a thread for each port
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port, lock))
        threads.append(t)
        t.start()

    # Wait for all threads to finish before continuing
    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    print(f"\n  [*] Scan complete in {elapsed:.2f} seconds.")


# ──────────────────────────────────────────────
# Main Entry Point
# ──────────────────────────────────────────────

def main():
    # Banner
    print("=" * 45)
    print("         Python Network Port Scanner")
    print("         For Educational Use Only")
    print("=" * 45)

    try:
        target     = input("\n  Enter target IP or hostname : ").strip()
        start_port = int(input("  Enter start port            : ").strip())
        end_port   = int(input("  Enter end port              : ").strip())

        # Resolve hostname to IP address
        ip = socket.gethostbyname(target)
        print(f"\n  [*] Target   : {target}")
        print(f"  [*] Resolved : {ip}")

        # Validate port range
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("\n  [!] Invalid port range. Use ports between 1 and 65535.")
            return

        scan_range(ip, start_port, end_port)

    except ValueError:
        print("\n  [!] Port must be a number.")
        main()
    except socket.gaierror:
        print("\n  [!] Hostname could not be resolved.")
        main()
    except KeyboardInterrupt:
        print("\n\n  [!] Scan interrupted by user.")


if __name__ == "__main__":
    main()
