from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from polls.models import Hotel, Room, Province


@registry.register_document
class RoomDocument(Document):
    class Index:
        name = "rooms"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Room
        fields = [
            "id",
            "name",
            "description",
            "adults",
            "children",
            "price",
            "image",
            "is_available",
        ]


@registry.register_document
class HotelDocument(Document):
    rooms = fields.NestedField(properties={
        "name": fields.TextField(),
        "description": fields.TextField(),
        "adults": fields.IntegerField(),
        "children": fields.IntegerField(),
        "price": fields.DoubleField(),
        "image": fields.TextField(),
        "is_available": fields.BooleanField()
    })

    class Index:
        name = "hotels"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Hotel
        fields = [
            "id",
            "name",
            "address",
            "description",
            "phone_number",
            "average_rating",
            "email",
            "image",
        ]
