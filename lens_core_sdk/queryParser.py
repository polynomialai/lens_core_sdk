import requests
import json


def parseQuery(query, env, authenticationURI):
    body = {"query": query, "authenticationURI": authenticationURI}
    if env == "prod":
        url = "https://intelligence.polynomial.ai/lens_core_prod/queryParser"
    else:
        url = "https://intelligence.polynomial.ai/lens_core_dev/queryParser"
    res = requests.post(url=url, json=body)
    response = json.loads(res.text)
    if response["status"]:
        return response["response"]
    else:
        return []


if __name__ == "__main__":
    print(parseQuery("pgs with wifi"))
