import json
import os
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.db.models import Count
from django.utils.timezone import utc

from api import utils


# FIX: make this atomic, so failure doesn't create duplicates
class Command(BaseCommand):
    help = "Imports all episodes from a directory"

    def add_arguments(self, parser):
        parser.add_argument(
            "-d", "--directory", type=str, help="Directory to import from"
        )

    def handle(self, *args, **kwargs):
        dir = kwargs["directory"]
        for f in os.listdir(dir):
            print(os.path.join(dir, f))
            if f.endswith(".json"):
                continue
            episodes = open(os.path.join(dir, f) + "/episodes.json")
            data = json.load(episodes)
            series = open(os.path.join(dir, f) + "/topic.json")
            series_title = json.load(series).get("id")
            for ep in data:
                utils.import_shiur(
                    size=ep["FileSize"],
                    title=ep["Title"],
                    series=series_title or "",
                    position=ep.get("Track"),
                    audio_src=ep["audio"],
                    video_src=ep.get("video", ""),
                )

            episodes.close()
