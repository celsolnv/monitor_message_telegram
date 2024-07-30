from .api import api


def bet_aviator(reference: str):
    data = {"reference_result": f"{reference}x", "limit": "2"}
    res = api.post("/bet", json=data)
    print(res.json())
    return res.json()


def get_value():
    res = api.get("/value")
    value = res.json().get("value")
    return value


def refresh():
    res = api.get("/refresh")
    return res.json()
