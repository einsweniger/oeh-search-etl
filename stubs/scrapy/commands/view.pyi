from scrapy.commands import fetch as fetch
from scrapy.utils.response import open_in_browser as open_in_browser
from typing import Any

class Command(fetch.Command):
    def short_desc(self): ...
    def long_desc(self): ...
    def add_options(self, parser: Any) -> None: ...
