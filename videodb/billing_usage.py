"""Module for BillingUsage schema."""

class BillingUsage:
    """Represents billing usage details."""

    def __init__(self, credit_balance=None, usage_this_month=None, breakdown=None):
        """
        :param float credit_balance: Remaining credit balance
        :param float usage_this_month: Usage total for the current month
        :param dict breakdown: Detailed usage breakdown by category
        """
        self.credit_balance = credit_balance
        self.usage_this_month = usage_this_month
        self.breakdown = breakdown or {}

    def __repr__(self):
        return (
            f"BillingUsage(credit_balance={self.credit_balance}, "
            f"usage_this_month={self.usage_this_month}, breakdown={self.breakdown})"
        )

    def to_json(self):
        """Return JSON-serializable dict representation."""
        return {
            "credit_balance": self.credit_balance,
            "usage_this_month": self.usage_this_month,
            "breakdown": self.breakdown,
        }
