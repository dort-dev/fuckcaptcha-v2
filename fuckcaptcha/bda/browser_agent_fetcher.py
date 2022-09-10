import funny.user_agent_fuckery
import random
import string

from faker import Faker
from fuckcaptcha.bda import fingerprinting
from faker.providers.user_agent import Provider


provider = Provider(Faker())


def rand_str(length) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))


def rand_platform_token() -> str:
    return f"{rand_str(10)} {rand_version()}".upper()


def rand_version() -> str:
    digits = []
    for i in range(2):
        digits.append("".join(random.choices(string.digits, k=3)))
    return ".".join(digits)


def rand_bda() -> dict:
    agent = funny.user_agent_fuckery.agent()
    return {
        "bda": fingerprinting.get_browser_data(agent),
        "agent": agent
    }
