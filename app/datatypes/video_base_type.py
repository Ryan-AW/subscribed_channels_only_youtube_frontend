""" defines a base dataclass that store metadata about a YouTube video """
from dataclasses import dataclass


@dataclass
class VideoBaseType:
    """ a base dataclass that store metadata about a YouTube video """
    video_id: str
