"""
Setting version
"""

if __name__ == '__main__':
    import sys
    import toml
    if len(sys.argv) < 2:
        sys.exit(1)
    ref = sys.argv[1]
    version = ref.removeprefix('refs/tags/')
    print(version)
    with open("pyproject_setting.toml", "r") as f:
        parsed_toml = toml.loads(f.read())
    parsed_toml['project']['version'] = version
    with open("pyproject.toml", "w") as f:
        toml.dump(parsed_toml, f)
