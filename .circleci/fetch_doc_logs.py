import json
import os
from pathlib import Path
import sys
from urllib.parse import urlparse
from urllib.request import urlopen


if len(sys.argv) != 2:
    print('USAGE: fetch_doc_results.py CircleCi-build-url')
    sys.exit()

target_url = urlparse(sys.argv[1])
*_, organization, repository, build_id = target_url.path.split('/')
print(f'Fetching artifacts from {organization}/{repository} for {build_id}')

artifact_url = (
    f'https://circleci.com/api/v2/project/gh/'
    f'{organization}/{repository}/{build_id}/artifacts'
)
print(artifact_url)
with urlopen(artifact_url) as response:
    artifacts = json.load(response)
artifact_count = len(artifacts['items'])
print(f'Found {artifact_count} artifacts')

with open(os.environ['GITHUB_OUTPUT'], 'w+') as fd:
    fd.write(f'count={artifact_count}\n')

logs = Path('logs')
logs.mkdir(exist_ok=True)

found = False
for item in artifacts['items']:
    path = item['path']
    if path.startswith('doc/logs/'):
        path = Path(path).name
        print(f'Downloading {path} from {item["url"]}')
        with urlopen(item['url']) as response:
            (logs / path).write_bytes(response.read())
        found = True

if not found:
    print('ERROR: Did not find any artifact logs!')
