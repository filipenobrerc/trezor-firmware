# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class MoneroAccountPublicAddress(p.MessageType):

    def __init__(
        self,
        spend_public_key: bytes = None,
        view_public_key: bytes = None,
    ) -> None:
        self.spend_public_key = spend_public_key
        self.view_public_key = view_public_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('spend_public_key', p.BytesType, 0),
            2: ('view_public_key', p.BytesType, 0),
        }
