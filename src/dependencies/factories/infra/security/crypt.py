# VerdanTech Source
from src.infra.security.crypt.passlib import PasslibPasswordCrypt


async def provide_passlib_crypt():
    """Provide passlib password crypt for dependency injection"""
    return PasslibPasswordCrypt()
