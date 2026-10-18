"""Verify SHA256SUMS.txt and ensure its paths stay inside the release directory.

SPDX-License-Identifier: MIT
"""
import argparse
import hashlib
from pathlib import Path


def verify(directory):
    directory = directory.resolve()
    lines = (directory / 'SHA256SUMS.txt').read_text('utf-8-sig').splitlines()
    if not lines:
        raise SystemExit('Empty checksum manifest')
    for line in lines:
        expected, name = line.split('  ', 1)
        path = (directory / name).resolve()
        if not path.is_relative_to(directory):
            raise SystemExit('Checksum path escapes release directory')
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != expected.lower():
            raise SystemExit('Checksum mismatch: ' + name)
        print('OK: ' + name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', nargs='?', type=Path,
                        default=Path(__file__).resolve().parents[1])
    verify(parser.parse_args().directory)
