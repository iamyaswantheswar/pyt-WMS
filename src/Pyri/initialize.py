import subprocess
import sys

requirements = ["matplotlib","PIL","cryptography"]

def check_requirements():
    for requirement in requirements:
        try:
            __import__(requirement)
        except ImportError:
            if requirement == "PIL":
                requirement = "pillow"
            print(f"{requirement} is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", requirement])
    print("All requirements are installed.")

check_requirements()

result = subprocess.run([sys.executable, "src/Pyri/login.py"],
                       capture_output=True, text=True)
print("Return code:", result.returncode)
print("Output:", result.stdout)
if result.stderr:
    print("Errors:", result.stderr)