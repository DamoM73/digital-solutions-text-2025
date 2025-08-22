# Networks 📝

:::{dropdown} Learning Goals
By the end of this section you will:
- understand the principles of transmitting data over a network
- understand the signficance network transmission concepts including latency, jitter, quality of service guarantee, and timeliness of delivery
- understand the TCP/IP, HTTP/HTTPS, FTP/FTPS, VPN, streaming, and broadcasting network transmission protocols  
- understand the methods of exchanging data including REST, JSON, XML and CSV/TSV
:::

Networks are the backbone of the modern world, but how do they work? Check the following videos to learn the fundamental about networking.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/3QhU9jd03a0?si=c15Ia4djP9A9xi-3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{tip} Crash Course Computer Networks Summary
:class: dropdown

- **Early Networks & Motivation:**
  - Pre-1970s, most computers were standalone. The need to share data and resources (printers, storage) drove network development.
  - Early methods like "Sneakernet" (physically moving storage media) were inefficient.
  - The first **Local Area Networks (LANs)** appeared in the 1950s/60s, typically within a single organization. A LAN can range from two computers in a room to a university campus.
- **Ethernet & Shared Media:**
  - **Ethernet**, developed at Xerox PARC in the 1970s, became a dominant LAN technology, initially using a shared cable.
  - **MAC Addresses (Media Access Control Address):** Each networked device has a unique MAC address. Data sent over Ethernet includes a header with the destination MAC address, so only the intended recipient processes it.
  - **Carrier Sense Multiple Access (CSMA):** To avoid "collisions" (multiple devices transmitting simultaneously and garbling data), devices "sense" (listen to) the carrier (shared cable or airwaves for Wi-Fi). If it's busy, they wait.
- **Collision Detection & Exponential Backoff:**
  - If two devices sense silence and transmit at the same time, a collision still occurs.
  - Devices can detect this collision, stop transmitting, wait a random period, and then try again.
  - To further manage this, they use **exponential backoff:** if another collision occurs, the wait time doubles (plus a random element) before retrying (e.g., 1s, then 2s, 4s, 8s). This helps alleviate network congestion.
  - **Bandwidth** is the rate at which a carrier can transmit data.
- **Scaling Networks: Switches & Collision Domains:**
  - Having too many devices on one shared carrier leads to frequent collisions.
  - The solution is to reduce the size of **collision domains** (the set of devices on a shared carrier).
  - **Network switches** connect multiple network segments. They learn which MAC addresses are on which segment and only forward data between segments if the destination is on a different segment. This allows multiple, non-interfering transmissions simultaneously on different parts of the network.
- **The Internet & Routing:**
  - The **Internet** is a network of interconnected networks.
  - **Routing** is the process of getting data from a source to a destination across these networks.
  - **Circuit Switching:** An early method, like old telephone systems, where a dedicated, exclusive physical circuit is established between two points for the duration of the communication. It's reliable but inefficient (unused capacity) and expensive.
  - **Message Switching:** Similar to the postal system. Messages are passed from one intermediate "hop" (e.g., a mail hub, or a network router) to the next. Each hop knows where to send it next based on the destination. This is more fault-tolerant; if one route is blocked (e.g., a blizzard), an alternative route can be used.
    - **Hop Count:** The number of hops a message takes. A **Hop Limit** prevents messages from looping endlessly in case of routing errors.
- **Packet Switching & IP Addresses:**
  - A downside of message switching is that large messages can tie up links.
  - **Packet Switching** is the solution: large transmissions are chopped into small, fixed-size **packets**.
  - Each packet contains a destination address on the network. This format is defined by the **Internet Protocol (IP)**.
  - Every computer on a network gets an **IP Address** (e.g., 172.217.7.238 for a Google server), typically four 8-bit numbers separated by dots.
  - Routers forward packets, and different packets from the same message can take different routes. This is efficient and fault-tolerant.
- **ARPANET & Decentralization:**
  - The world's first packet-switched network and the ancestor of the modern internet was **ARPANET**, funded by the US Advanced Research Projects Agency (ARPA) during the Cold War.
  - Packet switching's decentralized nature made it robust against potential attacks on central points.
  - The ARPANET in 1974 connected a few dozen computers; today, the internet connects nearly 10 billion devices, including the **Internet of Things** (smart fridges, thermostats, etc.).
:::

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/AEaKrq3SpW8?si=gVh5_2f8jmQfuNen" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{tip} Crash Course The Internet Summary
:class: dropdown

- **Network Structure:** The internet is made up of many connected devices. Your device connects to a Local Area Network (LAN), like your home Wi-Fi. That LAN connects to a bigger network called a Wide Area Network (WAN), managed by your Internet Service Provider (ISP). Data moves through several routers and eventually passes through high-speed connections that make up the internet’s core.
- **Data Transmission and Packets:** Information travels as small chunks called packets. When you request something online—like a video—your device sends a packet to the server. The server then responds by sending the data back in many small packets. You can view the path your packets take using a command like `traceroute`.
- **Internet Protocol (IP):** Every packet follows a standard called the Internet Protocol. An IP packet contains a header (with details like the destination IP address) and a data section (the content being sent).
- **User Datagram Protocol (UDP):** UDP is a fast and simple way to send data. It includes a port number to direct the packet to the correct program and a checksum to check for errors. UDP does not guarantee delivery or correct errors—it just drops any broken packets. It’s used for things where speed matters more than accuracy, like live video or voice chat.
- **Transmission Control Protocol (TCP):** TCP is used when it’s important that all data arrives complete and in the right order, like for email or loading websites. It adds features like numbering packets and requiring the receiver to confirm they were received. If something goes missing, it’s resent.
- **Domain Name System (DNS):** DNS translates website names (like google.com) into IP addresses that computers can use. When you enter a website address, your device contacts a DNS server to find out its IP address. DNS is organized into levels, starting with top-level domains like `.com`, then more specific domain names.
- **OSI Model:** All of this fits into the OSI model, which breaks down how networks work into layers. This includes the Physical, Data Link, Network, Transport, and Session layers, each handling a specific part of the communication process.
:::

:::{seealso} Traceroute (Doobly Doo)
:class: dropdown
Want to run traceroute on your computer? See directions below. Remember you can replace "dftba.com" with whatever website you want!

Traceroute on Windows

1. Press the Start Button
2. Type "CMD" and press "Enter"
3. In the Command Prompt type "tracert dftba.com"

   Traceroute on Mac
4. Click on the "Go" drop down menu
5. Click on "Utilities"
6. Open Terminal
7. Type "traceroute dftba.com"
:::

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/guvsH5OFizE?si=-qBwz9LiQseDuxeH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{tip} Crash Course World Wide Web Summary
:class: dropdown
**The Internet vs. The Web**

- **The Internet** is the global network that connects computers and devices around the world.
- **The World Wide Web** is one of the services that runs on the Internet. It’s a huge system of connected websites and pages that let people share and access information.

**Hypertext and Hyperlinks**

- Websites are made of **hypertext documents**, which are just pages with text, images, and other content.
- These pages are connected using **hyperlinks**, which let users click to move from one page to another.
- The idea of linking information this way was first imagined back in 1945 by a scientist named Vannevar Bush.

**How the Web Works (Protocols and Standards)**

- **URL (Uniform Resource Locator):** This is the unique address of a webpage, like `http://www.example.com/page.html`.
- **HTTP (Hypertext Transfer Protocol):** This is the system that web browsers and servers use to talk to each other. It includes commands like `GET` to request a page, and responses like `200 OK` (success) or `404 Not Found`.
- **HTML (Hypertext Markup Language):** This is the code used to create webpages. It uses tags like `<h1>` for headings, `<a>` for links, and `<li>` for list items.

**History and Key People**

- **Tim Berners-Lee** created the World Wide Web in 1990 while working at CERN. He also created the first web browser, the first web server, and the first versions of URL, HTML, and HTTP.
- The **Mosaic browser**, released in 1993, was the first to show images alongside text. It helped make the web more popular.

**Search Engines**

- As the Web got bigger, it became harder to find things. At first, there were human-made lists of sites, like early Yahoo!.
- Then came **search engines**, which automatically searched the web.
  - They use **web crawlers** to find pages by following links.
  - They store what they find in an **index**.
  - They use a **search algorithm** to show the most relevant results.
  - **Google** improved search results by creating **PageRank**, a system that ranks pages higher if other important pages link to them.

**Net Neutrality**

- **Net neutrality** is the idea that Internet Service Providers (ISPs) must treat all internet data equally.
- That means they can’t slow down, block, or speed up certain websites or services.
- Some people support it to keep the internet fair and open. Others think ISPs should be allowed to manage their networks how they want.
:::

## Network Transmission Principles 📝

Network transmission principles are fundamental concepts in networking that govern how data is sent and received across computer networks. These principles are essential for understanding how information flows efficiently and reliably over the internet and other network infrastructures.

### Latency

Latency refers to the delay or lag that occurs when data is transmitted from one point to another in a network. It can be caused by various factors:

- **Serialization and deserialization:**
  - Serialization is the process of converting data into a format that can be transmitted over a network.  
  - Deserialization is the reverse process.  
  - The serialization and deserialization steps introduce overhead, contributing to latency. The more complex the data and the longer the serialization process takes.
- **Propagation:**
  - Propagation delay in networks refers to the time it takes for data to travel from its source to its destination over a physical medium, such as a network cable or a fibre optic line.  
  - In networks, this delay is influenced by the physical distance between devices and the speed at which signals can travel through the medium.
- **Switching:**
  - When data is sent across a network, it's broken into smaller packets, and these packets need to find their way to the right destination.  
  - Switches make this happen efficiently. They determine the best path for each packet, helping them avoid traffic jams and collisions.  
  - To direct packets, switches need to inspect each packet. Each inspection accrues overhead, therefore latency is impacted by both the number of switches each packet passes through, and the speed of those switches.
- **Queuing:**
  - When lots of data packets arrive at a network device like a router, they might have to wait their turn before they can continue on their journey. This waiting time is called queuing delay.  
  - Low queuing delay means faster data transmission, inversely, high queuing delay can slow down data delivery.  

Low latency is crucial for real-time applications like video conferencing and online gaming, where delays can lead to a poor user experience.

:::{hint} Gaming Ping and Latency
:class: dropdown
Gaming ping is directly affected by latency. Ping is a measurement of the round-trip time it takes for a small packet of data (called a ping packet) to travel from your computer to a game server and back. Latency, often referred to as "ping" in gaming, represents the time delay between sending a command in the game and seeing its effect on the screen.
:::

### Jitter

Jitter is the variation in the delay of received packets in a network. It represents the inconsistency in the timing of packet arrivals. It can result from network congestion, varying path lengths for different packets, or differences in the processing time at network devices.

In applications like Voice over IP (VoIP) and streaming media, jitter can lead to disruptions and poor audio or video quality. Minimizing jitter is essential for smooth communication.

:::{hint} Jitter in video streaming
:class: dropdown
In video streaming, jitter appears as irregular and unexpected variations in the timing of frame delivery. It's typically manifested as noticeable fluctuations in the smoothness of video playback. Here's what jitter looks like in video streaming:

1. **Stuttering or Freezing:** One common symptom of jitter is when the video playback briefly stutters or freezes. You might see the video pause for a moment and then catch up suddenly.
2. **Uneven Playback Speed:** Jitter can cause the video to play back at uneven speeds. It may briefly speed up or slow down, making the motion appear unnatural.
3. **Frame Drops:** Jitter can result in frames being dropped during playback. This can lead to missing content or jerky movements in the video.
4. **Audio-Video Desynchronization:** Jitter can also affect the synchronization between the audio and video components of a stream. You might notice that the audio lags behind or leads the video.
5. **Pixelation and Artifacts:** In severe cases, jitter can cause pixelation or compression artifacts in the video, making the image quality deteriorate momentarily.
6. **Buffering Delays:** To compensate for jitter, video streaming services may introduce buffering delays. This means you have to wait longer for the video to start playing, which can be frustrating for viewers.
:::

### Quality of Service (QoS) Guarantee

Network **Quality of Service (QoS) guarantee** refers to the assurance that a network can provide specific levels of service and performance to different types of traffic or applications. QoS is critical in ensuring that data, voice, video, and other applications receive the necessary bandwidth, low latency, and minimal packet loss to function effectively.

To guarantee QoS, networks often employ various mechanisms, such as traffic prioritization, bandwidth reservation, and congestion management. For example, in a VoIP (Voice over Internet Protocol) call, QoS guarantee ensures that voice packets are prioritized over less time-sensitive data packets, reducing the chances of voice call degradation due to network congestion.

### Timeliness of delivery

The principle of **timeliness of delivery** in networking refers to the requirement that data should be delivered within a timeframe suitable for its intended use. This is crucial for ensuring that the information remains relevant and useful by the time it reaches its destination.

:::{seealso} Network Transmission Principles Activities
:class: dropdown
1. What is latency in networking and why is it important for online gaming?
2. Identify two causes of latency and explain them.
3. Define jitter and describe how it affects video streaming.
4. Give one network condition that increases jitter.
5. What does a Quality of Service (QoS) guarantee mean in networking?
6. Explain why QoS is important for a VoIP call.
7. What is meant by timeliness of delivery in networks?
8. Give an example of when timeliness of delivery is critical.
:::

## Network Transmission Protocols 📝

### TCP/IP 📝

**TCP/IP** stands for **Transmission Control Protocol / Internet Protocol**. It is the core set of communication rules (called a **protocol suite**) that computers use to send and receive data over networks, including the **internet**.

Developed in the 1970s, TCP/IP is now the **standard for all internet communication**.

**TCP/IP Protocol Layers**

TCP/IP is made up of **four layers**. Each layer has its own job:

1. **Application Layer**

   - Deals with **applications and user services**
   - This is the layer you interact with (e.g., web browsers, email clients)
   - Protocols here:
     - **HTTP/HTTPS** – web browsing
     - **SMTP** – sending emails
     - **IMAP/POP3** – receiving emails
     - **FTP** – file transfer

2. **Transport Layer**

   - Manages the **delivery of data**
   - Breaks data into chunks (called **segments**) and reassembles them
   - Handles error checking and flow control
   - Two main protocols:
     - **TCP** – Reliable, ordered delivery (used for most things)
     - **UDP** – Faster, no guarantee of delivery (used for games, video calls)

3. **Internet Layer**

   - Handles **routing** of data between devices across networks
   - Breaks data into **packets** and labels them with IP addresses
   - Protocols here:
   - **IP** – Internet Protocol (IPv4 and IPv6)
   - **ICMP** – for sending error and control messages (used by `ping`)

4. **Network Access Layer** (Link Layer)

   - Manages how data is sent **physically** over the network (wires, Wi-Fi, etc.)
   - Converts packets into electrical signals or radio waves
   - Protocols: Ethernet, Wi-Fi, ARP

**How TCP/IP Works (Step-by-Step)**

1. **User Action**: You enter `www.example.com` in your browser.
2. **DNS Lookup**: Your computer gets the IP address for the website using DNS.
3. **Data Preparation**: Your browser sends an HTTP request (application layer).
4. **TCP Adds Reliability**: The data is split into segments with error checks.
5. **IP Handles Routing**: Each segment is wrapped in an IP packet and given a destination IP.
6. **Data Sent Over Network**: Packets travel through routers and switches.
7. **Receiving End**: The server reassembles the segments and sends back a response.
8. **Browser Displays Page**: You see the website once all the data is received.

**TCP vs UDP Comparison**

| Feature   | TCP                            | UDP                              |
| --------- | ------------------------------ | -------------------------------- |
| Delivery  | Reliable (resends lost data)   | Unreliable (no resending)        |
| Order     | Keeps order                    | No guarantee of order            |
| Speed     | Slower (due to checking)       | Faster                           |
| Use cases | Web browsing, email, downloads | Video calls, games, live streams |

### What is IP?

**IP (Internet Protocol)** is a **network layer protocol** that handles **addressing and routing** of data between devices on a network. It ensures that packets of data are sent from the sender to the correct destination.

Every device on a network — like your phone, laptop, or a website server — is assigned a unique **IP address**, which acts like a digital address so the internet knows where to send information.

**IP is responsible for**
1. **Addressing**

   - Every device must have a unique **IP address**.
   - IP addresses identify the **sender** and the **receiver** of data.

2. **Packetization**

   - IP splits data into small units called **packets**.
   - Each packet includes:
     - **Sender IP address**
     - **Destination IP address**
     - Other information (e.g. time to live)

3.  **Routing**

   - Packets may travel through many routers across different networks.
   - Each router checks the **destination IP** and forwards the packet toward its target.
   - The path may not be the same for each packet — they can take different routes.

4.  **Delivery (Best-Effort)**

   - IP does not guarantee delivery.
   - Packets can be **lost**, **duplicated**, or **arrive out of order**.
   - That’s why **TCP** is often used on top of IP to ensure reliable delivery.

**Types of IP Addresses**

- **IPv4** (Internet Protocol version 4)
  - Most common version
  - Written in **4 numbers separated by dots**
  - Example: `192.168.1.1`
  - Uses **32 bits**, allowing about **4.3 billion** addresses
  - Running out of available addresses

- **IPv6** (Internet Protocol version 6)
  - Newer version designed to replace IPv4
  - Written in **8 groups of hexadecimal numbers**
  - Example: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
  - Uses **128 bits**, allowing **trillions of addresses**
  - Supports more devices and improved security

**Static vs Dynamic IP Addresses**

| Type           | Description                                       |
| -------------- | ------------------------------------------------- |
| **Static IP**  | Does not change. Manually set. Used for servers.  |
| **Dynamic IP** | Changes over time. Assigned by DHCP. Most common. |

**IP Header**

Every IP packet includes a **header** with important information:
- **Version** (IPv4 or IPv6)
- **Source IP address**
- **Destination IP address**
- **Time to Live (TTL)** – how many hops (routers) the packet can go through before being dropped
- **Protocol** – tells what’s inside (e.g., TCP, UDP)

### HTTP / HTTPS 📝

**HTTP (Hypertext Transfer Protocol)** and **HTTPS (Hypertext Transfer Protocol Secure)** are both protocols used for transferring data between a web browser (client) and a web server. The primary difference lies in security and data protection.

**Key Differences**

| Feature | HTTP | HTTPS |
|--- |--- |--- |
| Full Name | Hypertext Transfer Protocol | Hypertext Transfer Protocol Secure |
| Security | No encryption; data sent in plain text | Data encrypted using SSL/TLS |
| Default Port | 80 | 443 |
| Data Protection | Vulnerable to interception and tampering | Protects against eavesdropping and tampering |
| Server Authentication | No verification of server identity | Uses digital certificates to verify server |
| URL Prefix | http:// | https:// |
| Use Case | General browsing, non-sensitive data | Sensitive data (logins, payments, personal) |
| SEO Benefit | No boost | Preferred by search engines |

:::{hint} What is a Port?
:class: dropdown
A **computer port** is a number that helps computers know which program or service a piece of network data is meant for.

When data comes into your device (like a web page or a message), it’s sent to a specific **IP address** and a specific **port number**. The IP address identifies the device, and the port number identifies the application or service.

**Why Are Ports Needed?**
A single computer can run many programs at the same time—like a web browser, email client, and video game.
**Ports** help keep the traffic organized by assigning a number to each type of service.

- Data coming into your computer must be directed to the correct software.
- The operating system checks the **port number** and passes the data to the matching program.

**Common Port Numbers**
Some port numbers are **standardized**, meaning certain services always use the same ones:

| Port Number | Protocol / Service |
| --- | --- |
| 20, 21 | FTP (File Transfer Protocol) |
| 22 | SSH (Secure Shell) |
| 23 | Telnet |
| 25 | SMTP (Sending email) |
| 53 | DNS (Domain Name System) |
| 80 | HTTP (Web pages) |
| 443 | HTTPS (Secure web pages) |
| 110 | POP3 (Receiving email) |
| 143 | IMAP (Receiving email) |
:::

- **HTTP** is fast and suitable for non-sensitive information, but it is not secure—data can be intercepted or altered by third parties.
- **HTTPS** is essential for protecting sensitive data, preventing "man-in-the-middle" attacks, and building user trust.
- Modern browsers display a padlock icon for HTTPS sites, signalling a secure connection, and may warn users when a site is not secure.

**Basic Workflow**

1. **Connection Establishment:** The client initiates a TCP connection to the server. HTTP typically operates over TCP/IP and uses port 80 for standard HTTP connections.
2. **Request-Response Cycle:**

   - **Request:** Once the TCP connection is established, the client sends an HTTP request to the server. This request includes:
     - a request line (method, URL, HTTP version)
     - headers (host, user-agent, content-type, etc.)
     - sometimes a body (for methods like POST or PUT)
   - **Response:** The server processes the request and sends back an HTTP response. This response contains:
     - a status line (HTTP version, status code, status message)
     - response headers (content-type, content-length, server, etc.)
     - often a body containing the requested resource or data

3. **Connection Closure:** After the response is delivered, the connection can be closed, or kept open for further requests if the header Connection: keep-alive is used.

   **HTTP Methods**

- **GET:** Requests the specified resource. GET requests should only retrieve data and should have no other effect.
- **POST:** Submits data to be processed (e.g., from a form). The server may create or update resources based on the data provided.
- **PUT:** Replaces the current target resource with the request payload.
- **DELETE:** Removes the specified resource.
- **HEAD:** Similar to GET, but it retrieves only the status line and header section.
- **OPTIONS:** Describes the communication options for the target resource.
- **PATCH:** Applies partial modifications to a resource.

**Status Codes**

HTTP responses come with status codes that indicate the outcome of the request:

- **2xx (Success):** Indicates that the client's request was successfully received, understood, and accepted (e.g., 200 OK, 201 Created).
- **3xx (Redirection):** Indicates that further action needs to be taken by the client in order to complete the request (e.g., 301 Moved Permanently, 302 Found).
- **4xx (Client Error):** Indicates an error that seems to have been caused by the client (e.g., 404 Not Found, 403 Forbidden).
- **5xx (Server Error):** Indicates an error on the server side (e.g., 500 Internal Server Error, 503 Service Unavailable).

### FTP / FTPS 📝

**FTP**

**FTP** stands for **File Transfer Protocol**. It's one of the oldest protocols used to transfer files between two computers over a **TCP/IP network** (like the internet).

**How It Works:**

- FTP uses a **client-server model**.
  - The **FTP client** is the program you use to connect (e.g. FileZilla, Cyberduck, or even a terminal command).
  - The **FTP server** hosts files and handles file transfer requests.
- To connect, you provide:
  - A **server address** (like `ftp.example.com`)
  - A **username** and **password**
- Once connected, you can:
  - Browse directories
  - Upload files from your computer to the server
  - Download files from the server to your computer
  - Rename, delete, or move files

**Security**
FTP is **not secure** by default:
- Your username and password are sent **in plain text**.
- Files are transferred **without encryption**.
- Anyone using a network sniffer (like Wireshark) could intercept and read your data.

**FTPS**

**FTPS** stands for **FTP Secure** or **FTP over SSL/TLS**.

- It adds **encryption** using **SSL (Secure Sockets Layer)** or **TLS (Transport Layer Security)**.
- The encryption protects:
  - Login credentials
  - File data during transfer
- FTPS supports both:
  - **Implicit FTPS** (uses port 990; encryption starts immediately)
  - **Explicit FTPS** (uses port 21; client asks for encryption after connecting)

**Benefits of FTPS:**

- Secure transmission of sensitive files (e.g. medical data, financial documents)
- Authentication using **certificates** (optional, for extra security)
- Often used by businesses and government systems that require encrypted file transfer

### VPN

A **VPN (Virtual Private Network)** keeps your internet connection private and secure. It uses **protocols** to create a safe tunnel for your data.

Here are the most common VPN protocols:

- **PPTP (Point-to-Point Tunneling Protocol)**
  - Very old and fast
  - Easy to set up
  - Weak security — not recommended
- **L2TP/IPsec**
  - Combines two protocols for better security
  - Safer than PPTP
  - Slower, but more secure
- **OpenVPN**
  - Very secure and reliable
  - Can work on most networks
  - A bit slower but very safe
- **IKEv2/IPsec**
  - Fast and stable
  - Great for phones and tablets
  - Handles switching Wi-Fi and mobile data well
- **WireGuard**
  - New and very fast
  - Uses strong, modern security
  - Still being adopted by some platforms

| Protocol | Speed | Security | Best For |
| --- | --- | --- | --- |
| PPTP | ✅ Fast | ❌ Weak | Old systems (not safe) |
| L2TP/IPsec | ⚠️ Okay | ✅ Good | Better security |
| OpenVPN | ⚠️ Okay | ✅ Great | Most safe setups |
| IKEv2/IPsec | ✅ Fast | ✅ Great | Phones and mobile use |
| WireGuard | ✅ Fast | ✅ Great | Modern, future VPNs |

### Streaming 📝

**Streaming protocols** are rules that control how audio and video are sent over the internet so that people can watch or listen in **real time** without downloading the entire file first.

There are two main types:
- **Live streaming** – real-time content like live events or games
- **On-demand streaming** – videos or music you can play anytime (e.g. YouTube, Netflix)

**Common Streaming Protocols**

- **HTTP Live Streaming (HLS)**
  - Created by Apple
  - Breaks video into small chunks and sends them one at a time
  - Works well on phones, computers, and smart TVs
  - Can change quality depending on your internet speed (adaptive streaming)
- **Dynamic Adaptive Streaming over HTTP (MPEG-DASH)**
  - Similar to HLS but not Apple-specific
  - Also uses small chunks and adaptive quality
  - Works across many devices and platforms
- **Real-Time Messaging Protocol (RTMP)**
  - Older protocol made by Adobe
  - Used for low-latency (fast) live streaming
  - Often used to send live video from streamers to platforms like Twitch or YouTube
- **WebRTC (Web Real-Time Communication)**
  - Used for real-time communication like video calls (e.g., Zoom or Google Meet)
  - Very low latency (almost no delay)
  - Doesn’t need extra plugins or apps—works in modern browsers

| Protocol  | Best For | Key Features |
| --- | --- | --- |
| HLS | Live & on-demand | Widely supported, adaptive quality |
| MPEG-DASH | On-demand | Open standard, flexible |
| RTMP | Live streaming | Low delay, used for uploading video |
| WebRTC | Video calls | Real-time, works in browsers |

### Broadcasting 📝

**Broadcast protocols** are ways of sending data from one device to **many devices at once** on a network. They are used when the same message needs to reach a group of devices without sending it separately to each one.

**How Broadcasting Works**

- In a broadcast, data is sent to **all devices** on a local network. Each device checks the message to see if it’s meant for them.
- Broadcasting is usually only used in **Local Area Networks (LANs)**—not across the internet—because it creates a lot of traffic if overused.

**Common Broadcast Protocols**

- **ARP (Address Resolution Protocol)**
  - Used to find the **MAC address** of a device when you only know its **IP address**
  - Sends a broadcast message to the whole network asking, "Who has this IP?"
- **DHCP (Dynamic Host Configuration Protocol)**
  - Used to assign IP addresses to devices automatically
  - When a new device connects to the network, it broadcasts a message asking for an IP address
  - A **DHCP server** responds with an available address
- **NetBIOS**
  - Used in older Windows networks to share files and printers
  - Broadcasts names of devices to find others on the local network

| Type | Description |
| --- | --- |
| **Unicast** | One-to-one (sent to a single device) |
| **Broadcast** | One-to-all (sent to every device on LAN) |
| **Multicast** | One-to-many (sent to a specific group) |

:::{seealso} Network Transmission Protocols Activities
:class: dropdown
1. What does TCP/IP stand for and why is it important?
2. Name the four TCP/IP layers and briefly describe one.
3. Compare TCP and UDP with one use case for each.
4. What is the main role of the Internet Protocol (IP)?
5. Explain the difference between IPv4 and IPv6.
6. Why is TCP often used together with IP?
7. State one key difference between HTTP and HTTPS.
8. Give an example of when HTTPS is essential and explain why.
9. What does a browser’s padlock icon mean?
10. What is the main function of FTP?
11. Why is FTPS more secure than FTP?
12. What does a VPN do?
13. Name one VPN protocol suitable for mobile devices and explain why.
14. What is the main difference between live streaming and on-demand streaming?
15. Which streaming protocol is best for video calls and why?
16. What is the difference between unicast, broadcast, and multicast?
17. Which broadcast protocol is used to automatically assign IP addresses to new devices on a network?
18. What is the purpose of ARP?
:::

## Data Exchange Methods 📝

### REST (Representational State Transfer) 📝

REST is an architectural style for designing networked applications. It relies on a **stateless**, **client-server**, **cacheable communications protocol** &mdash; the HTTP (Hypertext Transfer Protocol).  

**RESTful** systems use HTTP requests to perform CRUD (Create, Read, Update, Delete) operations on resources.

**Key Concepts**

- **Resources:** Resources are typically data objects or services and can be accessed using a unique URL.
- **HTTP Methods:** REST uses standard HTTP methods to perform operations on resources.
- **Stateless Communication:** The server does not store any state about the client session on its end, therefore each request from a client to a server must contain all the information the server needs to understand and process the request.
- **Representation:** Resources are represented in different formats, usually JSON (JavaScript Object Notation) or XML (eXtensible Markup Language).
  - The client requests a resource and the server responds with the resource's current state in one of these formats.

**Example of Data Exchange Using REST:**

- **GET Request:**
  - A client wants to retrieve information about a book with the ID 123.
  - The client sends a GET request to the server at the URL: `http://api.library.com/books/123`.
    - The server responds with the book's details in JSON format:

     ```{code} json
     {
       "id": 123,
       "title": "Introduction to Programming",
       "author": "John Doe",
       "year": 2020
     }
     ```

- **POST Request:**
  - A client wants to add a new book to the library.
  - The client sends a POST request with the book's data to the URL: `http://api.library.com/books`.
  - The server processes the request and adds the book to the database, responding with the created book's details:

     ```{code} json
     {
       "id": 124,
       "title": "Advanced Programming",
       "author": "Jane Smith",
       "year": 2021
     }
     ```

- **PUT Request:**
  - A client wants to update the information of an existing book with the ID 123.
  - The client sends a PUT request with the updated data to the URL: `http://api.library.com/books/123`.
    - The server updates the book information and responds with the updated details:

     ```{code} json
     {
       "id": 123,
       "title": "Introduction to Programming - 2nd Edition",
       "author": "John Doe",
       "year": 2022
     }
     ```

- **DELETE Request:**
  - A client wants to delete a book with the ID 123.
  - The client sends a DELETE request to the URL: `http://api.library.com/books/123`.
  - The server deletes the book and confirms the deletion:

     ```{code} json
     {
       "message": "Book with ID 123 has been deleted."
     }
     ```

### JSON 📝

**JSON (JavaScript Object Notation)** is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It's widely used in web applications to send and receive data between a server and a client.

**Key Features of JSON**

- **Simplicity:**
  - JSON syntax is straightforward and easy to understand.
  - It is text-based, making it readable for humans.
- **Language Independence:**
  - Although it originates from JavaScript, JSON is language-agnostic.
  - It is supported by most programming languages, either natively or through libraries.
- **Lightweight:**
  - JSON data is compact and can be easily transmitted over networks, making it efficient for data exchange.

**JSON Structure**

JSON data is represented as key-value (called dictionaries in Python) pairs organized in a hierarchical structure. The basic building blocks of JSON are:

- **Objects:**
  - Enclosed in curly braces `{}`.
  - Contain a set of key-value pairs.
  - Keys are strings, and values can be strings, numbers, objects, arrays, `true`, `false`, or `null`.
    - Example:

     ```{code} json
     {
       "name": "John Doe",
       "age": 30,
       "isStudent": false
     }
     ```

- **Arrays:**
  - Enclosed in square brackets `[]`.
  - Contain a list of values.
    - Values can be of any JSON data type.
    - Example:

     ```{code} json
     {
       "students": ["Alice", "Bob", "Charlie"]
     }
     ```

- **Values:**
  - Can be strings, numbers, objects, arrays, Booleans (`true` or `false`), or `null`.
  - Strings are enclosed in double quotes.
  - Numbers can be integers or floating-point.
  - Example:

     ```{code} json
     {
       "name": "John Doe",
       "age": 30,
       "height": 5.75,
       "isStudent": false,
       "courses": null
     }
     ```

**JSON Example**

Here’s a complete example representing a student record:

```{code} json
{
  "student": {
    "id": 12345,
    "name": "John Doe",
    "age": 21,
    "isEnrolled": true,
    "courses": [
      {
        "courseName": "Mathematics",
        "courseCode": "MATH101",
        "credits": 3
      },
      {
        "courseName": "English Literature",
        "courseCode": "ENG201",
        "credits": 4
      }
    ],
    "contact": {
      "email": "john.doe@example.com",
      "phone": "555-1234"
    }
  }
}
```

**JSON usage**

- **APIs:** JSON is commonly used in RESTful APIs to exchange data between clients and servers.
- **Configuration Files:** Many software applications use JSON for configuration due to its readability and ease of parsing.
- **Data Storage:** JSON can be used to store data in databases, especially in NoSQL databases like MongoDB.
- **Web Development:** Web applications use JSON to transmit data asynchronously between the server and the client, often with technologies like AJAX.

**JSON advantages**

- **Readability:** JSON is easy to read and write for humans, making it straightforward to debug and understand.
- **Lightweight:** JSON's simple syntax results in smaller data sizes compared to XML, which reduces the bandwidth needed for data transfer.
- **Language Independence:** JSON is language-agnostic and can be parsed and generated by many programming languages, including JavaScript, Python, Java, and many others.
- **Integration with JavaScript:** JSON is native to JavaScript, making it highly efficient for web applications and seamless integration with web technologies.
- **Structured Data:** JSON's hierarchical structure allows for the representation of complex data relationships, making it suitable for a wide range of applications, from simple to complex data interchange formats.
- **Support for Data Types:** JSON supports common data types such as strings, numbers, arrays, objects, Booleans, and null, providing flexibility in data representation.
- **Widespread Adoption:** JSON is widely supported by web services and APIs, making it a standard choice for data exchange in modern web development.

**JSON disadvantages**

- **Limited Data Types:** JSON supports only a few basic data types (strings, numbers, Booleans, arrays, and objects), which may not be sufficient for more complex data representations.
- **No Schema Validation:** JSON lacks a built-in schema, which can lead to data consistency issues since there is no enforced structure, making it challenging to validate the data format.
- **Verbose for Complex Structures:** While lightweight for simple data, JSON can become verbose and less efficient for very complex or deeply nested structures, leading to increased parsing and processing time.
- **Security Vulnerabilities:** JSON parsing, especially in JavaScript, can be susceptible to security risks such as injection attacks if not properly sanitized and validated.
- **Binary Data Handling:** JSON is not suitable for directly handling binary data, often requiring encoding (like Base64) which increases the size of the data.
- **Lack of Comments:** JSON does not support comments, making it harder to document or annotate data within the JSON itself for future reference or understanding.

### XML 📝

**XML (eXtensible Markup Language)** is a versatile and widely-used format for storing and transporting data. Unlike JSON, which is primarily used for data interchange, XML is more commonly used for document storage, configuration files, and data interchange in enterprise systems.

**Key Features of XML**

- **Self-Descriptive:**
  - XML documents are self-descriptive, meaning they include metadata about the data they contain.
  - Each element is identified by a tag, making it clear what data is being represented.
- **Hierarchical Structure:**
  - XML documents have a tree-like structure with nested elements.
  - This hierarchical nature makes it easy to represent complex data relationships.
- **Extensibility:**
  - XML is extensible, allowing users to define their own tags.
  - This flexibility makes XML suitable for a wide range of applications.
- **Human and Machine Readable:**
  - XML documents are both human-readable and machine-readable.
  - They use plain text, making it easy to view and edit with a simple text editor.

**XML Structure**

- **Elements:**
  - Enclosed in opening and closing tags `<tag>` and `</tag>`.
  - Can contain text, attributes, other elements, or a combination of these.
  - Example:

     ```{code} xml
     <book>
       <title>Introduction to Programming</title>
       <author>John Doe</author>
       <year>2020</year>
     </book>
     ```

- **Attributes:**
  - Provide additional information about elements.
  - Placed within the opening tag of an element.
  - Example:

     ```{code} xml
     <book id="123">
       <title>Introduction to Programming</title>
       <author>John Doe</author>
       <year>2020</year>
     </book>
     ```

- **Prolog:**
  - The prolog is an optional part of the XML document that can contain an XML declaration and processing instructions.
  - The XML declaration specifies the version of XML and the character encoding used in the document.
  - Example:

     ```{code} xml
     <?xml version="1.0" encoding="UTF-8"?>
     ```

**XML Example**

Here’s a complete example representing a student record in XML:

```{code} xml
<?xml version="1.0" encoding="UTF-8"?>
<student>
  <id>12345</id>
  <name>John Doe</name>
  <age>21</age>
  <isEnrolled>true</isEnrolled>
  <courses>
    <course>
      <courseName>Mathematics</courseName>
      <courseCode>MATH101</courseCode>
      <credits>3</credits>
    </course>
    <course>
      <courseName>English Literature</courseName>
      <courseCode>ENG201</courseCode>
      <credits>4</credits>
    </course>
  </courses>
  <contact>
    <email>john.doe@example.com</email>
    <phone>555-1234</phone>
  </contact>
</student>
```

**XML usage**

- **Document Storage:** XML is often used to store configuration files and data files.
- **Data Interchange:** XML is used to exchange data between different systems and platforms.
  - Example: Web services often use XML-based protocols like SOAP (Simple Object Access Protocol) to communicate.
- **RSS Feeds:** XML is used to create RSS feeds, which are used to distribute updated content from websites.
  - Example: News websites and blogs often provide RSS feeds in XML format.
- **Document Formats** XML serves as the basis for various document formats.

**XML advantages**

- **Versatility:** XML can represent complex data structures and is suitable for a wide range of applications.
- **Standardization:** XML is a W3C standard, ensuring consistency and interoperability across different systems.
- **Self-Descriptive:** XML documents are self-descriptive, making them easy to understand and maintain.

**XML Disadvantages**

- **Verbosity:** XML can be quite verbose, leading to larger file sizes compared to more concise formats like JSON.
- **Parsing Overhead:** XML parsing can be computationally intensive, especially for large documents.

### CSV & TSV

**CSV (Comma-Separated Values)** and **TSV (Tab-Separated Values)** are both formats used for storing and exchanging tabular data in a plain text format. In a CSV file, each line corresponds to a row of data, and each value in the row is separated by a comma. TSV is similar to CSV, but instead of commas, tabs are used to separate values.

**CSV & TSV Key Features**

- **Simplicity:**
  - Easy to read and write by both humans and machines.
- **Compatibility:**
  - Supported by most spreadsheet programs like Microsoft Excel, Google Sheets, and database management systems.
- **Flexibility:**
  - Can store data of various types, including text and numbers.
- **Plain Text:**
  - Data is stored in a simple text format, making it easy to handle and manipulate.
- **Data Import/Export:**
  - These formats are commonly used for importing and exporting data in and out of databases, spreadsheets, and other data management systems.

**CSV Structure**

- **Header Row:** Often includes column names.
- **Data Rows:** Each row contains data fields separated by commas.
- **Optional Quotes:** Fields that contain commas, line breaks, or quotes are enclosed in double quotes

**CSV Example**

```{code} bash
Name, Age, City
Alice, 30, New York
Bob, 25, Los Angeles
Charlie, 35, "San Francisco, CA"
```

- The header row specifies the columns: Name, Age, City.
- Each subsequent row contains the corresponding data for each column.
- The field "San Francisco, CA" is enclosed in double quotes to handle the comma within the data.

**TSV Structure**

- **Header Row:** Often includes column names.
- **Data Rows:** Each row contains data fields separated by tabs.
- **Plain Text:** Fields generally do not need to be enclosed in quotes.

**TSV Example**

```{code} bash
Name    Age    City
Alice    30    New York
Bob    25    Los Angeles
Charlie    35    San Francisco, CA
```

- The header row specifies the columns: Name, Age, City.
- Each subsequent row contains the corresponding data for each column.
- Tabs are used as delimiters, and no special handling is required for fields with commas.

**Key Differences**

- **Delimiter:** CSV uses commas, while TSV uses tabs.
- **Field Handling:** CSV may require quotes for fields with special characters; TSV generally does not.

**Advantages of CSV and TSV**

- **Simplicity and Readability:** Files are easy to read and write by both humans and machines.  
- **Wide Compatibility:** Files are supported by a vast array of software applications, including spreadsheet programs like Microsoft Excel and Google Sheets, database management systems, and various data analysis tools.
- **Lightweight:** Files are typically smaller in size compared to other formats like XML or JSON, which makes them efficient for storage and transfer, particularly over networks.
- **Ease of Use:** Creating, editing, and parsing CSV files requires minimal resources and can be done with basic text editors and programming languages.
- **TSV files avoid delimiter conflicts:** Using tabs as delimiters in TSV files reduces the risk of conflicts with data values that might contain commas, making it easier to parse without requiring special handling for embedded delimiters.
- **TSV Compatibility:** TSV files are not as universally supported as CSV, but are still compatible with many spreadsheet applications and text editors.

**Disadvantages of CSV and TSV**

- **Lack of Standardization:** There is no universal standard for CSV and TSV files, leading to inconsistencies in how different applications handle delimiters, line breaks, and special characters.
- **Limited Data Types:** CSV and TSV files can only store plain text, which limits their ability to represent more complex data types such as binary data, hierarchical data, or objects.
- **Delimiter Conflicts:** For CSV files fields containing commas must be enclosed in quotes, which can complicate parsing and data entry. Additionally, if the data itself contains quotes or line breaks, it requires additional escaping. For TSV files, data that contains tabs can complicate parsing and require special handling.
- **No Support for Metadata:** CSV files do not include metadata about the data, such as data types, schema information, or encoding, making it difficult to ensure data integrity and consistency.
- **Scalability Issues:** For very large datasets, both CSV and TSV formats can become inefficient in terms of processing speed and memory usage, as they require reading the entire file into memory for manipulation.
- **Lack of Data Validation:** Both formats lack built-in mechanisms for data validation, which can lead to inconsistencies and errors if the data is not carefully managed and validated externally.
- **No Support for Hierarchical Data:** Both CSV and TSV are flat-file formats and do not support hierarchical or nested data structures, limiting their use for complex data representations.

:::{seealso} Data Exchange Methods Activities
:class: dropdown
1. What does REST stand for and what is it used for?
2. What does it mean that REST communication is “stateless”?
3. Which HTTP methods in REST are used for Create and Delete operations?
4. What is JSON commonly used for in web applications?
5. Give one advantage and one disadvantage of JSON.
6. In JSON, how are arrays represented? Provide an example.
7. How is data structured in XML?
8. Give one advantage and one disadvantage of XML compared to JSON.
9. Name one real-world use of XML.
10. What is the main difference between CSV and TSV?
11. Why are CSV and TSV considered “lightweight” formats?
12. Give one disadvantage of CSV or TSV.
:::