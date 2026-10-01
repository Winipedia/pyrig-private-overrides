"""Repository-level settings and protection ruleset configuration for GitHub."""

from pyrig_private.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile as PrivateRepositorySettingsConfigFile,
)
from pyrig_public.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile as PublicRepositorySettingsConfigFile,
)


class RepositorySettingsConfigFile(
    PrivateRepositorySettingsConfigFile,
    PublicRepositorySettingsConfigFile,
):
    """GitHub settings that keep the pyrig-private project repository public.

    Combine the project's repository settings with public requirements.
    """

    def visibility(self) -> str:
        """Return the public visibility required by this plugin.

        ``pyrig-private`` is itself an open-source project and dogfoods this
        override package, so its generated repository must remain public.

        Returns:
            The repository visibility value, ``"public"``.
        """
        return PublicRepositorySettingsConfigFile().visibility()
