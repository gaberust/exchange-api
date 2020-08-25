import json


class Exchange:

    def __init__(self, params):
        self.params = params
        self.__wallets = {}

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

