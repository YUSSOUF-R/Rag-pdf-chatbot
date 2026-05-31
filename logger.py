import logging
import os


class Logger:

    @staticmethod
    def setup_logger():

        os.makedirs("logs", exist_ok=True)

        logging.basicConfig(
            filename="logs/app.log",
            level=logging.INFO,
            format="""
%(asctime)s
%(levelname)s
%(message)s
""",
            filemode="a"
        )

        return logging.getLogger()