# WebSockets

## What are WebSockets?

- A protocol providing **full-duplex**, **bi-directional** communication over a **single TCP connection**.
- Enables servers and clients to send messages to each other **at any time**.
- Ideal for **real-time applications** (chat, gaming, live updates).

---

## How WebSockets work:

1. **Handshake**:  
    Client sends an HTTP/HTTPS request with an `Upgrade: websocket` header to initiate a WebSocket connection.
    
2. **Server Response**:  
    If the server supports WebSockets, it replies with a `101 Switching Protocols` response and upgrades the connection.
    
3. **Persistent connection**:  
    After upgrade, the TCP connection stays open for continuous two-way communication.
    

---

## Key features:

|Feature|Description|
|---|---|
|**Full-duplex**|Both client and server can send data independently at any time|
|**Low latency**|Messages sent instantly without HTTP overhead|
|**Single connection**|Uses one TCP connection, no repeated HTTP handshakes|
|**Stateful**|Connection remains open until closed|

---

## WebSocket Message Types:

- **Text** — UTF-8 encoded data (e.g., JSON)
- **Binary** — ArrayBuffer or other binary formats
- **Ping/Pong** — Keep connection alive, check latency
- **Close** — Close the connection gracefully

---

## WebSocket URL scheme:

- `ws://` — WebSocket over plain TCP (not secure)
- `wss://` — WebSocket over TLS/SSL (secure, like HTTPS)

---

## Basic example in JavaScript (client-side):

```js
const ws = new WebSocket('wss://example.com/socket');

ws.onopen = () => {
  console.log('Connection opened');
  ws.send('Hello server!');
};

ws.onmessage = (event) => {
  console.log('Message from server:', event.data);
};

ws.onclose = () => {
  console.log('Connection closed');
};

ws.onerror = (error) => {
  console.error('WebSocket error:', error);
};
```

---

## Use cases:

- Real-time chat apps
- Multiplayer games
- Live sports or stock updates
- Collaborative editing (Google Docs style)
- Notifications and alerts

---

## Comparison: WebSocket vs HTTP Polling

|Aspect|HTTP Polling|WebSocket|
|---|---|---|
|Latency|High (request/response for each poll)|Low (persistent connection)|
|Bandwidth|Higher (repeated HTTP headers)|Lower (less overhead)|
|Server load|Higher (many HTTP requests)|Lower (single connection per client)|
|Complexity|Simpler to implement|More complex server/client setup|

---

## Security considerations:

- Always use **`wss://`** (TLS encrypted) in production
- Authenticate users before upgrading connection
- Handle connection timeouts and errors gracefully
- Limit message size to prevent DoS attacks


---
