# 🤖 FastAPI Bot for Microsoft Teams & Azure Web Chat

A simple chatbot built with FastAPI and Microsoft Bot Framework that replies:

> **"How can I help you?"**

It supports:
- ✅ Microsoft Teams (via Bot Framework + manifest upload)
- ✅ Azure Web Chat (via Direct Line channel)

---

## ⚙️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Microsoft Bot Framework SDK for Python](https://pypi.org/project/botbuilder-core/)
- [ngrok](https://ngrok.com/) or Azure Dev Tunnels (to expose localhost)
- Azure App Registration (identity)
- Azure Bot Channels Registration (message routing)

---

## 🛠️ Prerequisites

- Python 3.8+
- Azure Subscription
- Microsoft Teams (desktop or web)
- [ngrok](https://ngrok.com/download) or [`devtunnel`](https://aka.ms/devtunnel/download)

---

## 🔐 Step 1: Create App Registration (Azure AD)

1. Go to [Azure Portal → App registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps)
2. Click **New registration**
3. Name: `fastapi-teams-bot`
4. Supported account types: **Accounts in any org and personal accounts**
5. Click **Register**
6. Copy the following:
   - `Application (client) ID` → **`MICROSOFT_APP_ID`**
   - `Directory (tenant) ID` (optional)

### 🔑 Generate a Client Secret

1. Go to **Certificates & secrets** in the App Registration
2. Click **+ New client secret**
3. Name it (e.g. `bot-secret`) and set an expiry
4. Click **Add** and copy the **Value** → **`MICROSOFT_APP_PASSWORD`**

---

## 🤖 Step 2: Create Azure Bot (Bot Channels Registration)

1. Go to **Azure Portal → Create a resource → Azure Bot**
2. Select **Bot Channels Registration**
3. In the form:
   - **Bot handle**: `fastapi-teams-bot`
   - **Microsoft App ID**: Paste the App ID from Step 1
   - **Microsoft App password**: Paste the secret
   - **Messaging endpoint**: Use placeholder (e.g. `https://dummy/api/messages`)
   - Choose **"Use existing app registration"**
4. Click **Create**

### ➕ Enable Channels

After deployment:
- Go to the bot resource → **Channels**
- Add:
  - ✅ Microsoft Teams
  - ✅ Web Chat

---

## ⚙️ Step 3: Local Development Setup

### 🧭 Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-teams-bot.git
cd fastapi-teams-bot


