"""Build the portable ZIP with explicit LF text and reproducible ZIP metadata."""
import pathlib
import zipfile

root = pathlib.Path(__file__).resolve().parents[1]
source = root / 'skills' / 'prompt-architect-executor'
archive = root / 'skills' / 'prompt-architect-executor.zip'
members = ['LICENSE', 'README.md', 'SKILL.md']
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for name in members:
        path = source / name
        content = path.read_bytes().replace(b'\r\n', b'\n')
        path.write_bytes(content)
        entry = zipfile.ZipInfo('prompt-architect-executor/' + name, (2026, 10, 31, 0, 0, 0))
        entry.compress_type = zipfile.ZIP_DEFLATED
        entry.external_attr = 0o100644 << 16
        z.writestr(entry, content)
print('Built', archive.name, 'with LF text and fixed metadata')
