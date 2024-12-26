from scapy.all import Ether, sendp

for i in range(1000):
  pkt = Ether(src="00:11:22:33:44:55" / "Flooding"

              send(pkt, iface="", verbose=0)
