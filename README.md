# JupyterHub OAuth Spawner

Spawner for OAuth authentication users. This Spawner uses same Jupyterhub user for OS operations, but you can control OAuth Users.

## Install

```

pip install jupyterhub_oauth_spawner

```

In your jupyterhub config file:

```

from jupyterhub_oauth_spawner.oauth_spawner import OAuthSpawner

c.JupyterHub.spawner_class = OAuthSpawner

c.OAuthSpawner.pre_start_hook = your_function
c.OAuthSpawner.pre_stop_hook = your_function
c.OAuthSpawner.post_start_hook = your_function
c.OAuthSpawner.post_stop_hook = your_function
```

**your_function** should expect and **user_object** with attributes **name** for user login and **hook_name** with hook called.

So in your function:


```

your_function(user, hook_name):
    send_info(user.name, hook_name)

```
