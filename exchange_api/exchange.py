import json


class Exchange:

    # # NAME must be set in subclass.
    # NAME = "Coinbase"
    NAME = None

    # # PARAM_NAMES must be set in subclass.
    # PARAM_NAMES = {
    #     "api_key": "API Key",
    #     "api_secret": "API Secret",
    #     "api_pass": "API Passphrase"
    # }
    PARAM_NAMES = None

    def __init__(self, params):
        self.params = params
        self.__wallets = {}
        if self.NAME is None:
            raise NotImplementedError("Class Variable 'NAME' Requires Non-None Value.")
        if self.PARAM_NAMES is None:
            raise NotImplementedError("Class Variable 'PARAM_NAMES' Requires Non-None Value.")

    def proc(self):
        raise NotImplementedError("Implementation Required.")

    def add_wallet(self, identifier, quantity, cost_basis, currency_name):
        self.__wallets[identifier] = {'quantity': quantity, 'cost_basis': cost_basis, 'currency_name': currency_name}

    def update_wallet(self, identifier, quantity=None, cost_basis=None, currency_name=None):
        if identifier not in self.__wallets:
            raise ValueError(f"Identifier '{identifier}' does not exist in wallets.")
        if quantity is not None:
            self.__wallets[identifier]['quantity'] = quantity
        if cost_basis is not None:
            self.__wallets[identifier]['cost_basis'] = cost_basis
        if currency_name is not None:
            self.__wallets[identifier]['currency_name'] = currency_name

    def json(self):
        return json.jsonify(self.__wallets)

