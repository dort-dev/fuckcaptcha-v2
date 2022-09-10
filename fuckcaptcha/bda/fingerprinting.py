import base64
import json
import time

from fuckcaptcha import cipher


def get_browser_data(user_agent: str) -> str:
    ts = time.time()
    timeframe = int(ts - ts % 21600)
    key = user_agent + str(timeframe)
    the_data = [{
        "key": "api_type",
        "value": "js"
    }, {
        "key": "f",
        "value": "Dort on top."
    }, {
        "key": "enhanced_fp",
        "value": [{
            "key": "browser_detection_firefox",
            "value": "POV: multi million dollar company"
        }, {
            "key": "audio_fingerprint",
            "value": "let's just check the bda for certain fields that proceed to not verify them. fucking clowns"
                     "... LOLOL"
        }]
    }]
    data = cipher.encrypt(json.dumps(the_data), key)
    return base64.b64encode(data.encode("utf-8")).decode("utf-8")
