import pytest

from db import SessionDI
from services import LinkService


@pytest.fixture()
def link_svc() -> tuple[LinkService, SessionDI]: ...


def test_link_service_get(link_svc: tuple[LinkService, SessionDI]):
    # Arrange
    ...

    # Act
    ...

    # Assert
    ...


def test_link_service_get_returns_none_for_missing_slug(
    link_svc: tuple[LinkService, SessionDI],
) -> None:
    # Arrange
    ...

    # Act
    ...

    # Assert
    ...


def test_link_service_create_persists_new_link(
    link_svc: tuple[LinkService, SessionDI],
) -> None:
    # Arrange
    ...

    # Act
    ...

    # Assert
    ...


def test_link_service_create_raises_for_duplicate_slug(
    link_svc: tuple[LinkService, SessionDI],
) -> None:
    # Arrange
    ...

    # Act / Assert
    ...


def test_link_service_list_links_returns_all_values(
    link_svc: tuple[LinkService, SessionDI],
) -> None:
    # Arrange
    ...

    # Act
    ...

    # Assert
    ...
