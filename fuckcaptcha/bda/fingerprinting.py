import random

from fuckcaptcha import cipher
import base64
import json
import secrets
import time


def get_browser_data(user_agent: str) -> str:
    ts = time.time()
    timeframe = int(ts - ts % 21600)
    key = user_agent + str(timeframe)
    the_data = [{
        "key": "api_type",
        "value": "js"
    }, {
        "key": "f",
        "value": secrets.token_hex(16)
    }, {
        "key": "enhanced_fp",
        "value": [{
            "key": "audio_fingerprint",
            "value": "nice fucking job funcaptcha you really fucking folded to this?"
        }]
    }]
    data = cipher.encrypt(json.dumps(the_data), key)
    return base64.b64encode(data.encode("utf-8")).decode("utf-8")
