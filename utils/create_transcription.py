from openai import Audio
import logging


def create_transcription(file_path: str):
    """Creates a transcription of an audio file using Whisper API.

    Parameters:
    file_path (str): Path to the audio file.

    Returns:
    str: Transcription of the audio file.
    None: If the file was not found.
    """

    logger = logging.getLogger(__name__)

    try:
        with open(file_path, "rb") as audio_file:
            transcript = Audio.transcribe("whisper-1", audio_file)
            return str(transcript.text)
    except FileNotFoundError:
        logger.error(f"File {file_path} not found.")
        return None
