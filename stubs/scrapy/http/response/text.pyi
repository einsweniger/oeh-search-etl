from scrapy.exceptions import ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.http import Request as Request
from scrapy.http.response import Response as Response
from scrapy.utils.python import memoizemethod_noargs as memoizemethod_noargs, to_unicode as to_unicode
from scrapy.utils.response import get_base_url as get_base_url
from typing import Any, Generator

class TextResponse(Response):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def replace(self, *args: Any, **kwargs: Any): ...
    @property
    def encoding(self): ...
    def body_as_unicode(self): ...
    def json(self): ...
    @property
    def text(self): ...
    def urljoin(self, url: Any): ...
    @property
    def selector(self): ...
    def xpath(self, query: Any, **kwargs: Any): ...
    def css(self, query: Any): ...
    def follow(self, url: Any, callback: Any=..., method: Any=..., headers: Any=..., body: Any=..., cookies: Any=..., meta: Any=..., encoding: Any=..., priority: Any=..., dont_filter: Any=..., errback: Any=..., cb_kwargs: Any=..., flags: Any=...) -> Request: ...
    def follow_all(self, urls: Any=..., callback: Any=..., method: Any=..., headers: Any=..., body: Any=..., cookies: Any=..., meta: Any=..., encoding: Any=..., priority: Any=..., dont_filter: Any=..., errback: Any=..., cb_kwargs: Any=..., flags: Any=..., css: Any=..., xpath: Any=...) -> Generator[Request, None, None]: ...

class _InvalidSelector(ValueError): ...
