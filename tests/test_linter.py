"""Unit tests for formal-action-contract-linter."""
import unittest
from formal_action_contract_linter.linter import FormalActionContractLinter


def dummy_bad(a, b=[]):
    pass


def dummy_good(a: int) -> int:
    """Process number.
    :param a: Input integer
    """
    return a


class TestFormalActionContractLinter(unittest.TestCase):
    def test_lint_bad_function(self):
        linter = FormalActionContractLinter()
        issues = linter.lint_function(dummy_bad)
        rule_ids = [i.rule_id for i in issues]
        self.assertIn("MUT001", rule_ids)
        self.assertIn("TYPE001", rule_ids)

    def test_lint_good_function(self):
        linter = FormalActionContractLinter()
        issues = linter.lint_function(dummy_good)
        self.assertEqual(len(issues), 0)
