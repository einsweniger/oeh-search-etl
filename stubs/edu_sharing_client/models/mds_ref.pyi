from typing import Any, Optional

class MdsRef:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, repo: Optional[Any] = ..., id: Optional[Any] = ...) -> None: ...
    @property
    def repo(self): ...
    @repo.setter
    def repo(self, repo: Any) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
