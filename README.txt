
# Music-On-Hold Track Creator

This Python script allows you to create a custom Music-On-Hold (MOH) track by mixing music files with periodic announcement messages. It uses the `pydub` library to overlay messages onto music tracks at specified intervals.

## Features

- Mixes multiple `.wav` music files from a directory into a single continuous track.
- Overlays announcement messages at regular intervals on the music track.
- Allows adjustment of music and message volumes during the overlay.
- Configurable initial delay before the first message and interval between subsequent messages.

## Prerequisites

- Python 3.x
- `pydub` library
- `ffmpeg` or `libav` (required by `pydub` for audio processing)

You can install `pydub` and `audiosegment` using pip:

```
pip install pydub
pip install audiosegment
```

Ensure you have `ffmpeg` or `libav` installed on your system. You can install `ffmpeg` with:

- **macOS**: `brew install ffmpeg`
- **Ubuntu**: `sudo apt-get install ffmpeg`
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to your PATH.

## Usage

### 1. Prepare Your Files

- **Music files**: Place your `.wav` music files in a directory, e.g., `music/`.
- **Message files**: Place your `.wav` announcement message files in a directory, e.g., `messages/`.

### 2. Run the Script

You can use the script as follows:

----python----
from pydub import AudioSegment
import os

def create_moh_track(music_dir, message_dir, output_file, message_interval=15, music_volume_reduction=-6, message_volume_increase=15, initial_delay=8):
    # Script code here...
    pass

# Example usage
music_dir = "music"
message_dir = "messages"
output_file = "moh_track.wav"

create_moh_track(music_dir, message_dir, output_file)
```

### 3. Script Arguments

- `music_dir`: Directory containing the `.wav` music files.
- `message_dir`: Directory containing the `.wav` message files.
- `output_file`: Path to save the final `.wav` output file.
- `message_interval` (optional): Interval (in seconds) between messages. Default is 15 seconds.
- `music_volume_reduction` (optional): Volume reduction (in dB) of the music during messages. Use a negative value to decrease the volume. Default is -6 dB.
- `message_volume_increase` (optional): Volume increase (in dB) of the message files. Default is 15 dB.
- `initial_delay` (optional): Delay (in seconds) before the first message is played. Default is 8 seconds.

### 4. Output

The script will create a `moh_track.wav` file containing your custom Music-On-Hold track.

## Example

Here is a basic example of using the script:


music_dir = "music"
message_dir = "messages"
output_file = "moh_track.wav"

create_moh_track(music_dir, message_dir, output_file, message_interval=20, music_volume_reduction=-5, message_volume_increase=10, initial_delay=10)
```

This will create a MOH track with messages every 20 seconds, a 10-second initial delay, and adjusted volumes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find a bug or have a feature request.
