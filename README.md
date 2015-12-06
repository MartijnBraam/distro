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
```