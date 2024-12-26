from scapy.all import IP, UDP, send

  ospf_pkt_ = IP(dst="<destination_IP_Address") / UDP(dport=89) / "OSPF, Hello Packet"

  send(ospf_pakt_)
