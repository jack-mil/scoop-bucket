import json
import os
from pathlib import Path
import subprocess as subp


def main():
    THISDIR = Path(__file__).parent
    os.chdir(THISDIR)

    proc = subp.run(f'powershell ./bin/checkver.ps1 -U', stdout=subp.PIPE)
    print(proc.stdout.decode())

    # Get unstaged changed to manifests in ./bucket
    proc = subp.run('git diff --name-only ./bucket', stdout=subp.PIPE)
    manifests = proc.stdout.decode().splitlines()

    # If no updates, exit
    if not len(manifests):
        print('All apps up to date')
        return

    # Just ensure only working with .json manifests
    for manifest in filter(lambda x: x.endswith('.json'), manifests):
        subp.run(f'git add {manifest}')
        # Parse the json to get new version
        with open(manifest, 'r') as f:
            file = json.load(f)
            vers = file['version']
        # Make a commit for each app
        subp.run(
            f'git commit -m "Update {Path(manifest).stem} to version {vers}"')


if __name__ == '__main__':
    main()
