import vlc

songs = {
    "Gangam style": "",
    "Cell": "Cell.mp3",
    "USA": "USA.mp3",
    "Shrek": "Shrek.mp3",
    "Never gonna": "Rickroll.mp3"
}

def play_song(song_path):
    player = vlc.MediaPlayer(song_path)
    player.play()
    input("Press Enter to stop the song")
    player.stop()

if __name__ == "__main__":
    print("Available Songs:")
    for i, song in enumerate(songs, 1):
        print(f"{i}. {song}")

    while True:
        try:
            selection = int(input("Enter the number of the song you want to play (or 0 to exit): "))
            if selection == 0:
                break
            song_name = list(songs.keys())[selection - 1]
            song_path = songs[song_name]
            print(f"Now playing: {song_name}")
            play_song(song_path)
        except (ValueError, IndexError):
            print("Please enter a number corresponding to the song.")

