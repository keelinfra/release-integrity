"""Offline checks for how scan.py classifies release assets and picks a verdict."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import scan  # noqa: E402


class Kind(unittest.TestCase):
    def test_names(self):
        cases = {
            "fzf-0.74.5-linux_amd64.tar.gz": "binary",
            "bat_0.26.1_amd64.deb": "binary",
            "tool_windows_arm64.exe": "binary",
            "fzf_0.74.5_checksums.txt": "checksum",
            "SHA256SUMS": "checksum",
            "ripgrep-15.2.0-x86_64-unknown-linux-musl.tar.gz.sha256": "checksum",
            "tool_1.0.0_SHA512SUMS": "checksum",
            "checksums.txt.sig": "signature",
            "SHA256SUMS.asc": "signature",
            "checksums.txt.pem": "signature",
            "tool.tar.gz.minisig": "signature",
            "tool.tar.gz.sigstore.json": "signature",
            "multiple.intoto.jsonl": "signature",
            "sbom.spdx.json": "metadata",
            "install.sh": "metadata",
            "cosign.pub": "metadata",
        }
        for name, want in cases.items():
            with self.subTest(name=name):
                self.assertEqual(scan.kind(name), want)


class Verdict(unittest.TestCase):
    base = {"immutable": False, "provenance": False, "signed": False, "checksums": False}

    def test_order(self):
        def v(**on):
            return scan.verdict({**self.base, **on})

        self.assertEqual(v(), "nothing")
        self.assertEqual(v(checksums=True), "checksums only")
        self.assertEqual(v(checksums=True, signed=True), "signed")
        self.assertEqual(v(signed=True, provenance=True), "provenance")
        self.assertEqual(v(provenance=True, immutable=True), "immutable")


class Trend(unittest.TestCase):
    def test_trend_and_latest(self):
        import json
        import tempfile

        rows = [{"verdict": v} for v in ["immutable", "checksums only", "nothing", "nothing"]]
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "trend.csv")
            scan.append_trend(path, rows, 10)
            scan.append_trend(path, rows, 10)
            with open(path) as f:
                lines = f.read().splitlines()
            self.assertEqual(len(lines), 3)  # header + two runs
            self.assertTrue(lines[1].endswith(",10,4,1,0,0,1,2,3"))
            with open(os.path.join(d, "latest.json")) as f:
                latest = json.load(f)
            self.assertEqual(latest["swappable"], 3)
            self.assertEqual(latest["swappable_share"], "75% of 4")


if __name__ == "__main__":
    unittest.main()
