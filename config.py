import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

auth_users = os.getenv("AUTH_USERS", "")  # comma-separated string
sudo_users = [int(num) for num in auth_users.split(",") if num.strip().isdigit()]

osowner_users = os.getenv("OSOWNER_USERS", "")
owner_users = [int(num) for num in osowner_users.split(",") if num.strip().isdigit()]
