import abc
import os
import sys
import re

# Define abstract test class
class testclass(metaclass=abc.ABCMeta):
    # Set correctoutput from the import
    def __init__(
        self,
        *,
        correct_output: str,
        exercise_location: str,
    ) -> None:
        self.__correctoutput = correct_output
        self.__exercise_location = exercise_location
        self.__illegal_patterns: list[re.Pattern] = []

    # Adds a pattern to the list of illegal patterns
    #
    # Patterns should be in regex format
    def add_illegal_string(self, s: str):
        # Compile regex string for performance reasons & immediate checking
        try:
            compiled = re.compile(s, re.MULTILINE)
            self.__illegal_patterns.append(compiled)
        except Exception as ex:
            print(f"Internal error: {ex}", file=sys.stderr)
            sys.exit(1)

    # Adds multiple patterns tot he list of illegal patterns
    #
    # Patterns should be in regex format
    def add_illegal_strings(self, s: list[str]):
        compiled_rgx = []

        # Compile regex string for performance reasons & immediate checking
        for regstr in s:
            try:
                compiled_rgx.append(re.compile(regstr, re.MULTILINE))
            except Exception as ex:
                print(f"Internal error: {ex}", file=sys.stderr)
                sys.exit(1)

        self.__illegal_patterns.extend(compiled_rgx)

    # Returns `True` if at least one illegal pattern matched, else `False`
    def check_illegal_patterns(self) -> bool:
        # If there aren't any patterns registered just skip over file loading
        if len(self.__illegal_patterns) == 0:
            return False

        with open(self.get_exercise_location(), "r") as f:
            lines = f.readlines()
            for rgx in self.__illegal_patterns:
                for index, line in enumerate(lines):
                    mtch = rgx.search(line.strip())
                    if mtch is not None:
                        print(f"Your file contains illegal patterns: '{mtch.group(0)}' in line '{index + 1}'")
                        return True
        return False

    # Abstract test_run Method
    @abc.abstractmethod
    def test_run(self) -> int:
        pass

    # Return the correct output from the class
    def get_correct_output(self) -> str:
        return self.__correctoutput

    # Return the exercise location
    def get_exercise_location(self) -> str:
        return self.__exercise_location

    # Static Method to check if exercise file exists
    @staticmethod
    def exercise_file_exists(exercise_location: str) -> bool:
        if os.path.exists(exercise_location) and os.path.isfile(exercise_location):
            return True
        else:
            filename = os.path.basename(os.path.normpath(exercise_location))
            print(f"Can't find your exercise file: '{filename}'", file=sys.stderr)
            return False

    # Static method to check if students output equals the correct output
    @staticmethod
    def check_output(correct_output: str, student_output: str) -> bool:
        # Check if the student's program output matches the solutions
        if student_output == correct_output:
            return True
        else:
            # If not, print student's output and solution

            # Replace newlines with explicitely stated newline characters
            student_output = student_output.replace("\n", "\\n\n")
            correct_output = correct_output.replace("\n", "\\n\n")
            print(
                f"Got wrong output, your program printed:\n{student_output}\n\nExpected:\n{correct_output}\n",
                file=sys.stderr,
            )
            return False
