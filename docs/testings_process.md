# Process of testing
1. Loading environmental variables from docker
    - `EXERCISE` for exercise name & finding python test module with the corresponding name
    - `USERNAME` for username of the student
    - `HOME` for the home directory of the container
    - `TMPDIR` for the temporary directory
2. Find, load & execute the python test module via the name in the `EXERCISE` env variable
3. Check if a student's exercise file exists
4. (*Optional*) Compile the code if needed (Rust, C, etc.)
5. Execute the code via binary or interpreter
6. Main loop
   1. Check if student's program ran longer than X seconds
   2. Read output from `stdout` to an array
   3. Check if student's program exited & get return code
   4. Depending on the returncode, fail test or continue
7. (*Optional*) Combine test output to one string
8. (*Optional*) Run solution code file to get expected output
9. Check if student's output matches expected solution output
10. Check student's source code for illegal patterns via regex