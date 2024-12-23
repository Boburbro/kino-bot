from data.config import ADMINS


async def isAdmin(user_id) -> bool:
    print(f"{user_id}: user is admin = {str(user_id) in ADMINS}")
    return str(user_id) in ADMINS


def parse_telegram_data(text):
    result = {}

    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        if line.endswith("(id)"):
            result["id"] = line.replace("(id)", "").strip()
        elif line.endswith("(url)"):
            result["url"] = line.replace("(url)", "").strip()
        elif line.endswith("(name)"):
            result["name"] = line.replace("(name)", "").strip()
        elif line.endswith("(plan)"):
            result["plan"] = line.replace("(plan)", "").strip()
    return result if result else None


text = """
-1002586541 (id)
1000 (plan)
IT with Bobur (name)
https://t.me/ITwithBobur (url)
"""
result = parse_telegram_data(text)
