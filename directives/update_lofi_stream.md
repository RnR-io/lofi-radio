# SOP — Updating the Lofi Radio Stream Link

> [!NOTE]
> YouTube live streams for Lofi Girl are occasionally restarted by YouTube, resulting in a new video ID. When this happens, follow this guide to update it.

There are two ways to update the active live stream link: via the UI (for a quick local fix that persists in your browser) or via a Python script (to update the codebase defaults permanently).

---

## Method 1 — Through the Web UI (Local Persistence)

This is the easiest way to update the stream immediately without editing any files. The app stores this configuration in your browser's local storage.

1. Open the Lofi Radio page.
2. Click the **Change Video** (🔗) button in the top right.
3. Paste the new YouTube video URL (e.g., `https://www.youtube.com/watch?v=X4VbdwhkE10`) and press **Enter** or click **Play**.
4. The stream is now updated. It will automatically load this stream even if you close and reopen the browser.
5. If you ever want to revert back to the default hardcoded stream, open the settings popup and click **Reset**.

---

## Method 2 — Run the Python Script (Codebase Defaults)

If you want to update the default stream built into the codebase (e.g., before publishing changes to GitHub Pages), run the helper script in the `execution/` directory.

### Requirements
- Python 3.x installed.

### Execution
From the root of the repository, run the script and provide the new YouTube URL or the 11-character video ID as an argument:

```bash
python3 execution/update_stream.py "https://www.youtube.com/watch?v=X4VbdwhkE10"
```

*Or using just the video ID:*

```bash
python3 execution/update_stream.py X4VbdwhkE10
```

### What this script does
1. Extracts the video ID from the argument.
2. Updates `const DEFAULT_VIDEO_ID` inside `index.html` and `radio.html`.
3. Updates the hardcoded `<iframe src="...">` embed fallbacks in both HTML files.
