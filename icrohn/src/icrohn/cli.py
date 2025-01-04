
import typer
from rich.console import Console

app = typer.Typer(name="hurting")
console = Console()

@app.command()
def record_info(info: str):
    """Record information."""
    console.print(f"Recorded information: {info}")

@app.command()
def main():
    """Main entry point for the CLI."""
    console.print("Welcome to the hurting CLI app!")
    console.print("Use the 'record-info' command to record information.")

if __name__ == "__main__":
    app()
