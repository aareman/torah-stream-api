from typing import List

from strawberry_django_plus import gql

from api import models


@gql.django.type(models.Shiur)
class Shiur:
    series: gql.auto
    size: gql.auto
    title: gql.auto
    audio_src: gql.auto
    video_src: gql.auto
    position: gql.auto


# TODO: Add category type and relation in shiur
@gql.django.type(models.Series)
class Series:
    key: gql.auto
    title: gql.auto
    podcast: gql.auto
    vodcast: gql.auto
    shiurim: List[Shiur]
