from scapy.all import *

  ospf_hello_ = IP(dst="<destination_IP_Address")/UDP(dport=89)/OSPF_Hdr(auth_type=0)

  send(ospf_hello_, iface="<interface value (eht0)")
