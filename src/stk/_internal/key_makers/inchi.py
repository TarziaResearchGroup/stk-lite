from stk._internal.key_makers.molecule import MoleculeKeyMaker
from stk._internal.key_makers.utilities import get_inchi
from stk._internal.molecule import Molecule


class Inchi(MoleculeKeyMaker):
    """
    Used to get the InChI of molecules.

    """

    def __init__(self) -> None:
        return

    def get_key_name(self) -> str:
        return "InChI"

    def get_key(self, molecule: Molecule) -> str:
        return get_inchi(molecule)

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return "Inchi()"
