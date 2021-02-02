from edu_sharing_client.api_client import ApiClient as ApiClient
from typing import Any, Optional

class COLLECTIONV1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def add_feedback_to_collection(self, repository: Any, collection: Any, **kwargs: Any): ...
    def add_feedback_to_collection_with_http_info(self, repository: Any, collection: Any, **kwargs: Any): ...
    def add_to_collection(self, repository: Any, collection: Any, node: Any, source_repo: Any, **kwargs: Any): ...
    def add_to_collection_with_http_info(self, repository: Any, collection: Any, node: Any, source_repo: Any, **kwargs: Any): ...
    def change_icon_of_collection(self, mimetype: Any, repository: Any, collection: Any, **kwargs: Any): ...
    def change_icon_of_collection_with_http_info(self, mimetype: Any, repository: Any, collection: Any, **kwargs: Any): ...
    def create_collection(self, body: Any, repository: Any, collection: Any, **kwargs: Any): ...
    def create_collection_with_http_info(self, body: Any, repository: Any, collection: Any, **kwargs: Any): ...
    def delete_collection(self, repository: Any, collection: Any, **kwargs: Any): ...
    def delete_collection_with_http_info(self, repository: Any, collection: Any, **kwargs: Any): ...
    def delete_from_collection(self, repository: Any, collection: Any, node: Any, **kwargs: Any): ...
    def delete_from_collection_with_http_info(self, repository: Any, collection: Any, node: Any, **kwargs: Any): ...
    def get_collection(self, repository: Any, collection: Any, **kwargs: Any): ...
    def get_collection_with_http_info(self, repository: Any, collection: Any, **kwargs: Any): ...
    def get_collections_references(self, repository: Any, collection: Any, **kwargs: Any): ...
    def get_collections_references_with_http_info(self, repository: Any, collection: Any, **kwargs: Any): ...
    def get_collections_subcollections(self, repository: Any, collection: Any, scope: Any, **kwargs: Any): ...
    def get_collections_subcollections_with_http_info(self, repository: Any, collection: Any, scope: Any, **kwargs: Any): ...
    def get_feedback_of_collection(self, repository: Any, collection: Any, **kwargs: Any): ...
    def get_feedback_of_collection_with_http_info(self, repository: Any, collection: Any, **kwargs: Any): ...
    def remove_icon_of_collection(self, repository: Any, collection: Any, **kwargs: Any): ...
    def remove_icon_of_collection_with_http_info(self, repository: Any, collection: Any, **kwargs: Any): ...
    def search(self, repository: Any, query: Any, **kwargs: Any): ...
    def search_with_http_info(self, repository: Any, query: Any, **kwargs: Any): ...
    def set_collection_order(self, repository: Any, collection: Any, **kwargs: Any): ...
    def set_collection_order_with_http_info(self, repository: Any, collection: Any, **kwargs: Any): ...
    def set_pinned_collections(self, body: Any, repository: Any, **kwargs: Any): ...
    def set_pinned_collections_with_http_info(self, body: Any, repository: Any, **kwargs: Any): ...
    def update_collection(self, body: Any, repository: Any, **kwargs: Any): ...
    def update_collection_with_http_info(self, body: Any, repository: Any, **kwargs: Any): ...
