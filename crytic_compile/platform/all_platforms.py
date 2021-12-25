"""
Module containing all the platforms
"""
# pylint: disable=unused-import
from .archive import Archive
from .brownie import Brownie
from .buidler import Buidler
from .dapp import Dapp
from .embark import Embark
from .etherlime import Etherlime
from .etherscan import (
    Etherscan,
    Kovan,
    Ropsten,
    Rinkeby,
    Goerli,
    Arbitrum,
    ArbitrumTestnet,
    Avalanche,
    AvalancheTestnet,
    Binance,
    BinanceTestnet,
    Fantom,
    Tobalaba,
    Polygon,
)
from .hardhat import Hardhat
from .solc import Solc
from .solc_standard_json import SolcStandardJson
from .standard import Standard
from .truffle import Truffle
from .vyper import Vyper
from .waffle import Waffle
from .foundry import Foundry
