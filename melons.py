"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    
    
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3 

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty, order_type= "domestic", tax= 0.08,):
        """Initialize melon order attributes"""
        super().__init___(species, qty, order_type, tax)

    

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, order_type= "international", tax= 0.17, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, order_type, tax, country_code)
        
        self.country_code = country_code

   


    def get_country_code(self):
        """Return the country code."""
        
        return self.country_code

        
