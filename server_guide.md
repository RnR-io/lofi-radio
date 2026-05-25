# 🖥️ Local Server — Setup & Resource Guide

## How to Start the Server

> [!IMPORTANT]
> You must do this every time you want to use `radio.html`. YouTube embeds only work over `http://`, not from a local file.

### Step 1 — Open Terminal
Press **⌘ + Space**, type `Terminal`, hit Enter.

### Step 2 — Run this command
```bash
python3 -m http.server 8080 --directory /Users/rinto/Documents/Codes
```

### Step 3 — Open the page in your browser
Go to:
```
http://localhost:8080/radio.html
```

### Step 4 — Stop the server when done
Press **Control + C** in the Terminal window.

---

## 💡 Shortcut: Make it one click (optional)

Create a shell script so you never have to type the command again:

```bash
# Run this once in Terminal to create the shortcut:
echo '#!/bin/zsh\npython3 -m http.server 8080 --directory /Users/rinto/Documents/Codes & sleep 1 && open http://localhost:8080/radio.html' > ~/start-radio.sh && chmod +x ~/start-radio.sh
```

Then just run `~/start-radio.sh` any time, or double-click it from Finder.

---

## 📊 Resource Usage

`python3 -m http.server` is an extremely lightweight built-in server. Here's what to expect:

| Resource | Usage |
|----------|-------|
| **CPU** | ~0% (idle), spikes <1% when page loads |
| **RAM** | ~8–12 MB (Python process, static files only) |
| **Network** | Only local loopback (127.0.0.1) — no internet traffic |
| **Disk** | None (read-only, no writes) |
| **Battery** | Negligible — less than keeping a browser tab open |

> [!NOTE]
> The heavy resource consumer is the **YouTube video itself** (rendered in your browser), not the Python server. The server simply serves the HTML file — it doesn't stream the video.

> [!TIP]
> You can safely leave the server running in the background all day. It uses less power than a Finder window.
