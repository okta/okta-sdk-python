from .okta_utils import Utils


def Collection(client, url, model):
    """
    Generic generator method for returning paged results.
    """
    while True:
        r = client.http.get(url)
        r_json = Utils.validate_response(r)

        for obj in r_json:
            # Convert json to correct object type
            yield model(obj, client)

        if 'next' in r.links:
            url = r.links['next']['url']
        else:
            break
