import sys
import importlib


def run_test(exercise_name: str):
    # Determine the module to the exercise-name
    try:
        module = importlib.import_module(f".{exercise_name}", "tests")
    except Exception as ex:
        print(f"Internal error: {ex}", file=sys.stderr)
        sys.exit(1)

    # Get the class from the module, which as to be named after the exercise
    # and instatiate it
    testclass = getattr(module, exercise_name)()

    # Execute the test-function for the given exercise
    sys.exit(testclass.test_run())
