from stk._internal.key_makers.molecule import MoleculeKeyMaker
from stk._internal.key_makers.utilities import get_inchi_key
from stk._internal.molecule import Molecule


class InchiKey(MoleculeKeyMaker):
    """
    Used to get the InChIKey of molecules.

    """

    def __init__(self) -> None:
        return

    def get_key_name(self) -> str:
        return "InChIKey"

    def get_key(self, molecule: Molecule) -> str:
        return get_inchi_key(molecule)

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return "InchiKey()"
