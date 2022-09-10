import random
import string

from fuckcaptcha.bda import fingerprinting


def rand_str(length) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length)).upper()


def rand_platform_token() -> str:
    return f"{rand_str(10)} {rand_version()}".upper()


def rand_version() -> str:
    digits = []
    for i in range(2):
        digits.append("".join(random.choices(string.digits, k=3)))
    return ".".join(digits)


def rand_bda() -> dict:
    agent = f"Firefox/{rand_version()} {rand_str(5)}/{rand_version()} OP/{rand_version()}"
    return {
        "bda": fingerprinting.get_browser_data(agent),
        "agent": agent
    }
