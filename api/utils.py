import re
from datetime import date
from os import wait
from typing import List, Optional

from django.utils.timezone import make_aware

from api import models, types


def import_shiur(
    size: int,
    title: str,
    series: str,
    position: Optional[str],
    audio_src: Optional[str] = "",
    video_src: Optional[str] = "",
) -> types.Shiur:

    series, _ = models.Series.objects.get_or_create(
        key=series,
        title=series,
        is_legacy=True,
    )
    created_at = (
        date.fromisoformat(title[:10])
        if (re.compile(r"^\d{4}-\d{2}-\d{2}")).match(title[:10])
        else None
    )
    shiur = models.Shiur.objects.create(
        size=size,
        title=title,
        audio_src=audio_src,
        video_src=video_src,
        position=int(position) if position else 0,
        series=series,
        imported_title=title,
        imported_series=series,
    )

    if created_at:
        shiur.created_at = created_at
        shiur.save()

    return shiur
