# Arp Cache Poisoning MITM

According to the [MITRE ATT&CK ARP Cache Poisoning MITM](https://attack.mitre.org/techniques/T1557/002/) technique, adversaries can manipulate ARP caches to position themselves between communicating devices on a local network. By associating their own MAC address with another device’s IP address, attackers can intercept, monitor, or modify network traffic, enabling activities such as credential theft or data manipulation.

## Suricatas Reaction to the Attack

With the current rule set, Suricata was not able to detect this attack.



## How the Attack Works

There are several tools available for performing ARP cache poisoning attacks. In this demonstration, the tool **arpspoof** (part of the dsniff suite) was used.

The tool can be executed with the following command:


```
arpspoof -i <interface> -t <target_ip> <spoofed_ip>
```


This command sends forged ARP replies to the target, associating the attacker's MAC address with the specified IP address, allowing the attacker to intercept network traffic.

## Mitigations

According to the [MITRE ATT&CK ARP Cache Poisoning MITM](https://attack.mitre.org/techniques/T1557/002/), the following mitigations can help reduce the risk of ARP poisoning attacks:

- **M1042 – Disable or Remove Feature or Program:** Disable ARP cache updates from gratuitous ARP replies where possible.  
- **M1041 – Encrypt Sensitive Information:** Use encryption (e.g., SSL/TLS) to protect network traffic and credentials.  
- **M1037 – Filter Network Traffic:** Enable protections such as DHCP Snooping and Dynamic ARP Inspection to prevent spoofed ARP traffic.  
- **M1035 – Limit Access to Resource Over Network:** Use static ARP entries for critical systems when feasible.  
- **M1031 – Network Intrusion Prevention:** Deploy intrusion detection/prevention systems to identify suspicious network behavior.  
- **M1017 – User Training:** Educate users to recognize certificate warnings that may indicate interception attempts.

### Chosen Mitigation Strategy

For my devices in my local network the most efficient way is to use static ARP entries. Depending on the system this can be done with this command:

```
sudo ip neigh add <IP_ADDRESS> lladdr <MAC_ADDRESS> dev <INTERFACE> nud permanent

```
