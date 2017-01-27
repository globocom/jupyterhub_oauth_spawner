from jupyterhub.spawner import LocalProcessSpawner
from traitlets import Any
from tornado import gen


class OAuthSpawner(LocalProcessSpawner):
    """Local spawner that runs single-user servers as the same user as the Hub itself.

    Overrides user-specific env setup with no-ops.
    """

    pre_start_hook = Any(None, config=True,
        help="""Python callable or importstring thereof
        to be called before the start of jupyter notebook.
        """
    )

    post_start_hook = Any(None, config=True,
        help="""Python callable or importstring thereof
        to be called after the start of jupyter notebook.
        """
    )

    pre_stop_hook = Any(None, config=True,
        help="""Python callable or importstring thereof
        to be called before the stop of jupyter notebook.
        """
    )

    post_stop_hook = Any(None, config=True,
        help="""Python callable or importstring thereof
        to be called after the stop of jupyter notebook.
        """
    )

    def make_preexec_fn(self, name):
        """no-op to avoid setuid"""
        return None

    def user_env(self, env):
        """no-op to avoid setting HOME dir, etc."""
        env["USER"] = self.user.name
        return env

    @gen.coroutine
    def start(self):
        if self.pre_start_hook:
            self.pre_start_hook(self.user, "Pre Start")
        super(OAuthSpawner, self).start()
        if self.post_start_hook:
            self.post_start_hook(self.user, "Post Start")

    @gen.coroutine
    def stop(self, now=False):
        if self.pre_stop_hook:
            self.pre_stop_hook(self.user, "Pre Stop")
        super(OAuthSpawner, self).stop(now)
        if self.post_stop_hook:
            self.post_stop_hook(self.user, "Post Stop")
