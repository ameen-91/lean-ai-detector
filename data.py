import os
from utils import run_command
import kagglehub
import tqdm


def login_kaggle():
    kagglehub.login()


def get_data():
    if not os.path.exists("data"):
        login_kaggle()
        os.makedirs("data")
        print("Downloading data...")
        run_command(
            "cwd data | kaggle datasets download -d shanegerami/ai-vs-human-text"
        )
    else:
        print("sad")


if __name__ == "__main__":
    get_data()
    print("Got Data!")
