# Work description
1. Configure docker image
    - `--read-only`
        - Mount the container's root FS read-only
    - `--network none`
        - Connect a container to a network without internet
    - `--memory 500M`
        - Memory limit
    - `--cpus 2.0`
        - Number of CPUs
    - `--user 1000:1000`
        - Username or UID (format: `<name|uid>[:<group|gid>]`)
    - `--env EXERCISE=hello-world`
        - Exercise name
    - `--env USERNAME=aeinstein`
        - Student's login
    - `--env HOME=/jail`
        - Home directory of the container
    - `--env TMPDIR=/jail`
        - Temporary directory of the container
    - `--workdir /jail`
        - Working directory inside the container
    - `--tmpfs /jail:size=100M,noatime,exec,nodev,nosuid,uid=1000,gid=1000,nr_inodes=5k,mode=1700`
        - Mount a TMPFS directory at `/jail`, 100MB writable
    - `--volume volume_containing_student_repo:/jail/student:ro`
        - Bind mount a volume containing the student's repo

2. Exit status
An important note about the automated tests is the exit status (pass or fail scenarios on the test):
    - Exit `0` means success and the test has passed
    - If not `0` it will be considered an error
    - The error output shown to students is whatever is written to `stdout` or `stderr`

3. The submitted work is stored in `jail/students`

# Notes
- [Dockerfile example](https://github.com/01-edu/public/blob/master/js/tests/Dockerfile)
