import subprocess


def convert_audio(input_file: str, output_file: str):
    """Converts an audio file to wav format using ffmpeg

    Parameters:
    input_file (str): Path to the input file.
    output_file (str): Path to the output file.

    Returns:
    int: Return code of the ffmpeg command.
    """

    command = ["ffmpeg", "-i", input_file, output_file]
    result = subprocess.run(command, check=True)

    # TODO: raise an exception if the conversion fails
    # result.check_returncode()

    return result.returncode
