import subprocess

completed = subprocess.run(['python3', 'other.py'],
                           capture_output=True,
                           text=True
                           )

print('args', completed.args)
print('retunrcode', completed.returncode)
print('stderr', completed.stderr)
print('stdout', completed.stdout)