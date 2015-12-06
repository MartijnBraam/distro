# distro

A python module to get information about the current Linux distribution.

## Usage

```python
import distro
d = distro.identify()
d.name            # debian
d.name_pretty     # Debian GNU/Linux
d.codename        # wheezy
d.codename_pretty # Wheezy
d.version_number  # 7
d.parent          # None
```

## Output for various distros

Distro        | name    | name_pretty      | codename | codename_pretty | parent
------------- | --------|------------------|----------|-----------------|--------
Debian        | debian  | Debian GNU/Linux | wheezy   | Wheezy          | None
Raspbian      | raspbian| Raspbian GNU/Linux| wheezy   | wheezy          | &lt;LinuxDistro debian 7&gt;
Arch Linux    | arch    | Arch Linux       |          |                 | None
