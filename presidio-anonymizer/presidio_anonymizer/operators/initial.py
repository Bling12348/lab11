from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    """Convert PII text entity into initials."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """
        Convert text into initials.

        Examples:
        "John Smith" -> "J. S."
        " Eastern Michigan University " -> "E. M. U."
        "@abc" -> "@A."
        """

        if not text:
            return ""

        # Split text into words
        words = text.strip().split()
        initials = []

        for word in words:
            # Find first alphanumeric character
            for ch in word:
                if ch.isalnum():
                    initials.append(f"{ch.upper()}.")
                    break

        return " ".join(initials)

    def validate(self, params: Dict = None) -> None:
        """No parameters required for Initial operator."""
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize
