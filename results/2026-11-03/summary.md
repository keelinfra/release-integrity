# Release integrity scan, 2026-11-03

242 most-starred Go/Rust CLI repos (topic `cli`, >=1000 stars) whose latest
release is under a year old and ships binaries. Latest release only.

| Verdict (best protection found) | Repos | Share |
|---|---|---|
| immutable | 26 | 11% |
| provenance | 19 | 8% |
| signed | 20 | 8% |
| checksums only | 111 | 46% |
| nothing | 66 | 27% |

**Swappable with no verifiable trace (checksums only or nothing): 177/242 (73%).**

Immutable on: 26; build provenance: 31; signatures: 32; checksum files: 157.

Top 20 by stars:

| Repo | Stars | Tag | Immutable | Provenance | Signed | Checksums |
|---|---|---|---|---|---|---|
| rtk-ai/rtk | 85416 | v1.1.0 | - | - | - | yes |
| junegunn/fzf | 83971 | v0.74.5 | - | - | - | yes |
| jesseduffield/lazygit | 83626 | v0.66.2 | - | - | - | yes |
| BurntSushi/ripgrep | 69665 | 15.2.0 | - | - | - | yes |
| tw93/Pake | 62779 | V3.17.6 | - | - | - | - |
| sharkdp/bat | 61038 | v0.26.1 | - | - | - | - |
| herdrdev/herdr | 47755 | v0.9.5 | yes | - | - | - |
| cli/cli | 46853 | v2.103.3 | yes | yes | - | yes |
| sharkdp/fd | 44932 | v10.5.0 | - | yes | - | - |
| sxyazi/yazi | 43204 | v26.9.1 | - | - | - | - |
| codewhale-hq/Codewhale | 41163 | v0.10.2 | - | - | - | yes |
| ajeetdsouza/zoxide | 40433 | v0.10.0 | - | - | - | - |
| esengine/DeepSeek-Reasonix | 36053 | studio-v2.57.0 | - | - | yes | yes |
| googleworkspace/cli | 32079 | v0.22.5 | yes | yes | - | yes |
| gitleaks/gitleaks | 30622 | v8.30.1 | - | - | - | yes |
| sharkdp/hyperfine | 29202 | v2.0.0 | - | - | - | - |
| t8y2/dbx | 28902 | v0.6.65 | - | - | yes | yes |
| charmbracelet/glow | 27898 | v3.0.0 | - | - | yes | yes |
| asdf-vm/asdf | 25611 | v0.20.2 | - | - | - | yes |
| yorukot/superfile | 24003 | v1.6.0 | - | - | - | yes |

Skipped candidates: {'latest release too old': 79, 'no binary assets': 21, 'no release': 11, 'error HTTP Error 403: Forbidden': 1}

