import abc

# Define abstract test class
class testclass(metaclass=abc.ABCMeta):
    # Set correctoutput from the import
    def __init__(
        self,
        correctoutput: str,
        exercise_location: str,
    ) -> None:
        self.__correctoutput = correctoutput
        self.__exercise_location = exercise_location

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
