class ChannelModel:
    def __init__(self, id: int, title: str, link: str, plan: int):
        self.id = id
        self.title = title
        self.link = link
        self.plan = plan

    def __repr__(self):
        return f"""ChannelModel(\n  id={self.id}, \n  title='{self.title}', \n  link='{self.link}', \n  plan={self.plan},\n)"""