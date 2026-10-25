# Release integrity scan

[![Monthly scan](https://github.com/keelinfra/release-integrity/actions/workflows/scan.yml/badge.svg)](https://github.com/keelinfra/release-integrity/actions/workflows/scan.yml)
[![Tests](https://github.com/keelinfra/release-integrity/actions/workflows/test.yml/badge.svg)](https://github.com/keelinfra/release-integrity/actions/workflows/test.yml)
[![Swappable releases](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fkeelinfra%2Frelease-integrity%2Fmain%2Fresults%2Flatest.json&query=%24.swappable_share&label=swappable%20releases&color=orange)](results/trend.csv)
[![Last scan](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fkeelinfra%2Frelease-integrity%2Fmain%2Fresults%2Flatest.json&query=%24.date&label=last%20scan&color=blue)](results)
[![License](https://img.shields.io/badge/license-Apache--2.0%20code%20%7C%20CC%20BY%204.0%20data-green)](#license)

Could someone with write access to a repository replace the files in its
latest GitHub release, and would a downloader be able to tell?

Once a month, [`scan.py`](scan.py) takes every Go and Rust repository tagged
`cli` with at least 1,000 stars, keeps those whose latest release is under a
year old and ships binaries, and records for that latest release:

| Column | Meaning |
|---|---|
| `immutable` | GitHub [immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases) are on: files can't be replaced, the tag can't move |
| `provenance` | a GitHub build-provenance attestation exists for its binaries (up to two binaries and one checksum file are looked up) |
| `signed` | it ships signature files (cosign/Sigstore, GPG, minisign, SLSA `.intoto.jsonl`) |
| `checksums` | it ships a checksum file; on its own this doesn't help, since whoever can replace a binary can replace the checksum file next to it |
| `verdict` | the strongest of the above; `checksums only` and `nothing` count as swappable |

Results: one directory per run under [`results/`](results), and one line per
run in [`results/trend.csv`](results/trend.csv), and the latest totals in
[`results/latest.json`](results/latest.json). The set of repositories is
re-queried each month, so it changes as projects cross 1,000 stars or stop
releasing.

The scan runs on the 3rd of each month from
[`.github/workflows/scan.yml`](.github/workflows/scan.yml) and commits its
results here. A full run takes about 950 API calls and a few minutes.
Repositories the token can't read are skipped and listed under `skipped` in
`results.json`.

Run it yourself with a token that can read public repositories (Python 3,
standard library only):

```sh
GITHUB_TOKEN=... python3 scan.py --out /tmp/scan
GITHUB_TOKEN=... python3 scan.py --repos owner/repo another/repo --out /tmp/scan
python3 -m unittest discover -s tests    # offline tests
```

First write-up, with what maintainers can do about it:
[English](https://shenxianpeng.dev/posts/2026/swappable-github-releases/) ·
[中文](https://shenxianpeng.dev/zh-cn/posts/2026/swappable-github-releases/).

## License

The script is under the Apache License 2.0; the data in `results/` is under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Made by
[keelinfra](https://keelinfra.io).
