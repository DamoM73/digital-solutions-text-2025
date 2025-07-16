# Data Security - Threats

:::{dropdown} Learning Goals
By the end of this section you will:
- understand malicious threats to data security
- understand non-malicious threats to data security
- know a range measure that be undertaken to protect against data threats
:::

Data security threats are risks that compromise the confidentiality, integrity, or availability of digital information. These threats can originate from malicious actors such as hackers, cybercriminals, or insiders, as well as from unintentional sources like software bugs or human error. Common threats include malware, phishing attacks, ransomware, data breaches, and denial-of-service (DoS) attacks. As digital systems become more interconnected, the potential for exploitation grows, making it essential for individuals and organizations to implement robust security measures to protect sensitive data and ensure system reliability.

Data security threats fall under two main categories:

- malicious threats which involve intentional acts
- non-malicious threats which are unintentional actions, accidents, or natural events

---

## Malicious Threats

Malicious data security threats are intentional attacks designed to compromise the confidentiality, integrity, or availability of data. There are numerous malicious threats to data security that organizations and individuals need to be aware of. Here are some of the most common threats:

### Malware

Malware is malicious software designed to disrupt, damage, or gain unauthorized access to computer systems. This includes:

- **Viruses**
  - designed to replicate themselves and spread from one computer to another
  - often disrupting operations, corrupting or deleting data, and potentially causing significant damage to systems and networks
  - spread by attaching itself to executable files or documents
- **Worms**
  - self-replicating malware
  - spreads autonomously across networks, exploiting vulnerabilities without needing to attach itself to an existing program
  - causes harm by consuming bandwidth, overloading systems, or delivering additional payloads such as ransomware.
- **Trojans**
  - disguises itself as a legitimate or benign application to deceive users into installing it
  - allows attackers to gain unauthorized access to the user's system to steal data, create backdoors, or perform other harmful actions once it is executed.
- **Ransomware**
  - designed to block access to a computer system or data
  - typically encrypts files until a ransom is paid to the attacker to restore access
  - often spreads through phishing emails, malicious downloads, or exploit kits
  - can cause significant disruption to individuals and organizations by locking them out of their own data or systems
- **Spyware**
  - designed to secretly monitor and collect information about a user's activities without their knowledge or consent
  - data can include browsing habits, keystrokes, login credentials, and other sensitive information
  - data is sent to the attacker for malicious purposes such as identity theft, financial fraud, or unauthorized access to systems and accounts.
- **Adware**
  - automatically displays or downloads advertising content, such as banners or pop-ups, on a user's computer or mobile device, often without their consent or knowledge.
  - while not always malicious, it can invade privacy by tracking user behaviour and gathering personal information for targeted advertising, and in some cases, it can serve as a conduit for more harmful malware.

**Malware Example**

One of the most infamous malware attacks is the [WannaCry ransomware attack](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack), which occurred in May 2017. WannaCry exploited a vulnerability in Microsoft Windows, known as EternalBlue, to spread rapidly across networks worldwide. 

The ransomware encrypted users' files and demanded a ransom payment in Bitcoin to decrypt the data. WannaCry affected hundreds of thousands of computers in over 150 countries, impacting critical sectors such as healthcare, finance, and telecommunications. 

The National Health Service (NHS) in the United Kingdom was particularly hard hit, leading to the cancellation of appointments and surgeries. The attack highlighted the importance of timely software updates and robust cybersecurity measures to protect against such vulnerabilities​.

### Phishing

A phishing attack is a type of cybercrime where attackers impersonate legitimate organizations or individuals to trick people into revealing sensitive information, such as passwords, credit card numbers, or login credentials. This is usually done through deceptive emails, messages, or websites that appear trustworthy but are designed to steal data or install malicious software. Phishing relies on social engineering techniques, exploiting human trust rather than technical vulnerabilities. These attacks can lead to identity theft, financial loss, and unauthorized access to personal or organizational systems.

**Phishing Example**

A notable example of a phishing attack is the [2016 attack on John Podesta](https://en.wikipedia.org/wiki/Podesta_emails), chairman of Hillary Clinton's presidential campaign. 

Hackers sent a phishing email disguised as a security alert from Google, claiming that Podesta needed to change his password due to suspicious activity. The email contained a link to a fake login page that closely resembled the genuine Google login page. Podesta's aide, believing the email to be legitimate, forwarded it to the campaign's IT staff, who mistakenly identified the email as genuine and advised Podesta to change his password using the provided link. As a result, Podesta entered his credentials on the fake page, allowing hackers to gain access to his email account. 

This breach led to the exposure of thousands of emails, which were subsequently published by WikiLeaks, causing significant political and reputational damage during the 2016 U.S. presidential election.

### Man-in-the-Middle (MitM) Attacks

A man-in-the-middle (MITM) attack occurs when a malicious actor secretly intercepts and possibly alters the communication between two parties without their knowledge. This type of attack allows the attacker to eavesdrop on sensitive information such as login credentials, financial data, or personal messages. MITM attacks can happen on unsecured or poorly secured networks, like public Wi-Fi, where the attacker can position themselves between the user and a legitimate service (e.g., a website or app). By doing so, they can capture data being sent or inject malicious content into the communication stream, posing serious risks to data confidentiality and integrity.

**Man-in-the-Middle Attack Example**

In 2015, Lenovo was found to have pre-installed a software called [Superfish](https://en.wikipedia.org/wiki/Superfish) on some of its laptops.

Superfish was an adware program that intercepted users' web traffic to inject advertisements. It did this by installing its own self-signed root certificate authority, allowing it to intercept and decrypt HTTPS traffic between the user's browser and websites, essentially performing a Man-in-the-Middle attack. 

This compromised the security of encrypted connections, making users vulnerable to further attacks and data theft by malicious entities exploiting the same root certificate.

### Denial of Service (DoS) and Distributed Denial of Service (DDoS) Attacks

A Distributed Denial-of-Service (DDoS) attack is a cyberattack in which multiple compromised computers or devices—often part of a botnet—are used to flood a target system, such as a website or server, with massive amounts of traffic. This overwhelming surge in requests exhausts the target’s resources, causing it to slow down significantly or crash completely, making it unavailable to legitimate users. DDoS attacks are often used to disrupt business operations, extort companies, or draw attention to political or social causes. Because the attack comes from many sources, it is difficult to block and can cause widespread disruption.

**DDoS example**

A notable example of a Distributed Denial of Service (DDoS) attack is the [October 2016 attack on Dyn](https://en.wikipedia.org/wiki/DDoS_attacks_on_Dyn), a company that manages DNS (Domain Name System) services. 

This attack involved a massive [botnet](https://en.wikipedia.org/wiki/Botnet) called Mirai, which harnessed the power of numerous compromised IoT (Internet of Things) devices, including cameras and DVRs, to flood Dyn's servers with traffic. The overwhelming volume of traffic disrupted Dyn's DNS services, leading to widespread outages for major websites and online services such as Twitter, Reddit, Netflix, and Airbnb. 

The attack highlighted the vulnerabilities of IoT devices and the significant impact DDoS attacks can have on internet infrastructure​ 

### Insider Threats

Insider threats occur when individuals within an organization—such as employees, contractors, or business partners—intentionally or unintentionally compromise the security of the organization’s data or systems. These threats can involve stealing sensitive information, sabotaging systems, or accidentally exposing data through negligence or poor security practices. Unlike external attackers, insiders often have legitimate access to critical systems and data, making their actions harder to detect and defend against. Insider threats pose a significant risk because they exploit trust and access, and can result in data breaches, financial loss, and damage to an organization’s reputation.

**Insider Threat Example**

One of the most infamous examples of an insider threat is the case of [Edward Snowden](https://en.wikipedia.org/wiki/Edward_Snowden). 

In 2013, Snowden, a former contractor for the National Security Agency (NSA), leaked classified documents to journalists, revealing extensive global surveillance programs operated by the NSA and its international partners. Snowden's disclosures exposed the scale and scope of government surveillance on citizens and sparked a global debate about privacy and security. 

His actions had profound implications for national security and privacy, leading to significant legal and political repercussions​.

### SQL Injections

SQL injection is a type of cyberattack where an attacker inserts malicious SQL (Structured Query Language) code into a web application's input fields to manipulate or access the underlying database. This can allow attackers to bypass authentication, view or modify sensitive data, delete records, or even gain full control over the database server. SQL injections typically occur when user inputs are not properly validated or sanitized, making the application vulnerable. These attacks are dangerous because they can compromise the confidentiality and integrity of stored data, and are often used to exploit poorly secured websites and applications.

**SQL Injection Example**

A famous example of an SQL injection attack is the 2008 breach of [Heartland Payment Systems](https://en.wikipedia.org/wiki/Heartland_Payment_Systems). 

Heartland, one of the largest payment processing companies in the United States, suffered a massive data breach due to an SQL injection vulnerability. Attackers exploited this vulnerability to install malware on Heartland’s network, allowing them to capture and exfiltrate over 130 million credit card numbers. 

This breach led to significant financial losses and legal repercussions for the company and highlighted the critical importance of securing web applications against SQL injection attacks.

### Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) is a type of cyberattack where an attacker injects malicious scripts—usually JavaScript—into webpages that are then viewed by other users. When a user visits the affected page, the script runs in their browser, potentially allowing the attacker to steal cookies, session tokens, or other sensitive information, impersonate the user, or perform actions on their behalf. XSS vulnerabilities typically occur when web applications fail to properly validate or sanitize user input. This makes XSS a serious threat to both user privacy and web application security, especially in platforms that rely on dynamic content and user-generated input.

**Cross-Site Scripting Example**

One of the most notable examples of a Cross-Site Scripting (XSS) attack occurred on MySpace in 2005, known as the ["Samy worm" attack](https://en.wikipedia.org/wiki/Samy_(computer_worm)). 

A user named Samy Kamkar created a worm that exploited an XSS vulnerability in MySpace's site. The worm embedded a script in Samy's profile page that, when visited by other users, would automatically add Samy to their friend list and display the phrase "but most of all, Samy is my hero" on their profile. Moreover, the script replicated itself to their profiles, leading to rapid and widespread propagation. Within 20 hours, over one million MySpace users were affected, making it one of the fastest spreading XSS worms in history. 

This incident highlighted the severe impact of XSS vulnerabilities and the importance of input validation and sanitization.

### Advanced Persistent Threats (APTs)

Advanced Persistent Threats (APTs) are prolonged and targeted cyberattacks in which an intruder gains unauthorized access to a network and remains undetected for an extended period. Unlike typical attacks that aim for quick disruption or theft, APTs are often carried out by highly skilled attackers—such as state-sponsored groups—with the goal of stealing sensitive data, conducting espionage, or sabotaging operations. These attacks use sophisticated techniques like spear phishing, zero-day exploits, and custom malware to infiltrate systems and maintain access over time. Because of their stealthy nature and targeted approach, APTs are particularly dangerous to governments, corporations, and critical infrastructure.

**Advanced Persistent Threat Example**

One of the most famous examples of an Advanced Persistent Threat (APT) is the [Stuxnet attack](https://en.wikipedia.org/wiki/Stuxnet), discovered in 2010. 

Stuxnet is a sophisticated malware believed to have been developed jointly by the United States and Israel to sabotage Iran's nuclear program. The malware targeted Siemens PLCs (Programmable Logic Controllers) used in Iran's Natanz uranium enrichment facility. It exploited multiple zero-day vulnerabilities and was capable of reprogramming the PLCs to cause the centrifuges to spin out of control while reporting normal operation to monitoring systems, effectively damaging the equipment and setting back Iran's nuclear efforts. 

This attack highlighted the potential of cyber warfare and the risks posed by APTs to critical infrastructure.

### Zero-Day Exploits

Zero-day exploits are cyberattacks that target previously unknown vulnerabilities in software or hardware—flaws that developers have had "zero days" to fix because they are not yet aware of them. These exploits are especially dangerous because they occur before a patch or update can be released, leaving systems defenceless. Attackers use zero-day vulnerabilities to gain unauthorized access, steal data, or compromise systems, often with highly targeted and stealthy methods. Because no existing security measures may detect or block them, zero-day exploits are highly prized by cybercriminals and nation-state hackers alike, posing significant risks to individuals, organizations, and governments.

**Zero-Day Exploits Example**

Both the **Stuxnet** worm and the **WannaCry** ransomware used zero-day exploits. 

**Stuxnet** used the following exploits:

- **LNK Vulnerability (CVE-2010-2568): Stuxnet exploited a vulnerability in how Windows processes shortcut files (.LNK). Simply viewing an infected USB drive in Windows Explorer would trigger the execution of the malware.
- **Windows Print Spooler Vulnerability (CVE-2010-2729): This vulnerability allowed remote code execution through the Windows Print Spooler service, enabling the malware to spread across networks.
- **Windows Task Scheduler Vulnerability (CVE-2010-3888): Stuxnet exploited a vulnerability in the Windows Task Scheduler to elevate privileges and gain administrative rights on infected systems.
- **MS08-067 (CVE-2008-4250): Although not a zero-day at the time of the Stuxnet attack, this older vulnerability was used to propagate across networked systems by exploiting a flaw in the Windows Server Service.
- **Win32k.sys Vulnerability (CVE-2010-2743): This vulnerability in the Windows kernel allowed Stuxnet to execute arbitrary code with kernel-mode privileges, providing extensive control over the infected system.

**WannaCry** used the [EternalBlue](https://en.wikipedia.org/wiki/EternalBlue) to exploit a flaw in the SMBv1 (Server Message Block) protocol, allowing the malware to execute arbitrary code on the target machine without requiring user interaction. The exploit took advantage of the way SMB handled specially crafted packets, causing the system to execute the attacker's code.

### Supply Chain Attacks

A supply chain attack is a cyberattack that targets the less secure elements of an organization's supply network, such as third-party vendors, contractors, or software providers, to compromise the primary target. Instead of attacking the main organization directly, hackers infiltrate trusted partners or software updates to insert malicious code or gain unauthorized access. Once the compromised component is integrated into the main system, the attacker can exploit it to steal data, disrupt operations, or move laterally within the network. These attacks are particularly dangerous because they exploit trusted relationships and can bypass traditional security defences, as seen in major incidents like the SolarWinds breach.

**Supply Chain Attack Example**

One of the most notorious examples of a supply chain attack is the [2020 SolarWinds hack](https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach). 

In this attack, cybercriminals infiltrated the IT management company SolarWinds and inserted malicious code into their Orion software updates, which were then distributed to SolarWinds' customers. This compromised update created a backdoor into the systems of approximately 18,000 organizations, including numerous U.S. government agencies and Fortune 500 companies. The attackers, believed to be associated with the Russian state-sponsored group APT29 (also known as Cozy Bear), used this access to conduct extensive espionage, gathering sensitive information from high-profile targets. 

This incident highlighted the vulnerabilities in software supply chains and the extensive impact such breaches can have on national security and corporate infrastructure

---

## Non-malicious Threats

Non-malicious threats to data security are risks that arise from unintentional actions, accidents, or natural events, rather than deliberate attacks. Here are some common non-malicious threats:

### Human Error

Human error is one of the most common causes of data security threats, often resulting from mistakes made by employees or users that unintentionally compromise systems or sensitive information. Examples include misconfiguring security settings, accidentally deleting critical files, clicking on phishing links, or using weak or reused passwords. Unlike malicious attacks, these threats stem from carelessness, lack of training, or poor understanding of security protocols. Despite being unintentional, the consequences can be severe—leading to data breaches, system outages, or exposure of personal and financial data. Addressing human error requires ongoing user education, strong policies, and automated safeguards to reduce risk.

**Human Error Example**

A famous example of a data security risk caused by human error is the [2017 Equifax data breach](https://en.wikipedia.org/wiki/2017_Equifax_data_breach#:~:text=Private%20records%20of%20147.9%20million,the%20public%20until%20September%202017.). 

In this incident, sensitive personal information of approximately 147 million people, including names, social security numbers, birth dates, addresses, and in some cases, driver's license numbers and credit card information, was exposed. The breach was primarily attributed to the failure of Equifax to apply a critical security patch for a known vulnerability in the Apache Struts web application framework. 

Despite being alerted to the vulnerability and the availability of a patch two months prior to the breach, Equifax's IT staff failed to update their systems, allowing attackers to exploit the flaw and gain access to sensitive data.

### Hardware Failures

Hardware failures pose a significant threat to data security and availability by causing sudden loss, corruption, or inaccessibility of important information. Failures can occur in hard drives, servers, storage devices, or networking equipment due to wear and tear, manufacturing defects, power surges, or environmental conditions like overheating. When hardware malfunctions, it can result in permanent data loss if proper backups and redundancy systems are not in place. Additionally, recovery from hardware failure can be time-consuming and costly, making it essential for organizations to implement robust disaster recovery plans, regular backups, and hardware monitoring to minimize the risk and impact of such failures.

**Hardware Failure Example**

A significant example of hardware failure resulting in data loss is the [2011 outage experienced by the cloud service provider Amazon Web Services (AWS)](https://money.cnn.com/2011/04/21/technology/amazon_server_outage/index.htm). 

In April 2011, a failure in AWS's Elastic Block Store (EBS) caused a cascading effect that led to extended downtime and data loss for numerous websites and services that relied on AWS. The incident began with a network configuration error during a routine maintenance operation, which resulted in a large number of EBS nodes becoming unreachable. As AWS engineers attempted to fix the problem, they inadvertently caused further issues that led to data corruption and loss. 

Many businesses experienced prolonged outages, and some permanently lost data due to the disruption.

### Software Bugs

Software bugs are flaws or errors in a program's code that can create vulnerabilities and pose serious threats to data security. These bugs may cause systems to behave unpredictably, expose sensitive information, or allow unauthorized access to data. For example, a coding error might disable authentication checks or mishandle user input, leading to issues like data corruption, privilege escalation, or security breaches. Because software is often complex and constantly updated, bugs can be difficult to detect and may remain unnoticed until exploited by attackers. To reduce these risks, developers must rigorously test code, apply updates and patches promptly, and follow secure coding practices.

**Software Bug Example**

In July 2023, a [software update for the CrowdStrike Falcon sensor resulted in a widespread issue](https://www.wired.com/story/crowdstrike-outage-update-windows/). 

The issue caused Blue Screen of Death (BSOD) errors on Windows systems, leading to significant IT disruptions. The flawed update caused system crashes and data loss across thousands of devices by corrupting system files and interrupting critical operations. This incident is attributed to a logic error in the sensor's configuration file.

This exemplifies how software bugs can lead to severe data loss and operational downtime, highlighting the necessity for rigorous testing and robust incident response protocols to mitigate such risks.

### Power Outages

Power outages can pose significant threats to data security by causing sudden system shutdowns that may lead to data loss, corruption, or hardware damage. When computers or servers lose power unexpectedly, open files may not be saved properly, databases can become inconsistent, and critical processes may be interrupted. Repeated power disruptions can also wear down hardware over time. Without proper backup power solutions, such as uninterruptible power supplies (UPS), and automated data-saving mechanisms, organizations risk losing important information and facing extended downtime. In sensitive environments, even a brief outage can disrupt business operations and compromise data integrity.

**Power Outages Example**

A notable example of data security being placed at risk due to power outages occurred in 2013 at the [National Security Agency's (NSA) massive data centre in Bluffdale](https://www.bbc.com/news/technology-24443266), Utah. 

The facility experienced a series of power outages caused by electrical surges. These outages damaged critical infrastructure, including computers and cooling systems, leading to concerns over potential data loss and system reliability. The issues were attributed to electrical surges during equipment testing and installation phases, which caused significant delays in the facility's operational readiness and raised questions about the robustness of the NSA's data security measures during infrastructure failures.

### Natural Disasters

Natural disasters such as floods, earthquakes, fires, and hurricanes can cause severe damage to physical infrastructure, resulting in the loss or inaccessibility of critical data. These events can destroy servers, data centres, and networking equipment, leading to permanent data loss if proper backups and disaster recovery plans are not in place. In addition to physical destruction, natural disasters can also disrupt power and internet connectivity, hindering access to cloud-based systems and remote services. To mitigate these threats, organizations should implement off-site backups, cloud storage, redundant systems, and comprehensive disaster recovery strategies to ensure data resilience and business continuity in the face of unforeseen events.

**Natural Disasters Example**

A well-known example of data security being jeopardized due to natural disasters occurred during [Hurricane Sandy in 2012](https://abcnews.go.com/Technology/hurricane-sandy-takes-york-city-data-center-gawker/story?id=17601425). 

The hurricane caused extensive power outages across the north-eastern United States, including in New York City. This led to significant disruptions at data centres, including those managed by Datagram, which hosted websites like Gawker, BuzzFeed, and the Huffington Post. The power outages caused by the hurricane resulted in a loss of connectivity and server downtime, highlighting vulnerabilities in data centre infrastructure. 

Despite having backup generators, Datagram's fuel pumps were located in a basement that flooded, rendering the backup power systems ineffective and resulting in prolonged outages and potential data loss risks.

### Network Failures

Network failures occur when the communication links between systems break down, posing serious threats to data availability and business operations. These failures can be caused by hardware malfunctions, software misconfigurations, cyberattacks, or issues with internet service providers. When a network goes down, users may lose access to critical data, experience interruptions in data transfer, or face delays in real-time services. In some cases, data being transmitted during the failure may be lost or corrupted. Network failures can also expose systems to security risks if fallback mechanisms are not secure. To minimize these threats, organizations should implement redundant network paths, monitor systems continuously, and have failover plans in place.

**Network Failures Example**

A significant example of network failures risking data security is the [2008 outage at RBS (Royal Bank of Scotland), NatWest, and Ulster Bank](https://www.theguardian.com/money/2012/jun/29/natwest-fiasco-what-happens.now).

This incident occurred when a routine software update to the bank's CA-7 batch processing system failed. The update corrupted the scheduling software, leading to a massive backlog of unprocessed transactions. As a result, millions of customers were unable to access their accounts, perform transactions, or receive salaries for several days.

The network failure exposed vulnerabilities in the bank's IT infrastructure and highlighted the critical importance of robust network management and backup systems in safeguarding financial data and ensuring continuity of banking operations.

### Data Synchronization Issues

Data synchronization issues arise when data stored in multiple locations—such as servers, databases, or devices—fails to update consistently and accurately across all systems. These inconsistencies can lead to outdated, conflicting, or incomplete information being used, which poses serious threats to data integrity and decision-making. Synchronization problems may occur due to network delays, software bugs, misconfigured sync settings, or interrupted processes. In critical systems, such issues can result in duplicated transactions, data loss, or system errors. To prevent these threats, organizations must use reliable synchronization protocols, ensure consistent time-stamping, and implement regular checks to detect and resolve discrepancies quickly.

**Data Synchronization Issues Example**

Another example of data synchronization issues risking data security is the [T-Mobile data breach in 2020](https://www.cpomagazine.com/cyber-security/second-data-breach-in-2020-for-t-mobile-exposed-customer-and-call-related-information-of-200000-subscribers/). 

The breach was attributed to issues in synchronizing customer data across different databases and systems. Attackers exploited these synchronization gaps, which resulted from complex data migration and integration processes within T-Mobile's infrastructure. This allowed unauthorized access to sensitive information, including personal data of over 200,000 customers. 

The incident exposed vulnerabilities in how data was managed and synchronized, highlighting the risks associated with inconsistent data replication and integration in large-scale IT environments.

### Lack of Proper Backups

A lack of proper backups poses a critical threat to data security, as it leaves organizations and individuals vulnerable to permanent data loss in the event of system failures, cyberattacks, accidental deletion, or natural disasters. Without reliable and up-to-date backups, it can be impossible to recover important files or restore operations after a disruption. This not only results in lost productivity and potential financial damage, but can also violate data protection regulations. Effective backup strategies—such as automated backups, off-site storage, and routine testing of recovery processes—are essential to ensure data can be restored quickly and accurately when needed.

**Lack of Proper Backups Example**

A famous example of data loss due to a lack of proper backups occurred in [2014 with the cloud storage provider, Code Spaces](https://www.breaches.cloud/incidents/codespaces/). 

In 2014, Code Spaces suffered a devastating attack when an attacker gained access to their Amazon Web Services (AWS) control panel. The attacker demanded a ransom, and when Code Spaces attempted to regain control, the attacker systematically deleted data and backups, effectively wiping out their entire infrastructure. 

Code Spaces had not maintained offsite backups or a robust backup strategy, leading to the irreversible loss of customer data. The severity of the attack and the lack of adequate backups forced Code Spaces to shut down permanently.

### Environmental Factors

Environmental factors such as temperature extremes, humidity, dust, and electromagnetic interference can pose serious threats to data security by damaging hardware components and disrupting normal system operations. Overheating can lead to hard drive failures, data corruption, or complete system crashes, while high humidity or dust build-up can cause short circuits and physical degradation of devices. Even subtle environmental changes can affect the reliability and longevity of data storage systems. To protect against these risks, organizations should maintain controlled environments for their IT infrastructure, including proper ventilation, air filtration, and environmental monitoring systems to detect and respond to harmful conditions promptly.

**Environmental Factors Example**

A notable example of data loss due to environmental conditions is the [2011 fire at the OVH data centre in Strasbourg, France](https://www.reuters.com/article/world/millions-of-websites-offline-after-fire-at-french-cloud-services-firm-idUSKBN2B20NT/). 

The fire was triggered by high humidity and electrical issues, leading to significant damage to the facility and its infrastructure. The incident resulted in the loss of customer data and disrupted services for many clients relying on OVH for hosting and cloud services. 

This event highlighted the critical importance of maintaining proper environmental controls, such as humidity and temperature regulation, and having robust disaster recovery plans to mitigate the impact of such incidents.

---

## Protecting Against Data Security Threats

Protecting against both malicious and non-malicious attacks involves a multi-layered approach that combines preventive measures, user education, and robust security practices:

### Software Measures

- **Install and Maintain Antivirus Software**: Use reputable antivirus and anti-malware programs to detect and remove malicious software. Ensure these programs are updated regularly to protect against the latest threats.
- **Regular Software Updates**: Keep all software, including operating systems, browsers, and plugins, up to date to patch vulnerabilities that malware could exploit.
- **Use Firewalls**: Implement network firewalls to block unauthorized access to your systems and monitor incoming and outgoing network traffic for suspicious activity.
- **Enable Email Filters**: Use email filtering tools to detect and block phishing emails and attachments that may contain malware.
- **Use Intrusion Detection and Prevention Systems (IDPS): Deploy IDPS to monitor network traffic for suspicious activity and potential intrusions, enabling prompt action to mitigate threats.
- **Behavioural Analytics**: Implement tools that use machine learning to analyse user behaviour and detect anomalies that may indicate insider threats
- **Prepared Statements**: Ensure that SQL queries are parameterized, which separates SQL code from data, making it impossible for an attacker to alter the query structure
- **Custom Error Messages**: Avoid exposing detailed error messages to users. Customize error messages to prevent attackers from gaining insights into the database structure.
- **Whitelisting**: Validate input against a list of allowed characters or patterns
- **Sanitize User Input**: Ensure all user input is sanitized to remove or encode any potentially harmful characters before processing.
- **Encode Output**: Encode all data before rendering it on the webpage to prevent the browser from interpreting it as executable code.
- **Use Secure Web Frameworks**: Utilize frameworks that have built-in protections against XSS, such as Ruby on Rails, Django, and Angular.
- **Encrypt Sensitive Data**: Ensure sensitive data is encrypted both at rest and in transit to protect it from unauthorized access.
- **Endpoint Security**: Use advanced EPP/EDR solutions to monitor and respond to suspicious activities on endpoints, leveraging behavioural analysis to identify potential zero-day exploits.
- **Synchronous Replication**: Use synchronous replication to ensure that data is written to multiple locations simultaneously, reducing the risk of discrepancies.
- **Automation Tools**: Use automated data synchronization tools and processes to reduce the risk of human error and ensure consistent data updates across systems.

### Hardware measures

- **Disconnect Infected Devices**: If a device is suspected to be infected with malware, disconnect it from the network immediately to prevent the spread to other systems.
- **RAID Configurations**: Use RAID (Redundant Array of Independent Disks) to create copies of data across multiple disks, so if one disk fails, data remains accessible.
- **High Availability**: Set up failover systems that automatically switch to a backup system in case of hardware failure, ensuring continuous data availability.
- **Battery Backup**: Deploy UPS systems to provide immediate, short-term power during an outage, allowing time for safe shutdown or switching to backup generators.
- **Long-term Power**: Install backup generators to supply power for extended periods during outages. Ensure they are regularly maintained and tested.
- **Proactive Monitoring**: Implement environmental monitoring systems to detect and alert for power issues, temperature fluctuations, and other environmental factors that could lead to hardware failure.
- **Scheduled Maintenance**: Perform regular network maintenance and updates to prevent failures due to outdated hardware or software. Ensure all network components are updated with the latest security patches.

### Networking measures

- **Email Authentication Protocols**: Use email authentication protocols to prevent email spoofing and ensure the integrity of email communications​.
- **Cloud-based DDoS Protection**: Services like Cloudflare, Akamai, and AWS Shield can absorb and mitigate DDoS traffic before it reaches your network.
- **Rate Limiting**: Configure your web server to limit the number of requests a user can make within a certain timeframe, helping to reduce the impact of DDoS attacks.
- **Redundancy and Load Balancing**: Distribute your infrastructure across multiple data centres and use load balancers to distribute traffic evenly, minimizing the risk of a single point of failure.
- **Scalable Bandwidth**: Work with your ISP to ensure you have sufficient bandwidth to handle unexpected traffic spikes and consider burstable bandwidth options.
- **Traffic Analysis**: Continuously monitor your network traffic to detect unusual patterns that may indicate an impending DDoS attack.
- **Network Segmentation**: Implement network segmentation to limit the spread of an attack. Use firewalls and access controls to restrict access to critical systems and data.
- **Distributed Data Centres**: Use geographically dispersed data centres to ensure that data and services remain available even if one location experiences a power outage.
- **Cloud Integration**: Utilize cloud services for data storage and critical applications, leveraging the redundancy and high availability provided by major cloud providers.
- **Implement Redundancy**: Ensure critical network components have backups. Use multiple ISPs, redundant routers, and switches to provide alternative paths for data if one fails.

### Policy measures

- **Educate Users**: Train employees and users to recognize phishing attempts, suspicious links, and unsafe downloads. Encourage the practice of not clicking on unknown or untrusted links and attachments.
- **Implement Strong Passwords and Multi-Factor Authentication (MFA): Use complex passwords and enable MFA to add an extra layer of security to accounts, making it harder for attackers to gain access.
- **Regular Backups**: Perform regular backups of critical data and store them securely. This ensures data can be restored in case of a ransomware attack or other data loss incidents.
- **Restrict User Privileges**: Limit user access to only the necessary systems and data required for their roles to minimize the impact of a potential malware infection.
- **Secure Browsing Practices**: Encourage users to hover over links to check the actual URL before clicking and to directly type URLs into the browser instead of clicking on links in emails​. Ensure websites use HTTPS to provide a secure connection, and educate users to look for the padlock icon in the browser address bar​.
- **Incident Response Plan**: Prepare a response strategy for dealing with phishing attacks, including steps for containing the breach, notifying affected parties, and recovering compromised accounts​.
- **Secure Wi-Fi Networks**: Avoid using public Wi-Fi for sensitive transactions. Use VPNs to encrypt traffic when accessing the internet through untrusted networks.
- **User Activity Monitoring**: Implement systems to monitor user activities and detect unusual or suspicious behaviour, such as excessive data downloads or access to unauthorized areas​.
- **Regular Audits**: Conduct regular audits of access logs and employee activities to identify and investigate potential insider threats
- **Data Protection Policies**: Develop and enforce comprehensive data protection policies that outline acceptable use of company resources and data
- **Data Loss Prevention (DLP): Use DLP solutions to detect and prevent unauthorized access, transfer, or use of sensitive data
- **Employee Engagement**: Promote a positive work environment and open communication to reduce grievances that may lead to insider threats
- **Anonymous Reporting Mechanisms**: Provide channels for employees to report suspicious activities anonymously, encouraging vigilance without fear of retribution
- **Restrict Database Permissions**: Ensure database accounts have the minimum necessary privileges. Avoid using administrative accounts for application connections.
- **Penetration Testing**: Conduct regular security audits and penetration tests to identify and mitigate vulnerabilities.
- **Code Reviews**: Perform thorough code reviews to ensure security best practices are followed.
- **Assess Vendors**: Conduct thorough security assessments and audits of all third-party vendors and partners to ensure they follow robust security practices.
- **Monitor Supply Chain**: Implement continuous monitoring of supply chain activities to detect unusual behaviours or anomalies
- **Reputable Sources**: Only source software, hardware, and services from reputable and trusted suppliers with a proven track record of security.
- **Comprehensive Plan**: Develop and test a disaster recovery plan that outlines procedures for data recovery and system restoration in the event of hardware failure.
- **Automated Testing**: Implement comprehensive automated testing, including unit tests, integration tests, and end-to-end tests, to catch bugs early in the development process.
- **Manual Testing**: Complement automated testing with thorough manual testing, particularly for complex or critical features.
- **Version Control Systems**: Use version control systems (e.g., Git) to track changes and enable easy rollback to previous versions if a bug is introduced.
- **Consistency Checks**: Perform regular data integrity and consistency checks on distributed databases (eg. Netflix) to identify and correct any synchronization issues promptly.
- **Conflict Detection and Resolution**: Implement conflict detection and resolution mechanisms to handle discrepancies that arise during data synchronization of distributed databases.
