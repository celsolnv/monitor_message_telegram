from requests_toolbelt import sessions


API_URL = "http://localhost:8000"

api = sessions.BaseUrlSession(base_url=API_URL)
