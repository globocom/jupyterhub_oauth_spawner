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

c.OAuthSpawner.pre_start_hook = your_function(user_object)
c.OAuthSpawner.pre_stop_hook = your_function(user_object)
c.OAuthSpawner.post_start_hook = your_function(user_object)
c.OAuthSpawner.post_stop_hook = your_function(user_object)
```

**user_object** has attribute **name** for user login, so in your function:


```

your_function(user):
    send_info(user.name)

```
