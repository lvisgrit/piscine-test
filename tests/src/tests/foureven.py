import sys
import os
import time
import subprocess
import testclass

# Define foureven class from testclass
class foureven(testclass.testclass):
    def __init__(self) -> None:
        super().__init__(
            "4\n6\n8\nWe have 4 even numbers\n", "/jail/student/foureven.py"
        )

    # Implemnt test_run
    def test_run(self) -> int:
        exercise_location = super().get_exercise_location()

        if not os.path.exists(exercise_location) and not os.path.isfile(
            exercise_location
        ):
            print("Can't find your exercise file: 'foureven.py'", file=sys.stderr)
            return 1

        # Run the student's solution with python
        student_process = subprocess.Popen(
            ["/usr/bin/env", "python3", exercise_location],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # Get process start time for checking runtime length
        start_student_proc = time.time()
        lines = []
        while True:
            # If the student's process ran longer than 5 seconds, terminate
            if (start_student_proc - time.time()) > 5.0:
                print("Program timeout (took longer than 5s)", file=sys.stderr)
                return 1

            # Append output from process to a list
            lines.append(student_process.stdout.readline().decode("utf-8"))

            # Get the returncode & check if the program is still running
            return_code = student_process.poll()
            if return_code is not None:
                if return_code != 0:
                    print(
                        f"Your program exited with return code '{return_code}' (!= 0)",
                        file=sys.stderr,
                    )
                    return 1
                # Get the remaining output and append it to the list too
                for output in student_process.stdout.readlines():
                    lines.append(output.decode("utf-8"))
                break
        # Join all strings in `lines` to a single string
        result_out = "".join(lines)

        # Check if the student's program output matches the solutions
        if result_out == super().get_correct_output():
            # TODO: Check if student hardcoded solution
            return 0
        else:
            # If not, print student's output and solution
            print(
                f"Got wrong output, your program printed:\n{result_out}\n\nExpected:\n{super().get_correct_output()}\n",
                file=sys.stderr,
            )
            return 1
