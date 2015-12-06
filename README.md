# distro

A python module to get information about the current Linux distribution.

## Usage

```python
import distro
d = distro.identify()
d.name           # debian
d.pretty_name    # Debian GNU/Linux 7 (wheezy)
d.codename       # wheezy
d.version_number # 7
```