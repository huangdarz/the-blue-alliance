import pytest
from _pytest.monkeypatch import MonkeyPatch

from backend.common.environment import Environment


@pytest.fixture
def set_dev(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("GAE_ENV", "localdev")


@pytest.fixture
def set_prod(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("GAE_ENV", "standard")


@pytest.fixture
def set_project(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("GOOGLE_CLOUD_PROJECT", "tbatv-prod-hrd")


@pytest.fixture
def set_service(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("GAE_SERVICE", "default")


def test_dev_env(set_dev) -> None:
    assert Environment.is_dev() is True
    assert Environment.is_prod() is False


def test_prod_env(set_prod) -> None:
    assert Environment.is_dev() is False
    assert Environment.is_prod() is True


def test_project_none() -> None:
    assert Environment.project() is None


def test_project(set_project) -> None:
    assert Environment.project() == "tbatv-prod-hrd"


def test_service_none() -> None:
    assert Environment.service() is None


def test_service(set_service) -> None:
    assert Environment.service() == "default"


def test_other_env(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("GAE_ENV", "something")
    assert Environment.is_dev() is False
    assert Environment.is_prod() is False
