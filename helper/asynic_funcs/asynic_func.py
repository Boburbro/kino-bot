from data.config import ADMINS


async def isAdmin(user_id) -> bool:
    print(f"user is admin = {str(user_id) in ADMINS}")
    return str(user_id) in ADMINS
