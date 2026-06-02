from rich.console import Console
from rich.table import Table
from rich import box


console = Console()


class Paginator:
    def __init__(self, items, page_size=10):
        self.pages = self._paginate(items, page_size)
        self.pages = list(self.pages)
        self.page_size = page_size

    def render_page(self, page_items, page, total_pages):
        table = Table(
            title=f"🎬 Movies (Page {page}/{total_pages})",
            box=box.ROUNDED,
            header_style="bold cyan"
        )

        table.add_column("ID", style="dim", width=6)
        table.add_column("Title", style="magenta")
        table.add_column("Year", style="green")
        table.add_column("Description", style="white")

        for film in page_items:
            table.add_row(
                str(film[0]),
                str(film[1]),
                str(film[2]),
                (film[3][:60] + "...") if film[3] else ""
            )

        console.clear()
        console.print(table)

    def _paginate(self, items, page_size):
        for i in range(0, len(items), page_size):
            yield items[i:i + page_size]

    def run(self):
        page = 0
        total_pages = len(self.pages)

        while True:
            page_items = self.pages[page]

            self.render_page(page_items, page + 1, total_pages)

            print("\n[n] next | [p] prev | [q] quit")

            cmd = input("> ").strip().lower()

            if cmd == "n" and page < total_pages - 1:
                page += 1

            elif cmd == "p" and page > 0:
                page -= 1

            elif cmd == "q":
                break
