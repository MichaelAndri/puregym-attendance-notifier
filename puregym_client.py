from puregym import PuregymAPIClient

def get_current_count(email: str, pin: str, gym: str = None) -> int:
    """
    Logs in, fetches attendance, and returns the current headcount.
    """
    client = PuregymAPIClient()
    client.login(email, pin)
    return client.get_gym_attendance(gym)