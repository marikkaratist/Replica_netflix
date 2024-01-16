import base64
import hashlib
import hmac

from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


# TODO: [security] Описать функцию compose_passwords(password_hash: Union[str, bytes], password: str)
def compare_passwords(self, password_hash, other_password) -> bool:
    decoded_digest = base64.b64decode(password_hash)
    hashed_password: bytes = hashlib.pbkdf2_hmac(
        hash_name=constants.HASH_NAME,
        salt=constants.HASH_SALT.encode('utf-8'),
        iterations=constants.HASH_GEN_ITERATIONS,
        password=other_password.encode('utf-8'),
    )
    return hmac.compare_digest(decoded_digest, hashed_password)
