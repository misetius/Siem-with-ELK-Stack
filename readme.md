The purpose of this project is to explore and test the Elastic Stack (Elasticsearch, Logstash, Kibana) in a practical environment by simulating cyber attacks.

## In this setup:

The ELK Stack runs on a laptop, acting as the central SIEM for log collection, processing, and visualization
Filebeat runs on a Raspberry Pi, collecting log data and forwarding it to the ELK Stack
Attacks are executed from a separate desktop computer targeting the Raspberry Pi

All simulated attacks performed, along with any countermeasures (if applicable), are documented below. Each attack has its own dedicated folder, which includes a detailed README file describing:

- the attack scenario
- execution steps
- logs generated
- detection and analysis in ELK Stack
- mapping to MITRE ATT&CK techniques
- possible mitigation strategies

This project demonstrates how a SIEM can be used to detect and analyze real-world attack behavior in a controlled lab environment.

## Environment

                  ATTACK TRAFFIC
        +----------------------------------+
        |        Desktop Computer          |
        |        (Attacker Machine)        |
        +---------------+------------------+
                        |
                        |  Attacks
                        v
        +---------------+------------------+
        |           Raspberry Pi           |
        |           (Target Host)          |
        |                                  |
        |   +--------------------------+   |
        |   |  Suricata IDS            |   |
        |   |  (Network Monitoring)    |   |
        |   +--------------------------+   |
        |                                  |
        |   +--------------------------+   |
        |   |  Filebeat Agent          |   |
        |   |  (Log Forwarding)        |   |
        |   +--------------------------+   |
        +---------------+------------------+
                        |
                        |  Logs (via Filebeat)
                        v
        +---------------+------------------+
        |            Laptop                |
        |            (SIEM)                |
        |                                  |
        |   +--------------------------+   |
        |   |  Elasticsearch           |   |
        |   |  (Storage & Search)      |   |
        |   +--------------------------+   |
        |                                  |
        |   +--------------------------+   |
        |   |  Kibana                  |   |
        |   |  (Dashboards & Analysis) |   |
        |   +--------------------------+   |
        |                                  |
        +----------------------------------+

## Few remarks

- The environment is fully isolated and accessible only from a single workstation within a private local network. No services are exposed to the public internet.

- "Attacks" are done to a Raspberry Pi system which my desktop normally has access to for example through SSH.

- Raspberry Pi is not publicly available and the services running on it are only available to devices in the local network.


