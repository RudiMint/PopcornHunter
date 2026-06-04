from rich.console import Console
from rich.table import Table
from rich import box


console = Console()


class Paginator:
    """
    Terminal-based paginator for displaying query results in pages.
    Features:
    - Splits results into fixed-size pages
    - Interactive navigation (next, previous, quit)
    - Rich table rendering for movie data
    - Automatic console clearing between pages
    """
    def __init__(self, items, page_size=10):
        self.pages = self._paginate(items, page_size)
        self.pages = list(self.pages)
        self.page_size = page_size

    def render_page(self, page_items, page, total_pages):
        """
        Render a single page of results as a formatted table.

        :param page_items: Items to display on the current page.
        :param page: Current page number (1-based).
        :param total_pages: Total number of pages.
        """
        table = Table(
            title=f"🎬 Movies (Page {page}/{total_pages})",
            box=box.ROUNDED,
            header_style="bold cyan"
        )

        table.add_column("ID", style="dim", width=6)
        table.add_column("Title", style="magenta")
        table.add_column("Year", style="green")
        table.add_column("Description", style="white", width=65, overflow="fold")

        for film in page_items:
            table.add_row(
                str(film[0]),
                str(film[1]),
                str(film[2]),
                film[3] or ""
            )

        console.clear()
        console.print(table)

    def _paginate(self, items, page_size):
        """
        Yield chunks of items split into pages.

        :param items: Full list of items.
        :param page_size: Number of items per page.
        :return: Generator yielding paginated slices of items.
        """
        for i in range(0, len(items), page_size):
            yield items[i:i + page_size]

    def run(self):
        """
        Start the interactive pagination loop.

        Users can navigate through pages using:
        - ``n`` → next page
        - ``p`` → previous page
        - ``q`` → quit pagination

        The method blocks until the user exits or only one page found.
        """
        page = 0
        total_pages = len(self.pages)

        while True:
            page_items = self.pages[page]

            self.render_page(page_items, page + 1, total_pages)

            if total_pages == 1:
                print("these are all the films found")
                break

            elif page == 0:
                print("\n[n] next | [q] quit")

            elif page == total_pages - 1:
                print("these are all the films found")
                print("\n[p] prev | [q] quit")

            else:
                print("\n[n] next | [p] prev | [q] quit")

            cmd = input("> ").strip().lower()

            if cmd == "n" and page < total_pages - 1:
                page += 1

            elif cmd == "p" and page > 0:
                page -= 1

            elif cmd == "q":
                break
