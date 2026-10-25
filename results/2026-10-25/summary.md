# Release integrity scan, 2026-10-25

241 most-starred Go/Rust CLI repos (topic `cli`, >=1000 stars) whose latest
release is under a year old and ships binaries. Latest release only.

| Verdict (best protection found) | Repos | Share |
|---|---|---|
| immutable | 25 | 10% |
| provenance | 19 | 8% |
| signed | 19 | 8% |
| checksums only | 111 | 46% |
| nothing | 67 | 28% |

**Swappable with no verifiable trace (checksums only or nothing): 178/241 (74%).**

Immutable on: 25; build provenance: 31; signatures: 30; checksum files: 156.

Top 20 by stars:

| Repo | Stars | Tag | Immutable | Provenance | Signed | Checksums |
|---|---|---|---|---|---|---|
| rtk-ai/rtk | 84499 | v1.0.1 | - | - | - | yes |
| junegunn/fzf | 83773 | v0.74.5 | - | - | - | yes |
| jesseduffield/lazygit | 83405 | v0.66.2 | - | - | - | yes |
| BurntSushi/ripgrep | 69417 | 15.2.0 | - | - | - | yes |
| tw93/Pake | 62301 | V3.17.6 | - | - | - | - |
| sharkdp/bat | 60923 | v0.26.1 | - | - | - | - |
| cli/cli | 46735 | v2.103.2 | yes | yes | - | yes |
| herdrdev/herdr | 45739 | v0.9.5 | yes | - | - | - |
| sharkdp/fd | 44858 | v10.5.0 | - | yes | - | - |
| sxyazi/yazi | 43008 | v26.9.1 | - | - | - | - |
| codewhale-hq/Codewhale | 41113 | v0.10.2 | - | - | - | yes |
| ajeetdsouza/zoxide | 40280 | v0.10.0 | - | - | - | - |
| esengine/DeepSeek-Reasonix | 35957 | studio-v2.51.0 | - | - | yes | yes |
| googleworkspace/cli | 31862 | v0.22.5 | yes | yes | - | yes |
| gitleaks/gitleaks | 30311 | v8.30.1 | - | - | - | yes |
| sharkdp/hyperfine | 29151 | v2.0.0 | - | - | - | - |
| charmbracelet/glow | 27796 | v3.0.0 | - | - | yes | yes |
| t8y2/dbx | 27700 | v0.6.54 | - | - | yes | yes |
| asdf-vm/asdf | 25610 | v0.20.2 | - | - | - | yes |
| yorukot/superfile | 23916 | v1.6.0 | - | - | - | yes |

Skipped candidates: {'latest': 78, 'no binary assets': 22, 'no release': 11, 'error HTTP Error 403: Forbidden': 1}

