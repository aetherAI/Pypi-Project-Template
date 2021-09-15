import io
import re
import sys
from contextlib import redirect_stderr

import anybadge
import pip
import toml


def main():
    output_file = sys.argv[1]
    project_name = toml.load('pyproject.toml')['tool']['poetry']['name']

    stream = io.StringIO()
    with redirect_stderr(stream):
        pip.main(f"install {project_name}==".split())

    p = re.compile(r"from versions: (.+)\)")
    m = p.search(stream.getvalue())
    latest_version = m.group(1).rsplit(', ', maxsplit=1)[-1]

    print("find latest version:", latest_version)
    args = f'-l pypi -v {latest_version} -f {output_file} -c green -o'.split(' ')
    anybadge.main(args)
    print(f"successfully write badge to {output_file}")


if __name__ == '__main__':
    main()
