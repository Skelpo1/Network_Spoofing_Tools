from scapy.all import Ether, sendp

for i in range(1000):
  pkt = Ether(src="00:11:22:33:44:55" / "Flooding" # !!!caution when setting mac address as you do not want to set make address flood = 00:00:00:... as this will cause STP confusion!!!

              send(pkt, iface="<interface value (eht0)", verbose=0)
