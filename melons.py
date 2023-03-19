"""Classes for melon orders."""


class AbstractMelonOrder:
    order_type = None
    tax = None

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def __repr__(self):
        return f"<species={self.species} qty={self.qty} shipped={self.shipped} order_type={self.order_type} tax={self.tax}>"

    def get_total(self):
        """Calculate price, including tax."""

        if self.species.lower() == "christmas":
            price_multiplier = 1.5
        else:
            price_multiplier = 1

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price * price_multiplier

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code

    def __repr__(self):
        return super().__repr__()[:-1] + f' country_code={self.country_code}>'

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    order_type = 'government'
    tax = 0

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def __repr__(self):
        return super().__repr__()[:-1] + f' passed_inspection={self.passed_inspection}>'

    def mark_inspection(self, passed):
        self.passed_inspection = passed
