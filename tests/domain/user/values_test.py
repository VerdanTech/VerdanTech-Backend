# Standard Library
from dataclasses import replace
from datetime import datetime
from typing import ContextManager

# External Libraries
import pytest
from pytest_mock import MockerFixture

# VerdanTech Source
from src.domain.user.exceptions import (
    EmailAlreadyVerifiedError,
    EmailConfirmationExpired,
)
from src.domain.user.values import BaseConfirmation, Email, EmailConfirmation

pytestmark = [pytest.mark.unit]


class TestEmail:
    # ======================================
    # Email.new_confirmation() tests
    # ======================================

    @pytest.mark.parametrize(
        ("already_verified", "key", "expected_error_context"),
        [(False, "abc", None), (True, "abc", EmailAlreadyVerifiedError)],
        indirect=["expected_error_context"],
    )
    def test_new_confirmation(
        self,
        already_verified: bool,
        key: str,
        expected_error_context: ContextManager,
        email: Email,
    ) -> None:
        """
        Ensure an error is thrown if the email
        is already verified.

        Args:
            already_verified (bool): whether the email is verified.
            key (str): the key to create confirmation with.
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py.
            email (Email): email object to test on (pytest fixture).
        """
        if already_verified:
            email = replace(email, verified=True)

        with expected_error_context as error:
            email = email.new_confirmation(key=key)
        if error is None:
            assert email.confirmation.key == key

    # ======================================
    # Email.verify() tests
    # ======================================

    @pytest.mark.parametrize(
        ("already_verified", "expected_error_context"),
        [(False, None), (True, EmailAlreadyVerifiedError)],
        indirect=["expected_error_context"],
    )
    def test_verify(
        self,
        already_verified: bool,
        expected_error_context: ContextManager,
        mocker: MockerFixture,
    ) -> None:
        """
        Ensure the email is returned unchanged except
        verified=True, confirmation=None, and
        verified_at is set to the current time, and
        the appropriate exception is raised if
        already verified.

        Args:
            already_verified: existing email verification state.
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py.
            mocker (MockerFixture): pytest-mock.
        """
        mock_datetime = mocker.patch("src.domain.user.values.datetime")
        mock_datetime.now.return_value = datetime(2023, 1, 1, 1, 1)
        email = Email(
            address="test@test.com",
            verified=already_verified,
            primary=False,
            confirmation=EmailConfirmation(key="abc"),
        )

        expected_output = Email(
            address="test@test.com",
            verified=True,
            primary=False,
            confirmation=None,
            verified_at=datetime(2023, 1, 1, 1, 1),
        )
        with expected_error_context:
            assert email.verify() == expected_output

    # ======================================
    # Email.make_primary() tests
    # ======================================

    def test_make_primary(self) -> None:
        """
        Ensure the email is returned expect True primary status.
        """
        email = Email(address="test@test.com", verified=False, primary=False)
        expected_output = Email(address="test@test.com", verified=False, primary=True)

        assert email.make_primary() == expected_output

    # ======================================
    # Email.make_unprimary() tests
    # ======================================

    def test_make_unprimary(self) -> None:
        """
        Ensure the email is returned expect False primary status.
        """
        email = Email(address="test@test.com", verified=False, primary=True)
        expected_output = Email(address="test@test.com", verified=False, primary=False)

        assert email.make_unprimary() == expected_output

    # ======================================
    # Email.check_confirmation_expired() tests
    # ======================================

    @pytest.mark.parametrize(
        ("is_confirmation_valid", "expected_error_context"),
        [
            # Test case: confirmation is valid, no error raised
            (True, None),
            # Test case: confirmation is not valid, error is raised
            (False, EmailConfirmationExpired),
        ],
        indirect=["expected_error_context"],
    )
    def test_check_confirmation_expired(
        self,
        is_confirmation_valid: bool,
        expected_error_context: ContextManager,
        mocker: MockerFixture,
    ) -> None:
        """
        Ensure an error is raised if the confirmation is not valid.

        Args:
            is_confirmation_valid (bool): mock result of confirmation validation.
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py.
            mocker (MockerFixture): pytest-mock.
        """
        mock_email_confirmation = mocker.MagicMock(spec=EmailConfirmation)
        mock_email_confirmation.is_valid.return_value = is_confirmation_valid
        email = Email(
            address="test@test.com",
            verified=False,
            primary=False,
            confirmation=mock_email_confirmation,
        )

        with expected_error_context:
            email.check_confirmation_expired(expiry_time_hours=0)


class TestBaseConfirmation:
    # ======================================
    # BaseConfirmation.is_valid() tests
    # ======================================

    @pytest.mark.parametrize(
        ("now", "created_at", "expiry_time_hours", "expected_result"),
        [
            # Test case: outside expiry window, false is returned
            (
                datetime(2023, 9, 16, 12, 0, 0),
                datetime(2023, 9, 16, 10, 0, 0),
                1,
                False,
            ),
            # Test case: inside expiry window, true is returned
            (
                datetime(2023, 9, 16, 12, 0, 0),
                datetime(2023, 9, 16, 11, 0, 0),
                2,
                True,
            ),
        ],
    )
    def test_is_valid(
        self,
        now: datetime,
        created_at: datetime,
        expiry_time_hours: int,
        expected_result: bool,
        mocker: MockerFixture,
    ) -> None:
        """
        Ensure the current time is correctly compared.
        against the time of creation and the expiry length.

        Args:
            now (datetime): mock current datetime.
            created_at (datetime): mock creation datetime.
            expiry_time_hours (int): mock application setting.
            expected_result (bool): expected validation result.
            mocker (MockerFixture): pytest-mock.
        """
        mock_datetime = mocker.patch("src.domain.user.values.datetime")
        mock_datetime.now.return_value = now
        confirmation = BaseConfirmation(key="abc", created_at=created_at)

        assert (
            confirmation.is_valid(expiry_time_hours=expiry_time_hours)
            == expected_result
        )
