# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class EosActionVoteProducer(p.MessageType):

    def __init__(
        self,
        voter: int = None,
        proxy: int = None,
        producers: List[int] = None,
    ) -> None:
        self.voter = voter
        self.proxy = proxy
        self.producers = producers if producers is not None else []

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('voter', p.UVarintType, 0),
            2: ('proxy', p.UVarintType, 0),
            3: ('producers', p.UVarintType, p.FLAG_REPEATED),
        }
