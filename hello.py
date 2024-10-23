from pytube import YouTube

# Function to download video from YouTube
def download_video(url):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Display video title
        print(f"Title: {yt.title}")
        
        # Display available video streams
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        print("Available streams:")
        for i, stream in enumerate(streams, 1):
            print(f"{i}. Resolution: {stream.resolution}, Filesize: {round(stream.filesize / (1024 * 1024), 2)} MB")

        # Choose the stream (resolution)
        choice = int(input("Enter the number of the stream to download: ")) - 1
        selected_stream = streams[choice]
        
        # Download the selected stream
        print("Downloading...")
        selected_stream.download()
        print(f"Download complete: {yt.title}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    url = input("Enter the YouTube video URL: ")
    download_video(url)

if __name__ == "__main__":
    main()
