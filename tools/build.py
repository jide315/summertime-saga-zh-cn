"""Build zh_cn.rpa using a separately installed 0.20.16 Windows game.

SPDX-License-Identifier: MIT
"""
import argparse
import hashlib
import os
from pathlib import Path
import pickle
import shutil
import subprocess
import tempfile
import zlib

ROOT = Path(__file__).resolve().parents[1]


def pack(destination, entries):
    """Write an RPA-3.0 archive with a Python-2-compatible index."""
    key = 0x42424242
    index = {}
    with destination.open('wb') as stream:
        stream.write(b'RPA-3.0 ' + b'0' * 16 + b' 42424242\n')
        for name, path in sorted(entries):
            data = path.read_bytes()
            index[name] = [(stream.tell() ^ key, len(data) ^ key, b'')]
            stream.write(data)
        offset = stream.tell()
        stream.write(zlib.compress(pickle.dumps(index, protocol=2)))
        stream.seek(0)
        stream.write(('RPA-3.0 %016x %08x\n' % (offset, key)).encode('ascii'))


def build(game_root, output):
    runtime = game_root / 'lib/windows-i686/python.exe'
    bootstrap = game_root / 'SummertimeSaga.py'
    for path in (runtime, bootstrap, game_root / 'game/scripts.rpa'):
        if not path.is_file():
            raise SystemExit('Missing required game file: ' + str(path))
    if output == ROOT / 'zh_cn.rpa':
        raise SystemExit('Use dist/ for builds; preserve the original release archive.')
    if output.is_relative_to(game_root):
        raise SystemExit('Output must be outside the installed game.')
    output.parent.mkdir(parents=True, exist_ok=True)
    workspace = ROOT / '.build'
    workspace.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='compile-', dir=workspace) as temp:
        project = Path(temp)
        game = project / 'game'
        shutil.copytree(ROOT / 'patch/game', game)
        # Link only stock archives. Compilation writes into the private copy.
        for name in ('audio.rpa', 'fonts.rpa', 'images.rpa', 'scripts.rpa', 'data.rpa'):
            source = game_root / 'game' / name
            if source.is_file():
                try:
                    os.link(source, game / name)
                except OSError:
                    shutil.copy2(source, game / name)
        for name in ('script_version.txt', 'presplash.jpg', 'changelog.txt', 'pledge_list.txt'):
            source = game_root / 'game' / name
            if source.is_file():
                shutil.copy2(source, game / name)
        for name in ('legal',):
            source = game_root / 'game' / name
            if source.is_dir():
                shutil.copytree(source, game / name)
        env = dict(os.environ, PYTHONIOENCODING='utf-8')
        subprocess.run([str(runtime), '-O', str(bootstrap), str(project), 'compile'],
                       cwd=runtime.parent, env=env, check=True)
        entries = []
        for source in sorted((ROOT / 'patch/game').rglob('*')):
            if not source.is_file():
                continue
            relative = source.relative_to(ROOT / 'patch/game')
            if source.suffix == '.rpy':
                relative = relative.with_suffix('.rpyc')
            compiled = game / relative
            if not compiled.is_file():
                raise SystemExit('Compilation did not produce: ' + str(relative))
            entries.append((relative.as_posix(), compiled))
        staged_output = project / 'zh_cn.rpa'
        pack(staged_output, entries)
        shutil.copy2(staged_output, output)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    (output.parent / 'SHA256SUMS.txt').write_text(
        digest + '  ' + output.name + '\n', encoding='utf-8')
    print('Built %s (%d members)\nSHA-256: %s' % (output, len(entries), digest))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game-dir', required=True, type=Path)
    parser.add_argument('--out', type=Path, default=ROOT / 'dist/zh_cn.rpa')
    args = parser.parse_args()
    build(args.game_dir.resolve(), args.out.resolve())
