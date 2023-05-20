import subprocess
import logging


def convert_audio(input_file_path: str, output_file_path: str):
    """Converts an audio file to wav format using ffmpeg

    Parameters:
    input_file (str): Path to the input file.
    output_file (str): Path to the output file.

    Returns:
    str: Path to the output file.
    None: If the command failed.
    """

    try:
        command = ["ffmpeg", "-i", input_file_path, output_file_path]
        result = subprocess.run(command, check=True)

        # raise an exception if the command failed
        result.check_returncode()
    except Exception as e:
        logger = logging.getLogger(__name__)

        logger.error(e)

        return None

    return output_file_path
