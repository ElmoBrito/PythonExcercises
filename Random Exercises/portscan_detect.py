import re

def portscan_detect(netflow):
  ip_dict = {}
  
  with open(netflow, 'r') as f:
    
    for line in f:
      split_log = re.split(' -> |:', line.strip())
      src_ips = split_log[0]
      dest_ips = split_log[2]
      dest_ports = split_log[3]
      
      if src_ips not in ip_dict:
        ip_dict[src_ips] = {}
      ip_dict[src_ips].setdefault(dest_ips, {})[dest_ports] = 1
    
    for src_ips, dest_ips in ip_dict.items():
      for ports in dest_ips:
        if len(dest_ips[ports]) >= 3:
          print(src_ips)
