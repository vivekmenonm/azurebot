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

## 🔐 Step 1: Create App Registration

1. Go to [Azure Portal → App registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps)
2. Click **New registration**
3. Name: `fastapi-teams-bot`
4. Supported account types: choose **Accounts in any org and personal accounts**
5. Register → Copy the:
   - **Application (client) ID** → `MICROSOFT_APP_ID`
   - **Directory (tenant) ID** (optional)

### 🔑 Create Client Secret
1. Go to your App → **Certificates & secrets**
2. Click **+ New client secret**
3. Copy the generated **Value** → `MICROSOFT_APP_PASSWORD`

---

## 🤖 Step 2: Create Azure Bot (Channels Registration)

1. Go to **Azure Portal → Create Resource → Azure Bot**
2. Click on create ![image](https://github.com/user-attachments/assets/df6b74b8-4a5f-4525-94cd-722310704a02)
3. Fill details and choose 	"Use existing app registration" and pass the app id we had in app registration. ![image](https://github.com/user-attachments/assets/0371c539-8f39-4813-baac-9046673c307a)

4. Choose: **Our newly created bot**
5. Fill:
   - **Microsoft App Password**: Paste the secret from step 1
   - **Messaging endpoint**: Which you got by running ngrok
6. Once deployed:
   - Go to **Channels** → Add **Microsoft Teams** and **Web Chat**

---

## ⚙️ Step 3: Local Setup

### 📥 Clone this repository

```bash
git clone https://github.com/your-username/fastapi-teams-bot.git
cd fastapi-teams-bot
