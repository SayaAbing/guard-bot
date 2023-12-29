import os.path

from typing import List, Optional


API_ID: int = 14920143
API_HASH: str = "5a316e55fb121d9b5e891b5ff07d4677"
TOKEN: str = "6316018634:AAGUWzU7SED1W6YsMnWubx_4Y1YXhN9sLrk"

log_chat: int = -1002062758454
sudoers: List[int] = [1715037142, 5628785242]
super_sudoers: List[int] = [1715037142, 5628785242]

prefix: List[str] = ["/", "!", ".", "$", "-"]

disabled_plugins: List[str] = []

WORKERS = 24

DATABASE_PATH = os.path.join("eduu", "database", "eduu.db")

TENOR_API_KEY: Optional[str] = "X9HD35B7ZGP6"

sudoers.extend(super_sudoers)

# notes

# 1. api_id & api_hash get from my.telegram.org
# 2. token fill with your bot_token get from @BotFather
# 3. log_chat fill with the chat id of a group that you should create for the bot logger
# 4. [optional] var disabled_plugins let you to disable an plugin to be loaded. Example:
# You don't want the youtube plugin to be loaded, then fill disabled_plugins var with youtube (or any name of the plugins file)
