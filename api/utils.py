import re
from os import wait
from typing import List, Optional

from api import models, types


def import_shiur(
    size: int,
    title: str,
    series: str,
    track: Optional[str],
    audio_src: Optional[str] = "",
    video_src: Optional[str] = "",
) -> types.Shiur:

    series, _ = models.Series.objects.get_or_create(
        key=series,
        title=series,
        is_legacy=True,
        category=models.Category.objects.get(name="Uncategorized"),
    )
    created_at = (
        title[:10] if (re.compile(r"^\d{4}-\d{2}-\d{2}")).match(title[:10]) else None
    )
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
