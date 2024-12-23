class MovieModel:
    def __init__(
        self,
        id: int,
        video_id: str,
        caption: str,
        download_count: int,
    ):
        self.id = id
        self.video_id = video_id
        self.caption = caption
        self.download_count = download_count

    @classmethod
    def fromJson(cls, json: dict):
        return cls(
            id=json["id"],
            video_id=json["video_id"],
            caption=json["caption"],
            download_count=json["download_count"],
        )

    def __repr__(self):
        return f"""MovieModel(\n  id={self.id}, \n  video_id='{self.video_id}', \n  caption='{self.caption}', \n  download_count={self.download_count},\n)"""
