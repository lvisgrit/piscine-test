import sys
import time
import subprocess
import testclass

# Define foureven class from testclass
class foureven(testclass.testclass):
    def __init__(self) -> None:
        super().__init__(
            correct_output="2\n4\n6\n8\nWe have 4 even numbers\n",
            exercise_location="/jail/student/foureven.py",
        )
        # Add single string as disallowed
        super().add_illegal_string("We have 4 even numbers")
        super().add_illegal_strings(
            [
                "for.*in",  # Disallow for-loops
                "print\\(f?[\"']?.*[\"']?\\)",  # Disallow prints
            ]
        )

    # Implemnt test_run
    def test_run(self) -> int:
        exercise_location = super().get_exercise_location()

        if not testclass.testclass.exercise_file_exists(exercise_location):
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
        correct_output = super().get_correct_output()
        if (
            testclass.testclass.check_output(correct_output, result_out)
            and not super().check_illegal_patterns()
        ):
            return 0
        else:
            return 1
