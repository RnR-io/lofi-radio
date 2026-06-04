import sys
import os
import re

def extract_video_id(url_or_id):
    url_or_id = url_or_id.strip()
    # If it's already an 11-character video ID
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id):
        return url_or_id
    
    # Otherwise try to extract from URL
    patterns = [
        r'(?:v=|list=|^/|embed/|youtu\.be/|/watch\?v=)([a-zA-Z0-9_-]{11})',
        r'youtube\.com/live/([a-zA-Z0-9_-]{11})'
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    
    return None

def update_file(filepath, new_id):
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace DEFAULT_VIDEO_ID declaration
    # const DEFAULT_VIDEO_ID = 'EWrX250Zhko'; or const DEFAULT_VIDEO_ID = 'jfKfPfyJRdk'; etc.
    content_updated, count1 = re.subn(
        r"(const DEFAULT_VIDEO_ID\s*=\s*['\"])[a-zA-Z0-9_-]{11}(['\"]\s*;)", 
        rf"\g<1>{new_id}\g<2>", 
        content
    )
    
    # Replace iframe source fallback
    # src="https://www.youtube.com/embed/EWrX250Zhko?autoplay=1"
    content_updated, count2 = re.subn(
        r"(src\s*=\s*['\"]https://www\.youtube\.com/embed/)[a-zA-Z0-9_-]{11}(\?autoplay=1['\"])",
        rf"\g<1>{new_id}\g<2>",
        content_updated
    )
    
    # Also replace any other hardcoded currentVideoID declaration if const was let previously
    # let currentVideoID = 'EWrX250Zhko';
    content_updated, count3 = re.subn(
        r"(let currentVideoID\s*=\s*['\"])[a-zA-Z0-9_-]{11}(['\"]\s*;)",
        rf"\g<1>{new_id}\g<2>",
        content_updated
    )
    
    if count1 > 0 or count2 > 0 or count3 > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content_updated)
        print(f"Updated {filepath} (replaced: {count1} defaults, {count2} iframe embeds, {count3} let definitions)")
        return True
    else:
        print(f"Warning: No match found to replace in {filepath}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 execution/update_stream.py <youtube_url_or_id>")
        sys.exit(1)
        
    input_val = sys.argv[1]
    video_id = extract_video_id(input_val)
    if not video_id:
        print(f"Error: Could not extract a valid YouTube video ID from: {input_val}")
        sys.exit(1)
        
    print(f"Target YouTube Video ID: {video_id}")
    
    # Determine base directory (LofiRadio directory)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    index_path = os.path.join(base_dir, 'index.html')
    radio_path = os.path.join(base_dir, 'radio.html')
    
    success_index = update_file(index_path, video_id)
    success_radio = update_file(radio_path, video_id)
    
    if success_index or success_radio:
        print("Default YouTube stream updated successfully!")
    else:
        print("No files were updated. Verify if files contain the replacement patterns.")

if __name__ == '__main__':
    main()
