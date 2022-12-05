import re
from typing import List, Optional

import strawberry
from strawberry.schema.config import StrawberryConfig
from strawberry_django_plus import gql

from api import models, types, utils

# TODO: Add queries
# - Progress, total / organized
# - Mutation to import a shiur
# TODO: Add rss feeds to be automatically generated


@strawberry.type
class Query:
    series: List[types.Series] = gql.django.field()
    # TODO: Add category query


# TODO: Add mutation for importing a shiur (optional series key)
# TODO: write a script to import all the old shiurim
@strawberry.type
class Mutation:
    @strawberry.field
    def upload_shiur(
        self,
        size: int,
        title: str,
        series: str,
        track: Optional[str],
        audio_src: Optional[str] = "",
        video_src: Optional[str] = "",
    ) -> types.Shiur:
        return utils.import_shiur(
            size=size,
            title=title,
            series=series,
            track=track,
            audio_src=audio_src,
            video_src=video_src,
        )


# TODO: Add extensions
schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig())
