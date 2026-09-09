import os
import json

# Get API_ID and API_HASH from https://my.telegram.org -> API Development Tools
# Get BOT_TOKEN from @BotFather on Telegram
API_ID    = int(os.environ.get('35884204',    '0'))   # your Telegram API ID (integer)
API_HASH  =     os.environ.get('ef7ef931449f4befcbb718c309001f14',  '')     # your Telegram API hash
BOT_TOKEN =     os.environ.get('8893770779:AAGqpLYa6UqwG_98kjGbntyJDexPMp3XLQ0', '')     # your bot token from @BotFather
TG_API    = f"https://api.telegram.org/bot{BOT_TOKEN}"

BOT_BRAND      = '𝑺𝑯𝑶𝑷𝑰 𝑰𝑵𝑭𝑬𝑹𝑵𝑶'
OWNER_NAME     = '𝙄𝙉𝙁𝙀𝙍𝙉𝙊_𝙓𝙍'                        # display name shown in bot messages
OWNER_USERNAME = 'Inferno_XR'                     # your Telegram username (without @)
OWNER_ID       = 6857145175                                  # your Telegram user ID (integer)
DEV_LINE       = f'💻 <b>Dev</b>  »  <a href="https://t.me/{OWNER_USERNAME}">{OWNER_NAME}</a>'

MASS_WORKERS = int(os.environ.get('MASS_WORKERS', '30'))

_ADMIN_FILE     = os.path.join(os.path.dirname(__file__), 'admin.json')
_DEFAULT_ADMINS = (
    {int(x.strip()) for x in os.environ.get('ADMIN_ID', '').split(',') if x.strip().isdigit()}
    | ({OWNER_ID} if OWNER_ID else set())
)


def _load_admin_ids() -> set:
    try:
        with open(_ADMIN_FILE) as f:
            data = json.load(f)
            ids  = data.get('admin_ids', [])
            return set(ids) | _DEFAULT_ADMINS if ids else _DEFAULT_ADMINS
    except Exception:
        return _DEFAULT_ADMINS


def _save_admin_ids(ids: set):
    try:
        with open(_ADMIN_FILE) as f:
            data = json.load(f)
    except Exception:
        data = {}
    data['admin_ids'] = list(ids)
    with open(_ADMIN_FILE, 'w') as f:
        json.dump(data, f)


ADMIN_IDS = _load_admin_ids()
ADMIN_ID  = OWNER_ID

PREMIUM_FILE    = 'premium.txt'
SITES_FILE      = 'sites.txt'
PROXY_FILE      = 'proxy.txt'
USER_PROXY_FILE = 'user_proxies.json'
USER_POOL_FILE  = 'user_pool.json'

LIMITS = {
    "admin":   5000,
    "premium": 2500,
}
