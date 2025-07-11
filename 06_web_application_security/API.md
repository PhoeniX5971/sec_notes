# API - Application Programming Interface

An **API** is a way for different software systems to **communicate** with each other. In web development, it usually refers to a set of **HTTP-based endpoints** exposed by a server that clients (like web apps or mobile apps) can call.

## Rest API

**REST** (Representational State Transfer) is the most common API style.

- Uses standard HTTP methods:
    
    - `GET` — Read data    
    - `POST` — Create data
    - `PUT` — Update/replace data
    - `PATCH` — Partially update data
    - `DELETE` — Delete data
        
- Each URL (endpoint) typically represents a **resource**.
    
- Responses are usually in **JSON**.

---
## GraphQL

**GraphQL** is a newer API style developed by **Meta (Facebook)**

- Uses a **single HTTP endpoint** (usually `/graphql`)
- Clients send **queries** or **mutations** in the request **body**
- Lets you **request exactly the data you need**
- Uses a strongly-typed schema
---

