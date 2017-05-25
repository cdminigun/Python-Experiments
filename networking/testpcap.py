import dpkt
import struct

pcap_fd = open("SampleData.pcap")
pcap = dpkt.pcap.Reader(pcap_fd)

for ts, buf in pcap:
    type(ts)
    print ts
    ts
    eth = dpkt.ethernet.Ethernet(buf)
    #print repr(eth)
    ip = eth.data
    #print repr(ip)
    tcp = ip.data
    print repr(tcp.dport)
    print repr(tcp)
    if "UDP" in repr(tcp):
        print("UDP packet")
    stuff = tcp.data
    print repr(stuff)
    print "\n\n"
    #print repr(tcp)
