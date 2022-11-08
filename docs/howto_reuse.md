# How to reuse the code
1. Add a new Python-file with a new test class
    - In the new file you can import the `testclass` module and create a new class that inherits from the abstract class `testclass`. The abstract class provides some common logic

2. Documentation for the abstract class `testclass`
    - test class provides the attributes `exercise_location`, `correctoutput` and `illegal_patterns`

    - The abstract method `test_run` needs to be implemented by the sub-classes so that they can do their own test logic

    - The method `add_illegal_string(s)` can be used to add a string or list of strings as an illegal pattern

    - `check_illegal_patterns` can be used to check if the students solution contains any of the forbidden patterns

    - The static method `exercise_file_exists` can be used to check if the exercise file from the student exists

    - The static method `check_output` checks if the imported parameters `student_output` and `correct_output` are equal

    
3. Implement the new testclass
    - In the new file you can call the constructor from the super-class to set the correct output aswell as the exercise location and add illegal patterns

    - Afterwards the abstract method `test_run` from the super-class has to be implemented by the new sub-class. This method should be used to get the students exercise file, run it and check if the output matches the correct output. If the output is correct you can also implement the hardcoded check by calling the method `check_illegal_patterns` from the super-class.

3. Explanation of init
    - In the init-file the module to the exercise-name will be determined. If there is no file to the exercise-name an error message will be showed.
    - If the module is found the class from the module, which as to be named after the exercise will be instantiated
    - Afterwards the `test_run` method will be called from the class