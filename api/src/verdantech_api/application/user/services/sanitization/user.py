import re

from litestar.contrib.repository.abc import AbstractAsyncRepository
from src.verdantech_api.domain.models.user.services.sanitization import (
    UserSanitizer,
    UserSanitizerConfig,
)
from src.verdantech_api.domain.utils.sanitizers import FieldSanitizer
from src.verdantech_api.domain.utils.sanitizers.sanitization.basic.ban import (
    BanSanitization,
    BanSanitizationConfig,
)
from src.verdantech_api.domain.utils.sanitizers.sanitization.basic.length import (
    LengthSanitization,
    LengthSanitizationConfig,
    LengthSanitizationSpec,
)
from src.verdantech_api.domain.utils.sanitizers.sanitization.basic.regex import (
    RegexSanitization,
    RegexSanitizationConfig,
)
from src.verdantech_api.domain.utils.sanitizers.sanitization.repo.unique import (
    UniqueSanitization,
    UniqueSanitizationConfig,
    UniqueSanitizationSpec,
)

from .email import EmailSanitization, EmailSanitizationConfig


def provide_user_sanitizer(user_repo: AbstractAsyncRepository) -> UserSanitizer:
    return UserSanitizer(
        config=UserSanitizerConfig(
            username=FieldSanitizer(
                LengthSanitization(
                    LengthSanitizationConfig(
                        spec=LengthSanitizationSpec(min=0, max=0), error_message=""
                    )
                ),
                RegexSanitization(
                    RegexSanitizationConfig(spec=re.compile, error_message="")
                ),
                BanSanitization(
                    BanSanitizationConfig(
                        spec=[], error_message="", extra={"case_sensitive": False}
                    )
                ),
                UniqueSanitization(
                    UniqueSanitizationConfig(
                        spec=UniqueSanitizationSpec(
                            field_name="username", repo=user_repo
                        ),
                        error_message="",
                    )
                ),
            ),
            email_address=FieldSanitizer(
                LengthSanitization(
                    LengthSanitizationConfig(
                        spec=LengthSanitizationSpec(min=0, max=0), error_message=""
                    )
                ),
                BanSanitization(
                    BanSanitizationConfig(
                        spec=[], error_message="", extra={"case_sensitive": False}
                    )
                ),
                UniqueSanitization(
                    UniqueSanitizationConfig(
                        spec=UniqueSanitizationSpec(
                            field_name="username", repo=user_repo
                        ),
                        error_message="",
                    )
                ),
                EmailSanitization(EmailSanitizationConfig()),
            ),
            password=FieldSanitizer(
                LengthSanitization(
                    LengthSanitizationConfig(
                        spec=LengthSanitizationSpec(min=0, max=0), error_message=""
                    )
                ),
                RegexSanitization(
                    RegexSanitizationConfig(spec=re.compile, error_message="")
                ),
                BanSanitization(
                    BanSanitizationConfig(
                        spec=[], error_message="", extra={"case_sensitive": False}
                    )
                ),
            ),
        )
    )
