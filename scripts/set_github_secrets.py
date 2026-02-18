#!/usr/bin/env python3
import os
import subprocess
import argparse
import shlex

def parse_env(path):
    res = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' not in line:
                continue
            k, v = line.split('=', 1)
            res.append((k.strip(), v.strip()))
    return res


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env-file', default='.env.prod')
    parser.add_argument('--repo', default=None)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    pairs = parse_env(args.env_file)
    for k, v in pairs:
        cmd = ['gh', 'secret', 'set', k, '--body', v]
        if args.repo:
            cmd += ['--repo', args.repo]
        if args.dry_run:
            print('DRY:', ' '.join(shlex.quote(x) for x in cmd))
        else:
            subprocess.run(cmd, check=True)


if __name__ == '__main__':
    main()

