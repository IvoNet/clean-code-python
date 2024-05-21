"""Temporary file that allows pylint to find at least one test."""

import pytest


def test_dummy_normal() -> None:
    """An example of a unit test."""
    assert True


@pytest.mark.integration_test
def test_dummy_integration() -> None:
    """An example of a test marked as an integration test."""
    assert True


@pytest.mark.e2e_test
def test_dummy_e2e() -> None:
    """An example of a test marked as an end-to-end test."""
    assert True
