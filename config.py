import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("7091128043:AAF6_dq4UK7yoBOTKSWrAG05OBdO7Syt4j0")

auth_users = os.getenv("AUTH_USERS", "7360968885")  # comma-separated string
sudo_users = [int(num) for num in auth_users.split(",") if num.strip().isdigit()]

osowner_users = os.getenv("OSOWNER_USERS", "7360968885")
owner_users = [int(num) for num in osowner_users.split(",") if num.strip().isdigit()]
