import requests

ENDPOINT = 'https://api.cdnjs.com/libraries'
CDN = 'https://cdnjs.cloudflare.com/ajax/libs'

# tags in package names that indicate we'd rather skip this one as a default
IDEALLY_SKIP = ['alpha', 'beta']


def api(data):
    response = requests.get(ENDPOINT, params=data)
    if response.ok:
        return response.json()['results']
    else:
        raise Exception('Unable to fetch results.')


def search(text, fields=None):
    data = {'search': text}
    if fields is not None:
        if isinstance(fields, list):
            fields = ','.join(fields)
        data['fields'] = fields
    return api(data)


def grab(name):
    results = search(name, fields='assets')
    if results and results[0]['name'] == name:
        return results[0]


def select_default(versions):
    for v in versions:
        vnum = v['version']
        if any(tag in vnum for tag in IDEALLY_SKIP):
            continue
        return v
    # if we couldn't find a good one after skipping, we gotta use what's left
    return v[0]


def asset_url(pkg, version, file):
    return '/'.join([CDN, pkg, version, file])
