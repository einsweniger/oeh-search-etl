from typing import Any, Optional

class GroupEntries:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, groups: Optional[Any] = ..., pagination: Optional[Any] = ...) -> None: ...
    @property
    def groups(self): ...
    @groups.setter
    def groups(self, groups: Any) -> None: ...
    @property
    def pagination(self): ...
    @pagination.setter
    def pagination(self, pagination: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
