from typing import Any, Optional

class Comment:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, ref: Optional[Any] = ..., reply_to: Optional[Any] = ..., creator: Optional[Any] = ..., created: Optional[Any] = ..., comment: Optional[Any] = ...) -> None: ...
    @property
    def ref(self): ...
    @ref.setter
    def ref(self, ref: Any) -> None: ...
    @property
    def reply_to(self): ...
    @reply_to.setter
    def reply_to(self, reply_to: Any) -> None: ...
    @property
    def creator(self): ...
    @creator.setter
    def creator(self, creator: Any) -> None: ...
    @property
    def created(self): ...
    @created.setter
    def created(self, created: Any) -> None: ...
    @property
    def comment(self): ...
    @comment.setter
    def comment(self, comment: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
