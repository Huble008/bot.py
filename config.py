import random
import string

# Helper function to generate recovery codes
def generate_recovery_code():
    """Generate a random recovery code."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))