Python
from pydub import AudioSegment
import os

def create_moh_track(music_dir, message_dir, output_file, message_interval=15, music_volume_reduction=-6, message_volume_increase=15, initial_delay=8):
    """
    Creates a music-on-hold track by mixing music files with periodic messages.

    Args:
        music_dir: The directory containing .wav music files.
        message_dir: The directory containing .wav message files.
        output_file: The path to save the final .wav output file.
        message_interval: The interval (in seconds) between messages.
        music_volume_reduction: The amount (in dB) to reduce music volume during messages (use a negative value to decrease volume).
        message_volume_increase: The amount (in dB) to increase message volume.
        initial_delay: The delay (in seconds) before the first message is played
    """

    # Get music and message file paths from directories
    music_files = [os.path.join(music_dir, f) for f in os.listdir(music_dir) if f.endswith('.wav')]
    message_files = [os.path.join(message_dir, f) for f in os.listdir(message_dir) if f.endswith('.wav')]

    # Load music and message files
    music_segments = [AudioSegment.from_wav(file) for file in music_files]
    message_segments = [AudioSegment.from_wav(file) for file in message_files]

    # Calculate total music duration
    total_music_duration = sum(seg.duration_seconds for seg in music_segments)

    # Create the final music track by concatenating music segments
    final_music = AudioSegment.empty()
    for segment in music_segments:
        final_music += segment

    # Overlay messages at intervals, starting after the initial delay, and repeating sequentially
    current_time = 0
    message_index = 0
    while current_time + initial_delay < final_music.duration_seconds:
        # Increase message volume
        message = message_segments[message_index] + message_volume_increase

        # Reduce music volume during message and overlay the message
        final_music = final_music.overlay(
            message,
            position=(current_time + initial_delay) * 1000,
            gain_during_overlay=music_volume_reduction
        )

        current_time += message_interval
        message_index = (message_index + 1) % len(message_segments)  # Cycle through messages

    # Export the final track
    final_music.export(output_file, format="wav")

# Example usage
music_dir = "music"
message_dir = "messages"
output_file = "moh_track.wav"

create_moh_track(music_dir, message_dir, output_file)