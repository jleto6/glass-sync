# Meta GlassSync

GlassSync is a Meta Glasses integration tool that automates syncing and downloading videos sent through Messenger from Meta View.

It automates media retrieval by logging into a dedicated Messenger account, monitoring a specified chat thread with your main Facebook account (linked to your Meta Glasses), and downloading incoming media automatically.

GlassSync leverages browser automation within Messenger’s standard web interface, simulating user actions transparently and ethically.

---

## How It Works

Your Meta Glasses are linked to your **main Facebook account**.  
You create a separate **dedicated Messenger account** (e.g., `ProjectName`) and add your main account as a friend.

When you say:

**"Hey Meta, send a video to ProjectName."**  
Your Glasses transmit the video via Messenger.  
GlassSync automatically detects and downloads the media as it arrives.

---

## Requirements

- Meta Ray-Ban Smart Glasses
- Facebook account linked to your Meta Glasses (main account)
- Dedicated Messenger account for receiving media
- Python 3.8+
- Google Chrome (latest version)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/meta-glasses-messenger-sync.git
cd meta-glasses-messenger-sync
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your credentials:

```bash
MESSENGER_EMAIL=your_dedicated_account_email
MESSENGER_PASSWORD=your_dedicated_account_password
MESSENGER_TARGET_ID=facebook_user_id_of_your_main_account
```

- **MESSENGER_EMAIL** and **MESSENGER_PASSWORD** are credentials for your dedicated Messenger account.
- **MESSENGER_TARGET_ID** is your main Facebook account’s user ID, linked with your Meta Glasses.

📌 **To find your Facebook user ID:**  
Visit [facebook.com/me](https://www.facebook.com/me) while logged in. You'll be redirected to a URL like `https://www.facebook.com/100012345678901`. The numeric portion is your user ID.

---

## Running the Application

Execute the script:

```bash
python glass_sync.py
```

GlassSync will:

- Log into Messenger.com using `undetected-chromedriver`
- Open the specified chat thread
- Monitor and download new image or video messages automatically

---

## Output

Media files are downloaded locally, named with timestamps for clarity:

```
media_20240507-184721.jpg
media_20240507-184725.mp4
```

---

## 🛠️ Future Enhancements

- Docker containerization
- Organize downloads by date (`/media/YYYY-MM-DD` folders)
- Cloud storage integration (e.g., AWS S3, Google Drive)
- Local REST API interface
