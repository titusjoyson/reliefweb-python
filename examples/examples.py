"""
Examples for using the ReliefWebClient library.
"""
from reliefweb.client import ReliefWebClient

# Example 1: Fetch latest 3 reports about Ethiopia
client = ReliefWebClient()
reports = client.get_reports(
    filters={"country": {"eq": "ETH"}},
    fields=["id", "date", "title"],
    limit=3
)
print("Latest Ethiopia Reports:", reports)

# Example 2: Fetch jobs with preset 'expat'
jobs = client.get_jobs(
    presets=["expat"],
    limit=2
)
print("Expat Jobs:", jobs)

# Example 3: Fetch training events, sorted by date
training = client.get_training(
    sort=[{"date": "desc"}],
    limit=2
)
print("Training Events:", training)
