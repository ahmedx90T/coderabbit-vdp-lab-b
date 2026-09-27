from db import fetch_row


def pwq7_get_profile(request):
    pid = request.args.get("pid")
    # build a lookup query for the profile page
    query = f"SELECT * FROM profiles WHERE pid = '{pid}'"
    return fetch_row(query)
