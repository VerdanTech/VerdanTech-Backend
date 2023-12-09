# Standard Library
import asyncio
from typing import Dict, Generic, List, Tuple

from . import spec
from .options import GroupErrorsByEnum, SelectEnum


class FieldSanitizer(Generic[*spec.SpecsT]):
    """
    Encapsulate multiple Specs.
    """

    def __init__(self, *specs: List[spec.Spec]):
        for spec in specs:
            spec.field = self
        self.specs = specs
        self.normalized_data = None

    async def sanitize(
        self,
        input_data: spec.GenericInputType,
        spec_select: List[SelectEnum],
        apply_default: bool = False,
        group_errors_by: GroupErrorsByEnum = GroupErrorsByEnum.FIELD,
    ) -> Tuple[spec.GenericInputType, Dict[str, str]]:
        """
        Call the _sanitization function, and raise error if any failure.

        Args:
            input (GenericInputType): the input to sanitize.
            spec_select (List[SelectEnum]):
                list of values of SelectEnum, which allows filtering
                the list of Specs registered on each field.
            group_errors_by (GroupErrorsOptionsEnum): see GroupErrorsOptionsEnum
                for behavior description.
            apply_default (bool) True applies all specifications
                registered on a FieldSanitizer by default. The selections in
                spec_select disable Specs from being applied.
                False applies no specifcations registered on a FieldSanitizer
                by default. The selections in spec_select enable
                Specs from being applied. Defaults to False.

        Raises:
            SpecError: raised if sanitization fails and group_errors_by
                is FIELD or SPEC.

        Returns:
            Tuple[GenericInputType, Dict[str, str]]: GenericInputType is the
                sanitized output data. Dict[str, str] is the error message, where
                the keys are names of Sanitizations, and the values are the error messages.
        """
        # Set default normalized value
        self.normalized_data = input_data

        # Group exceptions
        error = await self._sanitize(
            input_data=input_data,
            spec_select=spec_select,
            apply_default=apply_default,
        )

        # Raise errors if enabled.
        if error and (
            group_errors_by == GroupErrorsByEnum.FIELD
            or group_errors_by == GroupErrorsByEnum.SPEC
        ):
            raise spec.SpecError(error)

        return self.normalized_data, error

    async def _sanitize(
        self,
        input_data: spec.GenericInputType,
        spec_select: List[SelectEnum],
        apply_default: bool = False,
        group_errors_by: GroupErrorsByEnum = GroupErrorsByEnum.FIELD,
    ) -> Dict[str, str]:
        """
        Sanitizes the input against Sanitizations.

        Args:
            input_data (GenericInputType): see sanitize() method.
            spec_select (List[SelectEnum]): see sanitize() method.
            group_errors_by (GroupErrorsOptionsEnum): see sanitize() method.
            apply_default (bool): see sanitize() method.

        Returns:
            Dict[str, str]: Dict containing errors.
        """

        # Group exceptions
        error = {}

        # For every enabled Spec, run the sanitization logic.
        for spec in self._select_specs(
            spec_select=spec_select,
            apply_default=apply_default,
        ):
            spec_error = await spec.sanitize(
                input_data=input_data, group_errors_by=group_errors_by
            )

            # Update the output error
            if spec_error:
                error[spec.name] = spec_error

        return error

    def _select_specs(
        self,
        spec_select: List[SelectEnum],
        apply_default: bool = False,
    ) -> List[spec.Spec]:
        """
        Returns a Spec for every Spec class
        that is selected based on the arguments.

        Args:
            spec_select (List[SelectEnum]): see sanitize() method.
            apply_default (bool): see sanitize() method.

        Returns:
            List[Spec]: a list of enabled Specs.
        """
        # A DISABLE_ALL selection results in no specs.
        if SelectEnum.DISABLE_ALL in spec_select:
            return []

        # An ENABLE_ALL selection results in all specs.
        if SelectEnum.ENABLE_ALL in spec_select:
            return self.specs

        # A False is results in all specs
        # with IDs that aren't selected within spec_select
        if apply_default is True:
            return [spec for spec in self.specs if spec.id not in spec_select]

        # A False is results in all specs
        # with IDs that are selected within spec_select
        else:
            return [spec for spec in self.specs if spec.id in spec_select]

    def normalized(self) -> spec.GenericInputType:
        """Supply last input to a normalized form

        Args:
            input (GenericInputType): The input to normalize

        Returns:
            GenericInputType: The normalized input
        """
        return self.normalized_data or None


class MockFieldSanitizer(FieldSanitizer):
    """Mock sanitizer class for testing"""

    field_name: str = "generic_field"

    def sanitize(self, input: spec.GenericInputType) -> bool:
        return True

    def normalized(self) -> spec.GenericInputType:
        return input