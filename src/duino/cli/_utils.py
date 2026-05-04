from __future__ import annotations

import sys

import duino

from .. import Duino, _load_client

def get_client() -> Duino:
    return _load_client()


def organization_info() -> str:
    organization = Duino.organization
    if organization is not None:
        return "[organization={}] ".format(organization)

    return ""


def print_model(model: BaseModel) -> None:
    sys.stdout.write(model_json(model, indent=2) + "\n")


def can_use_http2() -> bool:
    try:
        import h2  # type: ignore  # noqa
    except ImportError:
        return False

    return True
