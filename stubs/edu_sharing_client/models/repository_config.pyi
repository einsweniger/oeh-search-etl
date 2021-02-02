from typing import Any, Optional

class RepositoryConfig:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, frontpage: Optional[Any] = ...) -> None: ...
    @property
    def frontpage(self): ...
    @frontpage.setter
    def frontpage(self, frontpage: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
