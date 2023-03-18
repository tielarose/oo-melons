"""Classes for melon orders."""


class AbstractMelonOrder:
    # order_type = None
    # tax = None

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        # can this be an attribute up top? Or does it need to be here in init?
        self.shipped = False

    def __repr__(self):
        return f'<species={self.species} qty={self.qty} shipped={self.shipped}>'
        # do we need to add order_type and tax to the repr? Does the repr go here or in the subclasses?

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

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

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
