import subprocess

# try:

completed = subprocess.run(['false'],  # setting this to false will produce an exit code 1 on the executed program
                           capture_output=True,
                           text=True,
                           check=True  # This will check if there is an error when running the other program
                           )

if completed.returncode != 0:
    print(completed.stderr)

# except subprocess.CalledProcessError as ex:  # this is an alternative to capture the error on the other executed program, but won't crash this program
#     print(ex)
