from typing import Any

class DeleteOption:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, delete: bool = ...) -> None: ...
    @property
    def delete(self): ...
    @delete.setter
    def delete(self, delete: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
