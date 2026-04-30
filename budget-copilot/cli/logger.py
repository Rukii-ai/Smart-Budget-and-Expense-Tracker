"""
Typer CLI and logging module
"""
import typer

app = typer.Typer()

@app.command()
def hello(name: str = typer.Argument(..., help="Name to greet")):
    """Simple greeting command"""
    typer.echo(f"Hello {name}!")

if __name__ == "__main__":
    app()
