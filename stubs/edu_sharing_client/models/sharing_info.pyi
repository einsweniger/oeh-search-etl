from typing import Any, Optional

class SharingInfo:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, password_matches: bool = ..., password: bool = ..., expired: bool = ..., invited_by: Optional[Any] = ..., node: Optional[Any] = ...) -> None: ...
    @property
    def password_matches(self): ...
    @password_matches.setter
    def password_matches(self, password_matches: Any) -> None: ...
    @property
    def password(self): ...
    @password.setter
    def password(self, password: Any) -> None: ...
    @property
    def expired(self): ...
    @expired.setter
    def expired(self, expired: Any) -> None: ...
    @property
    def invited_by(self): ...
    @invited_by.setter
    def invited_by(self, invited_by: Any) -> None: ...
    @property
    def node(self): ...
    @node.setter
    def node(self, node: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
