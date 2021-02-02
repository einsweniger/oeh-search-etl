from typing import Any, Optional

class StoredService:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    def __init__(self, name: Optional[Any] = ..., url: Optional[Any] = ..., icon: Optional[Any] = ..., logo: Optional[Any] = ..., in_language: Optional[Any] = ..., type: Optional[Any] = ..., description: Optional[Any] = ..., audience: Optional[Any] = ..., provider: Optional[Any] = ..., start_date: Optional[Any] = ..., interfaces: Optional[Any] = ..., about: Optional[Any] = ..., id: Optional[Any] = ..., is_accessible_for_free: bool = ...) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name: Any) -> None: ...
    @property
    def url(self): ...
    @url.setter
    def url(self, url: Any) -> None: ...
    @property
    def icon(self): ...
    @icon.setter
    def icon(self, icon: Any) -> None: ...
    @property
    def logo(self): ...
    @logo.setter
    def logo(self, logo: Any) -> None: ...
    @property
    def in_language(self): ...
    @in_language.setter
    def in_language(self, in_language: Any) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type: Any) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description: Any) -> None: ...
    @property
    def audience(self): ...
    @audience.setter
    def audience(self, audience: Any) -> None: ...
    @property
    def provider(self): ...
    @provider.setter
    def provider(self, provider: Any) -> None: ...
    @property
    def start_date(self): ...
    @start_date.setter
    def start_date(self, start_date: Any) -> None: ...
    @property
    def interfaces(self): ...
    @interfaces.setter
    def interfaces(self, interfaces: Any) -> None: ...
    @property
    def about(self): ...
    @about.setter
    def about(self, about: Any) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id: Any) -> None: ...
    @property
    def is_accessible_for_free(self): ...
    @is_accessible_for_free.setter
    def is_accessible_for_free(self, is_accessible_for_free: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
