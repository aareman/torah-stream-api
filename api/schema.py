from typing import List

import strawberry
from strawberry.schema.config import StrawberryConfig
from strawberry_django_plus import gql

from api import types

# TODO: Add queries
# - Progress, total / organized
# - Mutation to import a shiur


@strawberry.type
class Query:
    series: List[types.Series] = gql.django.field()


# TODO: Add mutation for importing a shiur (optional series key)
# TODO: write a script to import all the old shiurim


# TODO: Add extensions
schema = strawberry.Schema(query=Query, config=StrawberryConfig(auto_camel_case=False))
