from scrapy.commands import ScrapyCommand as ScrapyCommand
from typing import Any

class Command(ScrapyCommand):
    requires_project: bool = ...
    default_settings: Any = ...
    def short_desc(self): ...
    def run(self, args: Any, opts: Any) -> None: ...
