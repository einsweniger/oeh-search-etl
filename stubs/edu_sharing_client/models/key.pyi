from typing import Any, Optional

class Key:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, first: Optional[Any] = ..., second: Optional[Any] = ..., name: Optional[Any] = ..., group: Optional[Any] = ...) -> None: ...
    @property
    def first(self): ...
    @first.setter
    def first(self, first: Any) -> None: ...
    @property
    def second(self): ...
    @second.setter
    def second(self, second: Any) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name: Any) -> None: ...
    @property
    def group(self): ...
    @group.setter
    def group(self, group: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
