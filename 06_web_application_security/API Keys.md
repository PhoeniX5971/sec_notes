# API Keys

## What is an API Key?

An **API key** is a **unique identifier/token** used to authenticate a client (e.g. user, app, service) making a request to an API.

It says:

> “Hey, I'm allowed to access this API.”

---

## What It Does:

- **Identifies** the caller
- Sometimes **limits** or **tracks** usage (rate limits, billing)
- Can be used to **authorize access** to specific features/data

---

## 🛠️ How It's Used:

### Request Example:

```http
GET /weather?city=beirut&units=metric
Host: api.example.com
Authorization: Bearer YOUR_API_KEY
```

Or:

```http
GET /weather?city=beirut&apikey=YOUR_API_KEY
```

Or via headers:

```http
x-api-key: YOUR_API_KEY
```

---

## API Key vs Other Auth

|Method|Auth Level|Who uses it|
|---|---|---|
|API Key|Basic identity|Public/open APIs|
|OAuth Token|User-level auth|Securing user data|
|JWT|Stateless auth|Web apps / APIs|
|Session Cookie|Web apps|Logged-in users|

---

## Security Tips

| Mistake                       | Correct Way                              |
| ----------------------------- | ---------------------------------------- |
| Exposing key in frontend code | Keep keys secret, use backend as proxy   |
| Committing keys to GitHub     | Use `.env` files and `.gitignore` them   |
| Using same key forever        | Rotate keys, revoke unused ones          |
| Not restricting usage         | Apply IP/domain/rate limits if supported |

---

## 🧪 How to Test APIs with API Keys

```bash
curl -H "x-api-key: YOUR_API_KEY" https://api.example.com/data
```

Or with query param:

```bash
curl "https://api.example.com/data?apikey=YOUR_API_KEY"
```

---
