import os
import subprocess

# Define the correct Python path
correct_python_path = r"C:\Users\jerem\AppData\Local\Programs\Python\Python312"

# Get the current PATH environment variable
current_path = os.environ.get("PATH", "")

# Check if the correct Python path is already in the PATH
if correct_python_path not in current_path:
    # Add the correct Python path to the beginning of the PATH
    new_path = f"{correct_python_path};{current_path}"
    
    # Update the PATH environment variable
    os.environ["PATH"] = new_path
    
    # Use setx to make the change permanent
    subprocess.run(["setx", "PATH", new_path], shell=True)
    print(f"Updated PATH to prioritize: {correct_python_path}")
else:
    print(f"{correct_python_path} is already in the PATH")

# Verify the change
print("Current PATH:", os.environ["PATH"])

# Define file paths
base_path = r"C:\Users\jerem\local\iCrohn\icrohn"
pyproject_path = os.path.join(base_path, "pyproject.toml")
cli_path = os.path.join(base_path, "src", "icrohn", "cli.py")
init_path = os.path.join(base_path, "src", "icrohn", "__init__.py")
usage_path = os.path.join(base_path, "docs", "usage.rst")
conf_path = os.path.join(base_path, "docs", "conf.py")

# Update pyproject.toml
with open(pyproject_path, "r") as file:
    pyproject_content = file.read()

pyproject_content = pyproject_content.replace("name = \"iCrohn\"", "name = \"hurting\"")

with open(pyproject_path, "w") as file:
    file.write(pyproject_content)

# Update cli.py
cli_content = """
import typer
from rich.console import Console

app = typer.Typer(name="hurting")
console = Console()

@app.command()
def record_info(info: str):
    \"\"\"Record information.\"\"\"
    console.print(f"Recorded information: {info}")

@app.command()
def main():
    \"\"\"Main entry point for the CLI.\"\"\"
    console.print("Welcome to the hurting CLI app!")
    console.print("Use the 'record-info' command to record information.")

if __name__ == "__main__":
    app()
"""

with open(cli_path, "w") as file:
    file.write(cli_content)

# Update __init__.py
init_content = """
\"\"\"Top-level package for hurting.\"\"\"

__author__ = \"\"\"Jeremy Paul Evans\"\"\"
__email__ = 'jeremyevans@hey.com'
__version__ = '0.1.0'
"""

with open(init_path, "w") as file:
    file.write(init_content)

# Update usage.rst
usage_content = """
=====
Usage
=====

To use hurting in a project::

    import hurting
"""

with open(usage_path, "w") as file:
    file.write(usage_content)

# Update conf.py
with open(conf_path, "r") as file:
    conf_content = file.read()

conf_content = conf_content.replace("project = 'iCrohn'", "project = 'hurting'")
conf_content = conf_content.replace("htmlhelp_basename = 'icrohndoc'", "htmlhelp_basename = 'hurtingdoc'")
conf_content = conf_content.replace("('icrohn.tex',", "('hurting.tex',")
conf_content = conf_content.replace("('icrohn',", "('hurting',")

with open(conf_path, "w") as file:
    file.write(conf_content)

print("Files updated successfully.")