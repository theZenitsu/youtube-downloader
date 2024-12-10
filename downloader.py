import yt_dlp

def download_video(url, resolution='720p', output_folder='downloads/'):
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "Download completed successfully."
    except Exception as e:
        return f"Error: {str(e)}"

    
