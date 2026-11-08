"""CLI for formal-action-contract-linter."""
import sys
import argparse
from .linter import FormalActionContractLinter


def bad_tool(query, opts={}):
    return query


def good_tool(query: str, timeout: int = 10) -> str:
    """Run an authorized query against the safe backend.

    :param query: SQL string
    :param timeout: Execution timeout in seconds
    """
    return query


def main():
    parser = argparse.ArgumentParser(description="Formal Action Contract Linter CLI")
    parser.add_argument("--demo", action="store_true", help="Run contract linter demo")
    args = parser.parse_args()

    if args.demo:
        linter = FormalActionContractLinter()
        print("[*] Linting bad_tool:")
        for issue in linter.lint_function(bad_tool):
            print(f"    [{issue.severity}] {issue.rule_id}: {issue.message}")

        print("[+] Linting good_tool:")
        issues = linter.lint_function(good_tool)
        print(f"    Issues detected: {len(issues)} (Passed cleanly!)")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
