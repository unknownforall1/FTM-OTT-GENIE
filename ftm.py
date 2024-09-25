import os
from telegram import Update
from telegram.ext import Updater, CommandHandler
import yt_dlp

# Replace with your channel username
CHANNEL_USERNAME = '@ftmmovieskiduniya'

# Function to check if the user is a member of the specified channel
def is_user_member(update: Update) -> bool:
    user_id = update.message.from_user.id
    chat_member = update.bot.get_chat_member(CHANNEL_USERNAME, user_id)
    return chat_member.status in ['member', 'administrator', 'creator']

# Function to show progress
def progress_hook(d):
    if d['status'] == 'finished':
        print(f"\nDone downloading video: {d['filename']}")
    elif d['status'] == 'downloading':
        percent = d['downloaded_bytes'] / d['total_bytes'] * 100
        speed = d['speed']
        eta = d['eta']
        total_size = d['total_bytes']
        downloaded_bytes = d['downloaded_bytes']
        print(PROGRESS_BAR.format(percent=int(percent), downloaded_bytes=downloaded_bytes, total_size=total_size, speed=speed, eta=eta))

# Progress bar template
PROGRESS_BAR = (
    "╭━━━━❰ TEAM FTM DOWNLOADING..... ❱━➣\n"
    "┣⪼ 🗂️ : {downloaded_bytes} | {total_size} ( file size downloaded )\n"
    "┣⪼ ⏳️ : {percent}% ( percentage downloaded )\n"
    "┣⪼ 🚀 : {speed}/s  ( download speed )\n"
    "┣⪼ ⏱️ : {eta} ETA (estimated time)\n"
    "╰━━━━━━━━━━━━━━━➣"
)

# Function to download free video using yt-dlp and customize filename
def download_video(url, download_path='downloads/'):
    ydl_opts = {
        'outtmpl': f'{download_path}%(title)s.%(ext)s',  # Save with the original title
        'noplaylist': True,  # Ensure we're only downloading a single video
        'progress_hooks': [progress_hook]  # Set the progress hook
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', 'video')  # Get the video title
            video_duration = info_dict.get('duration', 0)  # Get the video duration in seconds
            file_size = info_dict.get('filesize', 0) or info_dict.get('filesize_approx', 0)  # Get file size

        # Customize the filename
        custom_filename = f"@ftmdeveloperz {video_title} 📥 Uᴘʟᴏᴀᴅᴇᴅ Bʏ @ftmmovieskiduniya 🚀\n" \
                          "🔧 Rɪᴘᴘᴇᴅ Bʏ @FTMDEVELOPER 💾\n" \
                          "⚠️ Dɪsᴄʟᴀɪᴍᴇʀ: Tʜɪs ғɪʟᴇ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ 𝟷𝟶 ᴍɪɴᴜᴛᴇs, sᴏ ᴘʟᴇᴀsᴇ ғᴏʀᴡᴀʀᴅ ɪᴛ ᴛᴏ ʏᴏᴜʀ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs. ⏳"

        # Define final output path with the custom name
        final_video_path = f"{download_path}{custom_filename}.mp4"

        # Rename the downloaded file
        os.rename(f'{download_path}{video_title}.mp4', final_video_path)

        return final_video_path, video_duration, file_size  # Return video path, duration, and size
    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        return None, 0, 0  # Return None and zeros if there's an error

# Start command
def start(update: Update):
    if not is_user_member(update):
        update.message.reply_text(
            f"Please join our channel {CHANNEL_USERNAME} to use this bot."
        )
        return

    update.message.reply_text("Send me a link to a free video from JioCinema, Hotstar, SonyLIV, or Zee5, and I'll download it for you!")

# Download video command
def download(update: Update):
    if not is_user_member(update):
        update.message.reply_text(
            f"Please join our channel {CHANNEL_USERNAME} to use this bot."
        )
        return

    if update.message.text:  # Check if the user provided a URL
        url = update.message.text
        chat_id = update.message.chat_id

        # Check if the URL is valid for supported platforms
        if any(platform in url for platform in ["jiocinema", "hotstar", "sonyliv", "zee5"]):
            update.message.reply_text('Downloading your free video, please wait...')

            # Download the video
            video_path, video_duration, file_size = download_video(url)
            if video_path:
                try:
                    # Send the downloaded video back to the user
                    update.message.reply_document(document=open(video_path, 'rb'))
                    update.message.reply_text(
                        f'Here is your free video!\n\n'
                        f'📏 **Duration**: {video_duration // 60}m {video_duration % 60}s\n'
                        f'💾 **File Size**: {file_size / (1024 * 1024):.2f} MB',
                    )
                except Exception as e:
                    update.message.reply_text(f"Failed to send the video: {str(e)}")
            else:
                update.message.reply_text("Error: Failed to download the video. Please try again.")
        else:
            update.message.reply_text('Unsupported platform or invalid URL! Please provide a valid link from JioCinema, Hotstar, SonyLIV, or Zee5.')
    else:
        update.message.reply_text('Please provide a valid video link!')

def main():
    # Get the bot token from the environment variables
    TOKEN = os.getenv('TELEGRAM_BOT_API_TOKEN')

    # Initialize the bot
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Register the command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("download", download))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

