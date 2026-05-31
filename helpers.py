import os
from datetime import datetime


def allowed_file(filename):
    """
    Check if uploaded file is PDF.
    """

    return "." in filename and filename.rsplit(".", 1)[1].lower() == "pdf"


def generate_timestamp():
    """
    Generate formatted timestamp.
    """

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def ensure_directory_exists(directory_path):
    """
    Create directory if not exists.
    """

    os.makedirs(directory_path, exist_ok=True)