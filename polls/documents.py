from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from polls.models import Hotel, Room, Booking


@registry.register_document
class HotelDocument(Document):
    province = fields.ObjectField(properties={
        "id": fields.TextField(),
        "slug": fields.TextField(),
        "name": fields.TextField(),
        "country": fields.ObjectField(properties={
            "code": fields.TextField(),
            "name": fields.TextField(),
            "currency": fields.TextField(),
        }),
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


@registry.register_document
class RoomDocument(Document):

    hotel = fields.ObjectField(properties={
        "id": fields.TextField(),
        "name": fields.TextField(),
        "address": fields.TextField(),
        "description": fields.TextField(),
        "phone_number": fields.TextField(),
        "average_rating": fields.FloatField(),
        "email": fields.TextField(),
        "image": fields.TextField(),
        "province": fields.ObjectField(properties={
            "id": fields.TextField(),
            "slug": fields.TextField(),
            "name": fields.TextField(),
            "country": fields.ObjectField(properties={
                "code": fields.TextField(),
                "name": fields.TextField(),
                "currency": fields.TextField(),
            })
        })
    })

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
class BookingDocument(Document):
    user = fields.ObjectField(properties={
        "id": fields.TextField(),
    })
    hotel = fields.ObjectField(properties={
        "id": fields.TextField(),
    })
    room = fields.ObjectField(properties={
        "id": fields.TextField(),
    })

    class Index:
        name = "bookings"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Booking
        fields = [
            "id",
            "check_in_date",
            "check_out_date",
            "total_price",
            "created_at",
            "updated_at",
            "status",
            "currency",
            "total_price_usd",
        ]
