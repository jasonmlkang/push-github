import sys
import argparse
import getpass
import requests
import json
import base64


parser = argparse.ArgumentParser()
parser.add_argument('--username', default=None)
parser.add_argument('--repo-base-url', default=None)
parser.add_argument('--repo-owner', default=None)
parser.add_argument('--repo-name', default=None)
parser.add_argument('--local-file', default=None)
parser.add_argument('--remote-file-name', default=None)
args = parser.parse_args()


def _print_missing(name):
    print "{} is missing".format(name)
    sys.exit(0)


def _byteify(input):
    """
    Turns {u'key': 'value', u'key2':[], u'key3': {}}
      into {'key':'value', 'key2':[], 'key3': {}}
    """
    if isinstance(input, dict):
        return {_byteify(key):_byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [_byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


def _parse_json(data):
    d = json.loads(data)
    return _byteify(d)


def _get_github(username, password, base_url, repo_owner, repo_name, remote_file_name):
    url = "https://{base_url}/api/v3/repos/{repo_owner}/{repo_name}/contents/{remote_file_name}".format(
        base_url=base_url,
        repo_owner=repo_owner,
        repo_name=repo_name,
        remote_file_name=remote_file_name,
    )

    try:
        res = requests.get(
            url=url,
            auth=(username, password),
            timeout=10,
        )

        if res.status_code != requests.codes.ok:
            raise Exception("Cannot get file from {}".format(url))
    except Exception as e:
        print e
        sys.exit(0)

    try:
        res_text = _parse_json(res.text)
    except Exception as e:
        print e
        sys.exit(0)

    return res_text


def _put_github(username, password, base_url, repo_owner, repo_name, remote_file_name, content, sha):
    url = "https://{base_url}/api/v3/repos/{repo_owner}/{repo_name}/contents/{remote_file_name}".format(
        base_url=base_url,
        repo_owner=repo_owner,
        repo_name=repo_name,
        remote_file_name=remote_file_name
    )

    payload = {
        "message": "Updating {}".format(remote_file_name),
        "content": base64.b64encode(content),
        "sha": sha,
    }

    print url
    print json.dumps(payload)

    try:
        res = requests.put(
            url=url,
            auth=(username, password),
            data=json.dumps(payload),
            timeout=10,
        )

        if res.status_code != requests.codes.ok:
            print res.text
            raise Exception("Cannot update file on {}".format(url))
    except Exception as e:
        print e
        sys.exit(0)


def run():
    if not args.username:
        _print_missing("username")
    if not args.base_url:
        _print_missing("base-url")
    if not args.repo_owner:
        _print_missing("repo-owner")
    if not args.repo_name:
        _print_missing("repo-name")
    if not args.local_file:
        _print_missing("local-file")
    if not args.remote_file_name:
        _print_missing("remote-file-name")

    password = getpass.getpass("Password:")

    # Get sha of the file
    res = _get_github(args.username, password, args.base_url, args.repo_owner, args.repo_name, args.remote_file_name)

    if not "sha" in res:
        print "Cannot get sha"
        sys.exit(0)
    sha = res["sha"]

    # Update with new content
    with open(args.local_file, 'r') as f:
        content = f.read()
    if content:
        _put_github(args.username, password, args.base_url, args.repo_owner, args.repo_name, args.remote_file_name, content, sha)


if __name__ == '__main__':
    run()
