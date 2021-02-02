from scrapy.http import Headers as Headers, Response as Response
from scrapy.responsetypes import responsetypes as responsetypes
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.project import data_path as data_path
from scrapy.utils.python import to_bytes as to_bytes, to_unicode as to_unicode
from scrapy.utils.request import request_fingerprint as request_fingerprint
from typing import Any

logger: Any

class DummyPolicy:
    ignore_schemes: Any = ...
    ignore_http_codes: Any = ...
    def __init__(self, settings: Any) -> None: ...
    def should_cache_request(self, request: Any): ...
    def should_cache_response(self, response: Any, request: Any): ...
    def is_cached_response_fresh(self, cachedresponse: Any, request: Any): ...
    def is_cached_response_valid(self, cachedresponse: Any, response: Any, request: Any): ...

class RFC2616Policy:
    MAXAGE: Any = ...
    always_store: Any = ...
    ignore_schemes: Any = ...
    ignore_response_cache_controls: Any = ...
    def __init__(self, settings: Any) -> None: ...
    def should_cache_request(self, request: Any): ...
    def should_cache_response(self, response: Any, request: Any): ...
    def is_cached_response_fresh(self, cachedresponse: Any, request: Any): ...
    def is_cached_response_valid(self, cachedresponse: Any, response: Any, request: Any): ...

class DbmCacheStorage:
    cachedir: Any = ...
    expiration_secs: Any = ...
    dbmodule: Any = ...
    db: Any = ...
    def __init__(self, settings: Any) -> None: ...
    def open_spider(self, spider: Any) -> None: ...
    def close_spider(self, spider: Any) -> None: ...
    def retrieve_response(self, spider: Any, request: Any): ...
    def store_response(self, spider: Any, request: Any, response: Any) -> None: ...

class FilesystemCacheStorage:
    cachedir: Any = ...
    expiration_secs: Any = ...
    use_gzip: Any = ...
    def __init__(self, settings: Any) -> None: ...
    def open_spider(self, spider: Any) -> None: ...
    def close_spider(self, spider: Any) -> None: ...
    def retrieve_response(self, spider: Any, request: Any): ...
    def store_response(self, spider: Any, request: Any, response: Any) -> None: ...

def parse_cachecontrol(header: Any): ...
def rfc1123_to_epoch(date_str: Any): ...
