class ProtocolDictionary:
    """
    Dictionary of protocols supported by Wireshark(v3.2.3-0-gf39b50865a13)\n
    Details in Wireshark->Edit->Preferences->Protocols menu\n
    Exclude: '29West' protocol family; 'Bluetooth' protocol family; 'OSI' protocol family;\n
    NOTE: 在这个字典中的协议名称，并不一定对应于通过Wireshark导出Pcap包信息中对应的'Protocol'列。
    譬如在该字典中的协议'ARP/RARP'，在Wireshark导出时的'Protocol'却是'ARP'。
    这就导致对于一些协议我们无法利用该字典进行标记。
    大家在测试中需要注意名称不对应的问题，及时发现并及时将正确的名称加入该字典。
    """

    dict = {
        # <protocol_name>: <protocol_index>
        # Sorted in dictionary order
        # #
        '2dparityfec': 0, '3GPP2 A11': 1, '6LoWPAN': 2, '802.11 Radio': 3, '802.11 Radiotap': 4, '9P': 5,
        # A
        'A-bis OML': 6, 'A21': 7, 'ACAP': 8, 'ACN': 9, 'ACR 122': 10, 'ACtrace': 11,
        'ADB': 12, 'ADB CS': 13, 'ADB Service': 14, 'ADP': 15, 'ADwin': 16, 'Aeron': 17,
        'AgentX': 18, 'AIM': 19, 'AJP13': 20, 'ALC': 21, 'ALCAP': 22, 'AllJoyn ARDP': 23,
        'AllJoyn NS': 24, 'AMP': 25, 'AMQP': 26, 'AMR': 27, 'AMS': 28, 'AMT': 29,
        'ANCP': 30, 'ANSI BSMAP': 31, 'ANSI MAP': 32, 'ANSI_TCAP': 33, 'AODV': 34, 'AOL': 35,
        'APRS': 36, 'AR Drone': 37, 'Armagetronad': 38, 'ARP/RARP': 39, 'ARP': 40, 'Artemis': 41,
        'ARTNET': 42, 'ARUBA_ERM': 43, 'ASAP': 44, 'ASTERIX': 45, 'AT': 46, 'ATH': 47,
        'ATM': 48, 'ATMTCP': 49, 'ATP': 50, 'Auto-RP': 51, 'AUTOSAR NM': 52, 'AX.25 KISS': 53,
        'AX.25 no L3': 54, 'AX4000': 55, 'AYIYA': 56,
        # B
        'Babel': 57, 'Banana': 58, 'BAT': 59, 'BAT GW': 60, 'BAT VIS': 61, 'BATADV': 62,
        'Bazaar': 63, 'BEEP': 64, 'BER': 65, 'BFCP': 66, 'BFD Control': 67, 'BGP': 68,
        'Bitcoin': 69, 'BitTorrent': 70, 'BJNP': 71, 'BMP': 72, 'BRP': 73, 'BSSAP': 74,
        'BSSAP2': 75, 'BSSGP': 76, 'BT-DHT': 77, 'BT-uTP': 78, 'BTSNOOP': 79, 'Bundle': 80,
        'BVLC': 81,
        # C
        'C12.22': 82, 'CAMEL': 83, 'CAN': 84, 'CAN over AVTP': 85, 'CAN-ETH': 86, 'CAPWAP-CONTROL': 87,
        'CAPWAP-DATA': 88, 'CAST': 89, 'CAT-TP': 90, 'cbsp': 91, 'CCSDS': 92, 'CESoETH': 93,
        'CESoPSN basic (no RTP)': 94, 'CFDP': 95, 'CFLOW': 96, 'CFP': 97, 'Chargen': 98, 'CHDLC': 99,
        'CIGI': 100, 'CIMD': 101, 'CIP': 102, 'CIP I/O': 103, 'CISCO3 ERSPAN MARKER': 104, 'CLDAP': 105,
        'CLNP': 106, 'CMP': 107, 'CMPP': 108, 'CN/IP': 109, 'CoAP': 110, 'collectd': 111,
        'ComponentStatusProtocol': 112, 'COPS': 113, 'COROSYNC/TOTEMNET': 114, 'COTP': 115, 'Couchbase': 116,
        'CP2179': 117, 'CPFI': 118, 'CPHA': 119, 'CQL': 120, 'CTDB': 121, 'CUPS': 122,
        'cvspserver': 123, 'CWIDS': 124,
        # D
        'D-BUS': 125, 'Data': 126, 'DAYTIME': 127, 'DB-LSP128': 128, 'DB-LSP-DISC': 129, 'DCCP': 130,
        'DCERPC': 131, 'DCOM': 132, 'DCT2000': 133, 'DDTP': 134, 'DeviceNet': 135, 'DHCP/BOOTP': 136,
        'DHCP': 137, 'DHCPFO': 138, 'DHCPv6': 139, 'DHCPv6 Bulk Leasequery': 140, 'DIAMETER': 141, 'DICOM': 142,
        'DIS': 143, 'DISTCC': 144, 'DJIUAV': 145, 'DLM3': 146, 'DLSw': 147, 'DLT': 148,
        'DLT_USER': 149, 'DMP': 150, 'DMX Channels': 151, 'DNP 3.0': 152, 'DNS': 153, 'DOCSIS': 154,
        'DOF': 155, 'DRb': 156, 'DRDA': 157, 'DSI': 158, 'DTCP-IP': 159, 'DTLS': 160,
        'DTPS': 161, 'DTPT': 162, 'DVB-CI': 163, 'DVB-S2': 164, 'DVMRP': 165,
        # E
        'E1AP': 166, 'ECHO': 167, 'ECMP': 168, 'eCPRI': 169, 'EDONKEY': 170, 'EGD': 171,
        'EHS': 172, 'Elasticsearch': 173, 'ELCOM': 174, 'ELF': 175, 'ENIP': 176, 'ENRP': 177,
        'ENTTEC': 178, 'EPL': 179, 'EPMD': 180, 'ERF': 181, 'Ericsson GSM A-bis P-GSL': 182, 'ErlDP': 183,
        'ESG Bootstrap': 184, 'ESIO': 185, 'ESP': 186, 'ESS': 187, 'ETAG': 188, 'Etch': 189,
        'ETHERCAT': 190, 'Ethernet': 191, 'EVRC': 192, 'EVS': 193, 'EXEC': 194,
        # F
        'F1AP': 195, 'F5 Ethernet trailer': 196, 'FB/IB GDS DB': 197, 'FC': 198, 'Fc00': 199, 'FCGI': 200,
        'FCoIB': 201, 'FDDI': 202, 'FF': 203, 'Fibre Channel over IP': 204, 'File-PCAP': 205, 'File-PCAPNG': 206,
        'FINGER': 207, 'FIX': 208, 'FLEXRAY': 209, 'FMP': 210, 'ForCES': 211, 'FP': 212,
        'FP Mux': 213, 'FR': 214, 'Frame': 215, 'FTP': 216, 'FTP-DATA': 217, 'FW-1': 218,
        # G
        'Gadu-Gadu': 219, 'GDB remote': 220, 'Gearman': 221, 'GED125': 222, 'Geneve': 223, 'giFT': 224,
        'GIOP': 225, 'Git': 226, 'GLBP': 227, 'GMHDR': 228, 'GMTRAILER': 229, 'GNUTELLA': 230,
        'GNW': 231, 'Gopher': 232, 'GPRS-LLC': 233, 'GPRS-NS': 234, 'GQUIC': 235, 'GRPC': 236,
        'Gryphon': 237, 'GSM Osmux': 238, 'GSM over IP': 239, 'GSM SMS': 240, 'GSM SMS UD': 241, 'GSM Um': 242,
        'GSM-R': 243, 'GSM_MAP': 244, 'GSMTAP': 245, 'GSS-API': 246, 'gsup': 247, 'GTP': 248,
        'GTPv2': 249, 'GVSP': 250,
        # H
        'H.223': 251, 'H.223 (Bitswapped)': 252, 'H.225.0': 253, 'H.245': 254, 'H.501': 255, 'H248': 256,
        'H263P': 257, 'H264': 258, 'H265': 259, 'HART_IP': 260, 'HAZELCAST': 261, 'HCrt': 262,
        'HDFS': 263, 'HDFSDATA': 264, 'HIP': 265, 'HiQnet': 266, 'HiSLIP': 267, 'HL7': 268,
        'HNBAP': 269, 'HP_ERM': 270, 'HPFEEDS': 271, 'HSMS': 272, 'HSRP': 273, 'HTTP': 274,
        'HTTP2': 275,
        # I
        'IAPP': 276, 'IAX2': 277, 'IB': 278, 'ICAP': 279, 'ICEP': 280, 'ICMP': 281,
        'ICP': 282, 'ICQ': 283, 'IEC 60870-5-101': 284, 'IEC 60870-5-104': 285, 'IEEE 802.11': 286,
        'IEEE 802.15.4': 287, 'IEEE 802.1AH': 288, 'iFCP': 289, 'ILP': 290, 'IMAP': 291, 'IMF': 292,
        'INAP': 293, 'Infiniband SDP': 294, 'Interlink': 295, 'IPDC': 296, 'IPDR/SP': 297, 'iPerf2': 298,
        'IPMI': 299, 'IPSICTL': 300, 'IPv4': 301, 'IPv6': 302, 'IPVS': 303, 'IPX': 304,
        'IRC': 305, 'ISAKMP': 306, 'iSCSI': 307, 'ISDN': 308, 'iSER': 309, 'ISMACRYP': 310,
        'iSNS': 311, 'ISO 15765': 312, 'ISO 8583': 313, 'ISObus VT': 314, 'ISUP': 315, 'ITDM': 316,
        'IUA': 317, 'IuUP': 318, 'IXIATRAILER': 319,
        # J
        'Jmirror': 320, 'JSON': 321, 'Juniper': 322, 'JXTA': 323,
        # K
        'K12xx': 324, 'Kafka': 325, 'KDP': 326, 'KDSP': 327, 'Kingfisher': 328, 'KINK': 329,
        'Kismet': 330, 'KNET': 331, 'KNX/IP': 332, 'Kpasswd': 333, 'KRB4': 334, 'KRB5': 335,
        'Kyoto Tycoon': 336,
        # L
        'L&G 8979': 337, 'L2TP': 338, 'LAPD': 339, 'LAPDm': 340, 'Laplink': 341, 'LCSAP': 342,
        'LCT': 343, 'LDAP': 344, 'LDP': 345, 'LDSS': 346, 'LGE_Monitor': 347, 'LINX/TCP': 348,
        'LISP Control': 349, 'LISP Data': 350, 'LISP Reliable Transport': 351, 'LLC': 352, 'LLDP': 353, 'LLMNR': 354,
        'LLRP': 355, 'LLT': 356, 'LMP': 357, 'LNet': 358, 'LOG3GPP': 359, 'Logcat': 360,
        'LoRaWAN': 361, 'LPD': 362, 'LSC': 363, 'LTE RRC': 364, 'LTP': 365, 'LWAPP': 366,
        'LWAPP-L3': 367, 'LWL4': 368, 'LwM2M-TLV': 369, 'LwMesh': 370, 'LWRES': 371,
        # M
        'M2PA': 372, 'M2UA': 373, 'M3UA': 374, 'MAC': 375, 'MAC-LTE': 376, 'MAC-NR': 377,
        'MAC-Telnet': 378, 'Manolito': 379, 'MATE': 380, 'MAUSB': 381, 'MBIM': 382, 'MCPE': 383,
        'mDNS': 384, 'MDS Header': 385, 'MEGACO': 386, 'MEMCACHE': 387, 'MGCP': 388, 'MIH': 389,
        'MIKEY': 390, 'MIME multipart': 391, 'MiNT': 392, 'MIOP': 393, 'MIPv6': 394, 'MLE': 395,
        'MNDP': 396, 'Mobile IP': 397, 'Modbus': 398, 'Modbus RTU': 399, 'Modbus/TCP': 400, 'Modbus/UDP': 401,
        'Mojito': 402, 'MoldUDP': 403, 'MoldUDP64': 404, 'MONGO': 405, 'MP2T': 406, 'MP4V-ES': 407,
        'MPEG DSM-CC': 408, 'MPEG SECT': 409, 'MPLS': 410, 'MPLS Echo': 411, 'MPLS PW ATM AAL5 SDU': 412,
        'MPLS PW ATM N:1 CW': 413, 'MPTCP': 414, 'MQ': 415, 'MQ PCF': 416, 'MQTT': 417, 'MQTT-SN': 418,
        'MRCPv2': 419, 'MS Proxy': 420, 'MSDP': 421, 'MSMMS': 422, 'MSNMS': 423, 'MSRP': 424,
        'MTP over NW UDP': 425, 'MTP2': 426, 'MTP3': 427, 'MySQL': 428,
        # N
        'Nano': 429, 'NAS-5GS': 430, 'NAS-EPS': 431, 'NASDAQ-ITCH': 432, 'NASDAQ-SOUP': 433, 'NAT-PMP': 434,
        'NB_RTPMUX': 435, 'NBAP': 436, 'NBD': 437, 'NBDS': 438, 'NBNS': 439, 'NBP': 440,
        'NBSS': 441, 'NCP': 442, 'NDMP': 443, 'NDPS': 444, 'NetBIOS': 445, 'Netdump': 446,
        'Netsync': 447, 'NEWMAIL': 448, 'NFS': 449, 'NGAP': 450, 'NGE': 451, 'NHRP': 452,
        'NJACK': 453, 'NLM': 454, 'NNTP': 455, 'NORDIC_BLE': 456, 'NORM': 457, 'NTLMSSP': 458,
        'NTP': 459, 'NVMe Fabrics RDMA': 460, 'NVMe/TCP': 461, 'NXP 802154 Sniffer': 462,
        # O
        'OBEX': 463, 'OCFS2': 464, 'OER': 465, 'OICQ': 466, 'OLSR': 467, 'OMAPI': 468,
        'OMRON FINS': 469, 'OPA FE': 470, 'OPA MAD': 471, 'OpcUa': 472, 'OpenFlow': 473, 'openSAFETY': 474,
        'openSAFETY ov. UDP': 475, 'OpenVPN': 476, 'OpenWire': 477, 'OPSI': 478, 'OptoMMP': 479, 'OSC': 480,
        'OSCORE': 481, 'OUCH': 482,
        # P
        'P_MUL': 483, 'PacketBB': 484, 'PANA': 485, 'PAPI': 486, 'Pathport': 487, 'PCAP': 488,
        'PCEP': 489, 'PCLI': 490, 'PCLI12 (timestamp)': 491, 'PCLI20 (timestamp, case ID)': 492,
        'PCLI8 (8 byte CCCID)': 493, 'PCOM/TCP': 494, 'PCP': 495, 'PDC': 496, 'PDCP-LTE': 497, 'PDCP-NR': 498,
        'PEEKREMOTE': 499, 'PER': 500, 'PFCP': 501, 'PFLOG': 502, 'PGM': 503, 'PGSQL': 504,
        'PIM': 505, 'PKCS12': 506, 'PKT CCC': 507, 'PKTC': 508, 'PKTC MTA FQDN': 509, 'PMPROXY': 510,
        'PN-RT': 511, 'PN532': 512, 'PN532_HCI': 513, 'PNIO': 514, 'PNRP': 515, 'POP': 516,
        'Port Control': 517, 'PPI': 518, 'PPP': 519, 'PPP MP': 520, 'PPPoED': 521, 'PPTP': 522,
        'PRES': 523, 'ProtoBuf': 524, 'PTP': 525, 'PTP/IP': 526, 'PULSE': 527, 'PVFS': 528,
        # Q
        'Q.931': 529, 'Q932': 530, 'QUAKE': 531, 'QUAKE2': 532, 'QUAKE3': 533, 'QUAKEWORLD': 534,
        'QUIC': 535,
        # R
        'R3': 536, 'RADIUS': 537, 'RANAP': 538, 'RDP': 539, 'RDT': 540, 'RedbackLI': 541,
        'RELOAD': 542, 'RELOAD FRAMING': 543, 'Riemann': 544, 'RIP': 545, 'RIPng': 546, 'RLC': 547,
        'RLC-LTE': 548, 'RLC-NR': 549, 'Rlogin': 550, 'RMCP': 551, 'RMI': 552, 'RPC': 553,
        'RPCAP': 554, 'RPKI-Router Protocol': 555, 'RSH': 556, 'RSIP': 557, 'RSL': 558, 'RSP': 559,
        'RSVP': 560, 'RSYNC': 561, 'RTCDC': 562, 'RTCP': 563, 'RTLS': 564, 'RTMPT': 565,
        'RTP': 566, 'RTP Event': 567, 'RTP-MIDI': 568, 'RTPproxy': 569, 'RTPS': 570, 'RTSP': 571,
        'RUA': 572, 'RUDP': 573, 'RX': 574,
        # S
        'S101': 575, 'S1AP': 576, 'SABP': 577, 'SAMETIME': 578, 'SAP': 579, 'SASP': 580,
        'SAToP (no RTP)': 581, 'SBUS': 582, 'SCCP': 583, 'SCoP': 584, 'SCSI': 585, 'SCTP': 586,
        'SDH': 587, 'SDP': 588, 'SEBEK': 589, 'SEL Protocol': 590, 'SES': 591, 'sFlow': 592,
        'SGSAP': 593, 'SIGCOMP': 594, 'SIMPLE': 595, 'SIMULCRYPT': 596, 'SIP': 597, 'SIR': 598,
        'SKINNY': 599, 'SKYPE': 600, 'SliMP3': 601, 'SMB': 602, 'SMB2': 603, 'SMBDirect': 604,
        'SML': 605, 'SMP': 606, 'SMPP': 607, 'SMRSE': 608, 'SMTP': 609, 'SMUX': 610,
        'SNA': 611, 'SNMP': 612, 'Snort': 613, 'Socks': 614, 'SolarEdge': 615, 'SOME/IP': 616,
        'SOME/IP-SD': 617, 'SoulSeek': 618, 'SoupBinTCP': 619, 'SPDY': 620, 'Spice': 621, 'SPRT': 622,
        'SRVLOC': 623, 'SSCOP': 624, 'SSDP': 625, 'SSH': 626, 'STANAG 5066 DTS': 627, 'STANAG 5066 SIS': 628,
        'StarTeam': 629, 'Steam IHS Discovery': 630, 'STP': 631, 'STT': 632, 'STUN': 633, 'SUA': 634,
        'SV': 635, 'SYNC': 636, 'SYNCHROPHASOR': 637, 'Synergy': 638, 'Syslog': 639,
        # T
        'T.38': 640, 'TACACS': 641, 'TACACS+': 642, 'TALI': 643, 'TAPA': 644, 'TCAP': 645,
        'TCP': 646, 'TCPENCAP': 647, 'TCPROS': 648, 'TDMoE': 649, 'TDMoP': 650, 'TDS': 651,
        'TeamSpeak2': 652, 'TELNET': 653, 'Teredo': 654, 'TETRA': 655, 'TFP': 656, 'TFTP': 657,
        'Thread': 658, 'Thrift': 659, 'Tibia': 660, 'TIME': 661, 'TIPC': 662, 'TiVoConnect': 663,
        'TLS': 664, 'TNS': 665, 'Token-Ring': 666, 'TPCP': 667, 'TPKT': 668, 'TPM2.0': 669,
        'TPNCP': 670, 'TRANSUM': 671, 'TSDNS': 672, 'TSP': 673, 'TTE': 674, 'TURNCHANNEL': 675,
        'TUXEDO': 676, 'TZSP': 677,
        # U
        'UA3G': 678, 'UASIP': 679, 'UAUDP': 680, 'UBDP': 681, 'UBERTOOTH': 682, 'UCP': 683,
        'UDP': 684, 'UDP-Lite': 685, 'UDPENCAP': 686, 'UDT': 687, 'UFTP': 688, 'UHD': 689,
        'ULP': 690, 'UMA': 691, 'UNISTIM': 692, 'USB': 693, 'USB DFU': 694, 'USBIP': 695,
        'UserLog': 696,
        # V
        'VCDU': 697, 'VICP': 698, 'Vines FRP': 699, 'VITA 49': 700, 'VLAN': 701, 'VNC': 702,
        'VP8': 703, 'VRRP': 704, 'VSIP': 705, 'VXLAN': 706, 'VXLAN (GPE)': 707,
        # W
        'WASSP': 708, 'WBXML': 709, 'WCCP': 710, 'WebSocket': 711, 'WHO': 712, 'WHOIS': 713,
        'WiMax (wmx)': 714, 'WiMAX ASN CP': 715, 'WiMAX MAC-PHY': 716, 'WINS-Replication': 717, 'WireGuard': 718,
        'WLCCP': 719, 'WOW': 720, 'WSP': 721, 'WTLS': 722, 'WTP': 723,
        # X
        'X.25': 724, 'X11': 725, 'X2AP': 726, 'XDMCP': 727, 'XMCP': 728, 'XML': 729,
        'XMPP': 730, 'XnAP': 731, 'XOT': 732, 'XYPLEX': 733,
        # Y
        'YAMI': 734, 'YMSG': 735,
        # Z
        'Z39.50': 736, 'ZEBRA': 737, 'ZigBee': 738, 'ZigBee APS': 739, 'ZigBee Green Power': 740, 'ZIOP': 741,
        'ZRTP': 742, 'ZVT': 743,
        # Not included protocol is 'UNKNOWN'
        'UNKNOWN': 999
    }

    opposite_dict = {
        # <protocol_index>: <protocol_name>
        value: key for key, value in dict.items()
    }