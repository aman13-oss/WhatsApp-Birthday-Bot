<div align="center">

<img src="images/banner.png" alt="Birthday Automation banner" width="100%">

# 🎂 WhatsApp Birthday Bot

### *"Bro, when was your birthday again?" 😭* — never have to say that again.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automation-43B02A?logo=selenium&logoColor=white)
![WhatsApp Web](https://img.shields.io/badge/WhatsApp-Web-25D366?logo=whatsapp&logoColor=white)
![Chrome](https://img.shields.io/badge/Google-Chrome-4285F4?logo=googlechrome&logoColor=white)
![macOS](https://img.shields.io/badge/macOS-launchd-000000?logo=apple&logoColor=white)
![Status](https://img.shields.io/badge/Status-Personal%20Use-orange)

**A small project that solves one very real problem.**

[The Problem](#-the-problem) •
[Features](#-features) •
[How It Works](#%EF%B8%8F-how-it-works) •
[Quick Start](#-quick-start) •
[Add a Birthday](#-adding-a-birthday) •
[Automation](#-automatic-run-9-am-daily) •
[FAQ](#-troubleshooting--faq)

</div>

---

## 😭 The Problem

As a student and as a human, I almost always forget people's birthdays 😂

And somehow I only remember after seeing that person's WhatsApp status:

> *"Thank you everyone for the wishes 🥲"*

```mermaid
flowchart LR
    A[😴 Forgot the birthday] --> B[📱 Sees status:<br/>'Thanks for the wishes']
    B --> C[😭 Now I have to send a late wish]

    D[🤖 Birthday Bot] --> E[⏰ Auto-checks at 9 AM]
    E --> F[🎉 Wish sent on time]
    F --> G[😎 Everyone is impressed]

    style A fill:#ffd6d6,stroke:#e74c3c
    style C fill:#ffd6d6,stroke:#e74c3c
    style D fill:#d6ffe0,stroke:#27ae60
    style G fill:#d6ffe0,stroke:#27ae60
```

**The solution:** save contacts' birthdays in a JSON file. The program checks the date every day and automatically sends a birthday wish from my device through WhatsApp Web.

> 💡 This is also a practical project for a B.Tech CSE student — it combines **Python, JSON, Selenium, automation, file handling, and scheduling** in one real-world project.

---

## 🚀 Features

| | Feature | Details |
|---|---|---|
| 📅 | **JSON Storage** | All birthdays live in `birthdays.json` |
| 🔎 | **Automatic Date Check** | Finds whose birthday is today on its own |
| 💬 | **Contact Search** | Searches the contact on WhatsApp Web and opens the chat |
| 🎉 | **Auto Wish** | Sends `Happy Birthday 🎉🥳🎂` |
| 👥 | **Multiple Birthdays** | Handles several birthdays on the same day |
| 🛡️ | **Duplicate Protection** | Never sends two wishes on the same day |
| 💾 | **Sent Records** | Keeps a log in `sent_birthdays.json` |
| 🌐 | **Saved Session** | Uses a Chrome profile, so no repeated QR scans |
| ⏰ | **Daily Scheduler** | Runs every day at 9:00 AM via macOS `launchd` |
| 🧩 | **Zero Code Changes** | Add new birthdays without touching `main.py` |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| 🐍 **Python** | Core logic |
| 🤖 **Selenium** | Browser automation |
| 📄 **JSON** | Birthday data and sent records |
| 💬 **WhatsApp Web** | Delivery channel |
| 🌐 **Google Chrome** | Browser (with a saved profile) |
| 🍎 **macOS launchd** | Daily scheduling |

---

## ⚙️ How It Works

### 🧭 Project Workflow at a Glance

<div align="center">
  <img src="images/how-it-works.png" alt="Project workflow: birthdays.json to Python script to datetime.now to check birthdays to today's birthdays" width="380">
</div>

### 🔄 Main Flow

```mermaid
flowchart TD
    A([🚀 Bot starts]) --> B[📄 Load birthdays.json]
    B --> C[📆 Check today's date]
    C --> D{🎂 Anyone's birthday<br/>today?}
    D -- ❌ No --> Z([😴 Exit])
    D -- ✅ Yes --> E[👥 Build today's birthday list]
    E --> F{🛡️ Wish already<br/>sent?}
    F -- ✅ Yes --> G[⏭️ Skip contact]
    F -- ❌ No --> H[🌐 Open WhatsApp Web]
    H --> I[🔎 Search contact]
    I --> J[💬 Open chat]
    J --> K[🎉 Send 'Happy Birthday 🎉🥳🎂']
    K --> L[💾 Save record to sent_birthdays.json]
    L --> M{More contacts<br/>left?}
    G --> M
    M -- Yes --> F
    M -- No --> Z

    style A fill:#d6e4ff,stroke:#3b82f6
    style K fill:#d6ffe0,stroke:#27ae60
    style L fill:#d6ffe0,stroke:#27ae60
    style Z fill:#eee,stroke:#999
```

### 🧠 Behind the Scenes (Sequence)

```mermaid
sequenceDiagram
    autonumber
    participant L as ⏰ launchd (9 AM)
    participant P as 🐍 main.py
    participant J as 📄 JSON Files
    participant S as 🤖 Selenium
    participant W as 💬 WhatsApp Web

    L->>P: Daily trigger
    P->>J: Read birthdays.json
    P->>P: Match today's date
    P->>J: Check sent_birthdays.json (duplicate?)
    alt New birthday
        P->>S: Launch Chrome (saved profile)
        S->>W: Open web.whatsapp.com
        S->>W: Search contact + open chat
        S->>W: Send "Happy Birthday 🎉🥳🎂"
        P->>J: Save sent record
    else Already sent
        P-->>L: Skip ✅
    end
```

---

## 📁 Project Structure

```text
Whatsapp_birthday_bot/
│
├── 🐍 main.py                  # Core bot logic
├── 📄 birthdays.json           # Birthday database (edit this one)
├── 📦 requirements.txt         # Dependencies
├── 🙈 .gitignore               # Excludes personal files
├── 🖼️ assets/                  # README images (banner, screenshots)
├── 📘 README.md                # You are here
│
│   ── 🔒 Runtime files (not committed to git) ──
├── 🌐 chrome_profile/          # Saved WhatsApp session
├── 💾 sent_birthdays.json      # Duplicate-protection record
├── 📝 birthdaybot.log          # Normal logs
└── ⚠️ birthdaybot_error.log    # Error logs
```

---

## ⚡ Quick Start

### 1️⃣ Clone & Install

```bash
git clone <your-repo-url>
cd Whatsapp_birthday_bot
pip install -r requirements.txt
```

### 2️⃣ Add Birthdays
Add your contacts to `birthdays.json` ([see below](#-adding-a-birthday)).

### 3️⃣ First Run (scan the QR — only once)

```bash
python main.py
```

Chrome opens → **scan the WhatsApp Web QR code**. The session is saved in `chrome_profile/`, so you won't need to scan again. ✅

### 4️⃣ Manual Run (for testing)

```bash
cd ~/Desktop/Whatsapp_birthday_bot
/opt/anaconda3/bin/python main.py
```

#### 🖥️ Example terminal output

<div align="center">
  <img src="images/terminal-output.png" alt="Terminal output showing today's birthdays and success message" width="600">
</div>

#### 💬 Example messages sent

<div align="center">
  <img src="images/sample-messages.png" alt="Sample birthday messages sent on WhatsApp" width="700">
</div>

> 📸 Screenshots are illustrative examples of the output. Your script name and message text may differ.

---

## 📝 Adding a Birthday

Open `birthdays.json` and add a new entry:

```json
{
    "name": "Rahul",
    "birth_month": 10,
    "birth_date": 5
}
```

Full file example:

```json
[
    {
        "name": "Rahul",
        "birth_month": 10,
        "birth_date": 5
    },
    {
        "name": "Priya",
        "birth_month": 12,
        "birth_date": 25
    }
]
```

#### 📄 Sample `birthdays.json`

<div align="center">
  <img src="images/sample-birthdays-json.png" alt="Sample birthdays.json file" width="420">
</div>

#### 👥 Example contacts list

<div align="center">
  <img src="images/contacts-list.png" alt="Example contacts and birthdays table" width="650">
</div>

> ✅ **That's it.** No change is required in `main.py`.
> ⚠️ Write `name` exactly as the contact is **saved in WhatsApp**, otherwise the search will fail.

---

## ⏰ Automatic Run (9 AM Daily)

On macOS, the project is configured to run automatically **every day at 9:00 AM**, so you never need to run `main.py` by hand.

```mermaid
flowchart LR
    A[🕘 9:00 AM] --> B[⚙️ launchd trigger]
    B --> C[🐍 main.py runs]
    C --> D{🎂 Birthday today?}
    D -- Yes --> E[🎉 Send wish]
    D -- No --> F[😴 Do nothing]
    E --> G[📝 Save log]
    F --> G
```

<details>
<summary>📂 <b>Sample launchd .plist (click to expand)</b></summary>

<br>

Path: `~/Library/LaunchAgents/com.birthdaybot.plist`
*(adjust paths for your own system)*

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.birthdaybot</string>

    <key>ProgramArguments</key>
    <array>
        <string>/opt/anaconda3/bin/python</string>
        <string>/Users/YOUR_USERNAME/Desktop/Whatsapp_birthday_bot/main.py</string>
    </array>

    <key>WorkingDirectory</key>
    <string>/Users/YOUR_USERNAME/Desktop/Whatsapp_birthday_bot</string>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>/Users/YOUR_USERNAME/Desktop/Whatsapp_birthday_bot/birthdaybot.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/YOUR_USERNAME/Desktop/Whatsapp_birthday_bot/birthdaybot_error.log</string>
</dict>
</plist>
```

To load / unload:

```bash
launchctl load ~/Library/LaunchAgents/com.birthdaybot.plist
launchctl unload ~/Library/LaunchAgents/com.birthdaybot.plist
```

</details>

---

## 🛡️ Duplicate Protection

The bot stores successfully sent birthdays in:

```text
sent_birthdays.json
```

```mermaid
flowchart LR
    A[🎂 Rahul's birthday] --> B{Today's entry in<br/>sent_birthdays.json?}
    B -- ❌ No --> C[🎉 Send wish] --> D[💾 Save record]
    B -- ✅ Yes --> E[⏭️ Skip — will not send again]
```

If the same birthday is processed again on the same day, the bot **skips** that contact instead of sending another message. No spam. 😌

---

## 🔐 Personal Use & Privacy

- 🎯 This project is mainly built for **personal use and learning** as a B.Tech CSE student.
- 🔒 The WhatsApp session is kept inside the local `chrome_profile/` folder.
- 🙈 Personal runtime files (`chrome_profile/`, logs, sent records) are excluded using `.gitignore`.

> ⚠️ **Never push `chrome_profile/` to GitHub** — it contains your WhatsApp login session.

<details>
<summary>📄 <b>Recommended .gitignore</b></summary>

```gitignore
chrome_profile/
sent_birthdays.json
birthdaybot.log
birthdaybot_error.log
__pycache__/
*.pyc
```

</details>

---

## 🧯 Troubleshooting / FAQ

<details>
<summary>❓ <b>The bot didn't send a wish — what should I check?</b></summary>

<br>

1. Open `birthdaybot_error.log` — the error will be there
2. Make sure the month/date in `birthdays.json` is correct
3. Make sure the contact `name` matches the name saved in WhatsApp
4. Is WhatsApp Web still logged in? (If `chrome_profile/` was deleted, scan the QR again)
5. Was your Mac on and awake at 9 AM?

</details>

<details>
<summary>❓ <b>I have to scan the QR code every time</b></summary>

<br>

Check that `chrome_profile/` is being saved at the correct path. If the folder is deleted or corrupted, the session is lost.

</details>

<details>
<summary>❓ <b>Selenium can't find an element (selectors failing)</b></summary>

<br>

WhatsApp Web's UI changes over time. When that happens, the **Selenium selectors in `main.py` need to be updated** (use Inspect Element in the browser to find the new selector).

</details>

<details>
<summary>❓ <b>What if two people have a birthday on the same day?</b></summary>

<br>

The bot wishes both of them, one after another. ✅

</details>

<details>
<summary>❓ <b>How do I change the message?</b></summary>

<br>

Edit the wish string in `main.py` (default: `Happy Birthday 🎉🥳🎂`).

</details>

---

## 🗺️ Future Ideas

- [ ] 🎨 A list of random wishes (a different message each time)
- [ ] 🏷️ Personalized messages (`Happy Birthday Rahul 🎂`)
- [ ] 🔔 Mac notification when the bot runs
- [ ] 🔮 Reminder to myself about tomorrow's birthdays
- [ ] 🪟 Windows Task Scheduler / 🐧 Linux cron support
- [ ] 🖥️ A small GUI to add birthdays

---

## 📌 Note

WhatsApp Web's interface can change over time, so Selenium selectors may need updates if WhatsApp changes its webpage structure.

---

<div align="center">

**Made with Python ❤️🐍**

*A small project to solve one very real problem:*
**"Bro, when was your birthday again?" 😭**

⭐ If you liked it, give the repo a star!

</div>