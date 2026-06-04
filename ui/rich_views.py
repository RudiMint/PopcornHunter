from contextlib import contextmanager
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich import box


console = Console()


def show_top_queries(data):
    """
    This function renders a console table showing the most frequent search
    types and how often each type has been executed.
    :param data:  Aggregated query statistics.
    """
    table = Table(
        title="Top Queries",
        box=box.SIMPLE_HEAVY,
        header_style="bold yellow"
    )

    table.add_column("Type", style="cyan")
    table.add_column("Count", style="green")

    for item in data:
        table.add_row(item["_id"], str(item["count"]))
    console.print(table)


def show_unique_queries(data):
    """
    Display the most recent unique search queries in a formatted console table.
    :param data: List of unique search records to display.
    """
    table = Table(
        title="Unique Searches",
        box=box.MINIMAL_DOUBLE_HEAD,
        header_style="bold blue"
    )

    table.add_column("Type", style="magenta")

    for item in data:
        table.add_row(
            item["search_type"],
            str(item["timestamp"]),
            str(item["params"]),
            str(item["results_count"])
        )

    console.print(table)


@contextmanager
def loading(text="Processing..."):
    """
    Context manager that displays a Rich progress spinner during a blocking operation.
    :param text: Description shown next to the spinner.
    """
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

def show_genres_table(genres):
    """
    Display a list of movie genres in a formatted grid-style console table.
    :param genres: List of genre names.
    """
    table = Table(
        title="Genres",
        box=box.ROUNDED,
        title_style="bold magenta",
        border_style="blue",
        show_header=False
    )

    table.add_column("Genre")

    columns = 4

    rows = [
        genres[i:i + columns]
        for i in range(0, len(genres), columns)
    ]

    for row in rows:
        row += [""] * (columns - len(row))
        table.add_row(*row)

    console.print(table)


def show_year_range(min_year, max_year):
    """
     Display the available movie release year range in a styled console panel.
    :param min_year: The earliest release year found in the dataset.
    :param max_year: The latest release year found in the dataset.
    """
    panel = Panel.fit(
        f"[bold green]{min_year}[/bold green] → [bold green]{max_year}[/bold green]",
        title="📅 Available Year Range",
        border_style="cyan"
    )

    console.print(panel)




