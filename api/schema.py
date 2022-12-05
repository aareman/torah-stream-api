import re
from typing import List, Optional

import strawberry
from strawberry.schema.config import StrawberryConfig
from strawberry_django_plus import gql

from api import models, types

# TODO: Add queries
# - Progress, total / organized
# - Mutation to import a shiur


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

        series, created = models.Series.objects.get_or_create(
            key=series,
            title=series,
            category=models.Category.objects.get(name="Uncategorized"),
        )
        created_at = (
            title[:10]
            if (re.compile(r"^\d{4}-\d{2}-\d{2}")).match(title[:10])
            else None
        )
        if created_at:
            title = title[10 + 3 :]
        shiur = models.Shiur.objects.create(
            size=size,
            title=title,
            audio_src=audio_src,
            video_src=video_src,
            track=int(track) if track else 0,
            created_at=created_at,
            series=series,
        )

        return shiur


# TODO: Add extensions
schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig())
