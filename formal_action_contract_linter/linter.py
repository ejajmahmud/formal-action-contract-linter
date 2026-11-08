"""Core Formal Action Contract Linter implementation."""
import inspect
from typing import Dict, List, Any, Callable, Optional


class LintIssue:
    def __init__(self, rule_id: str, message: str, severity: str = "ERROR"):
        self.rule_id = rule_id
        self.message = message
        self.severity = severity


class FormalActionContractLinter:
    def lint_function(self, func: Callable) -> List[LintIssue]:
        issues = []
        sig = inspect.signature(func)
        doc = inspect.getdoc(func) or ""

        # 1. Check docstring presence
        if len(doc.strip()) < 10:
            issues.append(LintIssue("DOC001", f"Function '{func.__name__}' is missing descriptive docstrings"))

        # 2. Check return type annotation
        if sig.return_annotation == inspect.Signature.empty:
            issues.append(LintIssue("TYPE001", f"Function '{func.__name__}' is missing return type annotation"))

        # 3. Check parameters
        for p_name, param in sig.parameters.items():
            # Type annotation check
            if param.annotation == inspect.Signature.empty:
                issues.append(LintIssue("TYPE002", f"Parameter '{p_name}' in '{func.__name__}' lacks type annotation"))

            # Mutable default check
            if isinstance(param.default, (list, dict, set)):
                issues.append(LintIssue("MUT001", f"Parameter '{p_name}' in '{func.__name__}' uses mutable default object"))

            # Parameter documentation check
            if p_name not in doc and len(sig.parameters) > 0:
                issues.append(LintIssue("DOC002", f"Parameter '{p_name}' not described in docstrings"))

        return issues
