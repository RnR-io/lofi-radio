#!/bin/zsh
# ── Lofi Focus + Pomodoro Launcher ──

PORT=8080
DIR="/Users/rinto/Documents/Codes/LofiRadio"

# Kill any process already using port 8080
lsof -ti tcp:$PORT | xargs kill -9 2>/dev/null

# Start Python HTTP server in background
python3 -m http.server $PORT --directory "$DIR" &>/dev/null &
disown

# Wait for the server to start
sleep 1.5

# Open in default browser
open "http://localhost:$PORT/index.html"

# Wait for browser to open, then silently close this terminal window
sleep 2
osascript -e 'tell application "Terminal"
    close (every window whose frontmost is true)
end tell' &
disown
