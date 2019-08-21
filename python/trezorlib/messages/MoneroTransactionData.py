# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MoneroTransactionDestinationEntry import MoneroTransactionDestinationEntry
from .MoneroTransactionRsigData import MoneroTransactionRsigData

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class MoneroTransactionData(p.MessageType):

    def __init__(
        self,
        version: int = None,
        payment_id: bytes = None,
        unlock_time: int = None,
        outputs: List[MoneroTransactionDestinationEntry] = None,
        change_dts: MoneroTransactionDestinationEntry = None,
        num_inputs: int = None,
        mixin: int = None,
        fee: int = None,
        account: int = None,
        minor_indices: List[int] = None,
        rsig_data: MoneroTransactionRsigData = None,
        integrated_indices: List[int] = None,
        client_version: int = None,
        hard_fork: int = None,
        monero_version: bytes = None,
    ) -> None:
        self.version = version
        self.payment_id = payment_id
        self.unlock_time = unlock_time
        self.outputs = outputs if outputs is not None else []
        self.change_dts = change_dts
        self.num_inputs = num_inputs
        self.mixin = mixin
        self.fee = fee
        self.account = account
        self.minor_indices = minor_indices if minor_indices is not None else []
        self.rsig_data = rsig_data
        self.integrated_indices = integrated_indices if integrated_indices is not None else []
        self.client_version = client_version
        self.hard_fork = hard_fork
        self.monero_version = monero_version

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('version', p.UVarintType, 0),
            2: ('payment_id', p.BytesType, 0),
            3: ('unlock_time', p.UVarintType, 0),
            4: ('outputs', MoneroTransactionDestinationEntry, p.FLAG_REPEATED),
            5: ('change_dts', MoneroTransactionDestinationEntry, 0),
            6: ('num_inputs', p.UVarintType, 0),
            7: ('mixin', p.UVarintType, 0),
            8: ('fee', p.UVarintType, 0),
            9: ('account', p.UVarintType, 0),
            10: ('minor_indices', p.UVarintType, p.FLAG_REPEATED),
            11: ('rsig_data', MoneroTransactionRsigData, 0),
            12: ('integrated_indices', p.UVarintType, p.FLAG_REPEATED),
            13: ('client_version', p.UVarintType, 0),
            14: ('hard_fork', p.UVarintType, 0),
            15: ('monero_version', p.BytesType, 0),
        }
