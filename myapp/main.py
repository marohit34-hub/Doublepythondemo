# myapp/main.py
"""Simple app module with a small function and CLI."""

from __future__ import annotations
import argparse
import sys

def add(a: int, b: int) -> int:
    """Return sum of two integers."""
    return a + b

def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint, returns 0 on success."""
    parser = argparse.ArgumentParser(prog="myapp")
    parser.add_argument("a", type=int, help="first integer")
    parser.add_argument("b", type=int, help="second integer")
    args = parser.parse_args(argv)
    result = add(args.a, args.b)
    print(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
