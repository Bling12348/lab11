from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    """Convert PII text entity into initials, preserving leading symbols."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """
        Convert text into initials while preserving leading non-alphanumeric characters.

        Examples:
        "John Smith" -> "J. S."
        "     Eastern    Michigan   University " -> "E. M. U."
        "@abc" -> "@A."
        "@843A" -> "@8."
        "--**abc" -> "--**A."
        """

        if not text:
            return ""

        words = text.strip().split()
        initials = []

        for word in words:
            prefix = ""
            initial_found = False
            for ch in word:
                if not initial_found and ch.isalnum():
                    # First alphanumeric character becomes uppercase initial
                    initials.append(f"{prefix}{ch.upper()}.")
                    initial_found = True
                    break
                elif not initial_found:
                    # Preserve leading non-alphanumeric characters
                    prefix += ch
            if not initial_found:
                # If no alphanumeric character, just append the word as is
                initials.append(word)

        return " ".join(initials)

    def validate(self, params: Dict = None) -> None:
        """No parameters required for Initial operator."""
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize