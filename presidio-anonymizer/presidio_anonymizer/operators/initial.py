"""Replaces the PII text entity with empty string."""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Initialize the string - empty value."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        # Minimal placeholder implementation
        return ""

    def validate(self, params: Dict = None) -> None:
        # No validation needed for now
        pass

    def operator_name(self) -> str:
        # This must be the NAME you want to register in the factory
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize