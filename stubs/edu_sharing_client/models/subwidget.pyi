from typing import Any, Optional

class Subwidget:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, id: Optional[Any] = ...) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
