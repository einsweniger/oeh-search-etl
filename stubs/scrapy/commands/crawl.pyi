from scrapy.commands import BaseRunSpiderCommand as BaseRunSpiderCommand
from scrapy.exceptions import UsageError as UsageError
from typing import Any

class Command(BaseRunSpiderCommand):
    requires_project: bool = ...
    def syntax(self): ...
    def short_desc(self): ...
    exitcode: int = ...
    def run(self, args: Any, opts: Any) -> None: ...
