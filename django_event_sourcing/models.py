import enum
import uuid

from django.conf import settings
from django.db import models

from .globals import get_event_type_register


class EventType(str, enum.Enum):
    """Represents the type of an event."""

    @property
    def fully_qualified_value(self):
        return self.get_namespace() + "." + self.value


class EventTypeField(models.CharField):
    """Stores the fully qualified value of an event type."""

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 255
        kwargs["db_index"] = True
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        del kwargs["db_index"]
        return name, path, args, kwargs

    def from_db_value(self, fully_qualified_value, *args, **kwargs):
        return get_event_type_register()[fully_qualified_value]

    def to_python(self, fully_qualified_value):
        if isinstance(fully_qualified_value, EventType):
            return fully_qualified_value

        return get_event_type_register()[fully_qualified_value]

    def get_prep_value(self, event_type):
        return event_type.fully_qualified_value


class Event(models.Model):
    """Represents an action that will happen."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = EventTypeField()
    payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="events"
    )
