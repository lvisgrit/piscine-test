import os
import sys
import tests
from dotenv import load_dotenv

EXERCISE_NAME = ""
USERNAME = ""
HOME_DIRECTORY = ""
TMPDIR = ""


def entrypoint():
    load_dotenv()

    try:
        # Get the given environment variables
        EXERCISE_NAME = os.environ["EXERCISE"]
        USERNAME = os.environ["USERNAME"]
        HOME_DIRECTORY = os.environ["HOME"]
        TMPDIR = os.environ["TMPDIR"]

    # Handle possible error, when env-var are missing
    except KeyError:
        print("Internal error, can't get environmental variables", file=sys.stderr)
        # Set Exit Status to 1 for error
        return 1

    # Execute Funtion run_test with the exercise name
    tests.run_test(EXERCISE_NAME)


if __name__ == "__main__":
    entrypoint()
