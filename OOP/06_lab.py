from abc import ABC, abstractmethod


class CreditCard:
    def __init__(self):
        self.bank_name = None
        self.card_limit = None
        self.card_type = None
        self.installment_shopping = None


class CreditCardBuilder(ABC):
    def __init__(self):
        self._credit_card = CreditCard()

    @property
    def credit_card(self) -> CreditCard:
        return self._credit_card

    @abstractmethod
    def bank_name_func(self) -> str:
        pass

    @abstractmethod
    def card_limit_func(self) -> int:
        pass

    @abstractmethod
    def card_type_func(self) -> str:
        pass

    @abstractmethod
    def installment_shopping(self) -> str:
        pass


class AmericanExpressCard(CreditCardBuilder):
    def __init__(self):
        super().__init__()

    def bank_name_func(self) -> str:
        self.credit_card.bank_name = "Garanti"
        return self.credit_card.bank_name

    def card_limit_func(self) -> int:
        self.credit_card.card_limit = 1000000
        return self.credit_card.card_limit

    def card_type_func(self) -> str:
        self.credit_card.card_type = "AE"
        return self.credit_card.card_type

    def installment_shopping(self) -> str:
        self.credit_card.installment_shopping = "yes"
        return self.credit_card.installment_shopping


class VisaCard(CreditCardBuilder):
    def __init__(self):
        super().__init__()

    def bank_name_func(self) -> str:
        self.credit_card.bank_name = "ISB"
        return self.credit_card.bank_name

    def card_limit_func(self) -> int:
        self.credit_card.card_limit = 2000000
        return self.credit_card.card_limit

    def card_type_func(self) -> str:
        self.credit_card.card_type = "Visa"
        return self.credit_card.card_type

    def installment_shopping(self) -> str:
        self.credit_card.installment_shopping = "none"
        return self.credit_card.installment_shopping


class Creator:
    @staticmethod
    def create(credit_card_builder: CreditCardBuilder) -> None:
        print(
            f'Bank Name: {credit_card_builder.bank_name_func()}\n'
            f'Card Limit: {credit_card_builder.card_limit_func()}\n'
            f'Card Type: {credit_card_builder.card_type_func()}\n'
            f'Shopping: {credit_card_builder.installment_shopping()}\n'
        )


def main():
    print("--- American Express ---")
    Creator.create(credit_card_builder=AmericanExpressCard())

    print("--- Visa Card ---")
    Creator.create(credit_card_builder=VisaCard())


if __name__ == "__main__":
    main()