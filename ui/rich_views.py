import time
from contextlib import contextmanager
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich import box


console = Console()


def show_top_queries(data):
    table = Table(
        title="🔥 Top Queries",
        box=box.SIMPLE_HEAVY,
        header_style="bold yellow"
    )

    table.add_column("Type", style="cyan")
    table.add_column("Count", style="green")

    for item in data:
        table.add_row(item["_id"], str(item["count"]))

    console.print(table)


def show_unique_queries(data):
    table = Table(
        title="🕓 Unique Searches",
        box=box.MINIMAL_DOUBLE_HEAD,
        header_style="bold blue"
    )

    table.add_column("Type", style="magenta")

    for item in data:
        table.add_row(item["_id"])

    console.print(table)


@contextmanager
def loading(text="Processing..."):
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
        console=console
    ) as progress:

        task = progress.add_task(text, total=None)
        yield
        progress.update(task, completed=100)


def show_genres(genres):
    table = Table(
        title="🎭 Available Genres",
        box=box.ROUNDED,
        header_style="bold cyan"
    )

    table.add_column("Genres", style="magenta")

    for g in genres:
        table.add_row(g)

    console.print(table)


def show_year_range(min_year, max_year):
    panel = Panel.fit(
        f"[bold green]{min_year}[/bold green] → [bold green]{max_year}[/bold green]",
        title="📅 Available Year Range",
        border_style="cyan"
    )

    console.print(panel)




