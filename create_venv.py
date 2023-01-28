import subprocess
import os

# Create a new virtual environment
subprocess.call(["python", "-m", "venv", "venv"])

# Activate the virtual environment
activate_env = os.path.join("venv", "Scripts", "activate_this.py")
exec(open(activate_env).read(), {'__file__': activate_env})

# Install packages from the requirements file
subprocess.call(["pip", "install", "-r", "requirements.txt"])
