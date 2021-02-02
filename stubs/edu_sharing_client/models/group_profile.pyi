from typing import Any, Optional

class GroupProfile:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, group_email: Optional[Any] = ..., display_name: Optional[Any] = ..., group_type: Optional[Any] = ..., scope_type: Optional[Any] = ...) -> None: ...
    @property
    def group_email(self): ...
    @group_email.setter
    def group_email(self, group_email: Any) -> None: ...
    @property
    def display_name(self): ...
    @display_name.setter
    def display_name(self, display_name: Any) -> None: ...
    @property
    def group_type(self): ...
    @group_type.setter
    def group_type(self, group_type: Any) -> None: ...
    @property
    def scope_type(self): ...
    @scope_type.setter
    def scope_type(self, scope_type: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
