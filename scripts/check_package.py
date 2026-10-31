import pathlib, zipfile, hashlib
root = pathlib.Path(__file__).resolve().parents[1]
source = root / 'skills' / 'prompt-architect-executor'
archive = root / 'skills' / 'prompt-architect-executor.zip'
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None, 'Archive CRC failure'
    files = sorted(p for p in source.rglob('*') if p.is_file())
    expected = {str(pathlib.PurePosixPath('prompt-architect-executor') / p.relative_to(source).as_posix()) for p in files}
    assert set(z.namelist()) == expected, 'Unexpected or missing archive files'
    assert {'prompt-architect-executor/SKILL.md', 'prompt-architect-executor/README.md', 'prompt-architect-executor/LICENSE'} <= expected
    for p in files:
        member = 'prompt-architect-executor/' + p.relative_to(source).as_posix()
        assert b'\r\n' not in z.read(member), 'Non-canonical text line endings: ' + member
        assert z.read(member) == p.read_bytes(), 'Source/archive mismatch: ' + member
    assert (source / 'SKILL.md').read_text(encoding='utf-8').startswith('---\nname: prompt-architect-executor\n')
print('PASS: archive CRC, exact member set, required files, skill metadata and byte parity')
print('SKILL.md sha256:', hashlib.sha256((source / 'SKILL.md').read_bytes()).hexdigest())
