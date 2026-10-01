"""Test module."""

from pyrig_private_overrides.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile,
)


class TestRepositorySettingsConfigFile:
    """Test repository settings overrides."""

    def test_visibility(self) -> None:
        """Keep the generated pyrig-private repository public."""
        assert RepositorySettingsConfigFile.I.visibility() == "public"

    def test_generated_settings_preserve_public_policies(self) -> None:
        """Test method."""
        settings = RepositorySettingsConfigFile.configs()

        assert settings["repository"]["visibility"] == "public"
        assert settings["fork_pr_contributor_approval"] == {
            "approval_policy": "all_external_contributors",
        }
        assert {ruleset["target"] for ruleset in settings["rulesets"]} == {
            "branch",
            "tag",
        }
