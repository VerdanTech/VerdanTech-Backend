# VerdanTech Source
from src.domain.garden.enums import RoleEnum
from src.ops.common import schema


@schema
class GardenInviteCreateInput:
    """
    Garden invitation DTO.

    Fields:
        garden_key (str): the key id of the garden to create the membership invitation to.
        user_username (str): the username of the user to invite.
        role (RoleEnum): the role to set on the membership.
    """

    garden_key: str
    user_username: str
    role: RoleEnum


@schema
class GardenRevokeMembershipInput:
    """
    Garden membership removal DTO.

    Fields:
        garden_key (str): the key id of the garden to change the membership on.
        user_username (str): the username of the user with the membership to remove.
    """

    garden_key: str
    user_username: str


@schema
class GardenRoleChangeInput:
    """
    Garden membership role change DTO.

    Fields:
        garden_key (str): the key id of the garden to change the membership on.
        user_username (str): the username of the user with the membership.
        role (RoleEnum): the role to set on the membership.
    """

    garden_key: str
    user_username: str
    role: RoleEnum
