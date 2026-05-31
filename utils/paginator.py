class Paginator:
    def __init__(self, items, page_size=10):
        self.pages = self._paginate(items, page_size)
        self.page_size = page_size

    def _paginate(self, items, page_size):
        for i in range(0, len(items), page_size):
            yield items[i:i + page_size]

    def run(self):
        pages = iter(self.pages)

        page_num = 1
        page = next(pages, None)

        while page is not None:
            print(f"\nPage {page_num}")
            for item in page:
                print(item)

            next_page = next(pages, None)

            if next_page is None:
                print("no more results")
                break

            page = next_page
            page_num += 1

            user_input = input("\nEnter — next | q — exit: ")
            if not user_input:
                continue
            else:
                break

