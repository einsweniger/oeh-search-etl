from edu_sharing_client.api_client import ApiClient as ApiClient
from typing import Any, Optional

class RATINGV1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def add_or_update_rating(self, body: Any, rating: Any, repository: Any, node: Any, **kwargs: Any): ...
    def add_or_update_rating_with_http_info(self, body: Any, rating: Any, repository: Any, node: Any, **kwargs: Any): ...
    def delete_rating(self, repository: Any, node: Any, **kwargs: Any): ...
    def delete_rating_with_http_info(self, repository: Any, node: Any, **kwargs: Any): ...
