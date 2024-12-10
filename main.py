from config_manager import load_config, save_config
from downloader import download_video
from validator import is_valid_url
from progress_tracker import show_progress_bar
import sys
from interface import interface


def main():
    print("===================================")
    print("Welcome to the YouTube Downloader!")
    print("===================================\n")
    
    # Load configurations
    config = load_config()
    default_folder = config.get("default_folder", "downloads/")

    try:
        while True:
            print("\nMain Menu:")
            print("1. Download a video")
            print("2. Set default download folder")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                # Launch the download interface
                interface(default_folder)
            elif choice == '2':
                # Update default download folder
                new_folder = input("Enter the new default download folder: ")
                config["default_folder"] = new_folder
                save_config(config)
                print(f"Default folder updated to: {new_folder}")
            elif choice == '3':
                print("Exiting. Thank you for using YouTube Downloader!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting gracefully. Goodbye!")

if __name__ == "__main__":
    main()
