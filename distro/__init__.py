import distro.debian
import distro.archlinux
import distro.ubuntu


def identify():
    # Make sure the distro is listed above its parent distro
    tests = [
        distro.ubuntu.identify,
        distro.debian.identify,
        distro.archlinux.identify
    ]
    for test in tests:
        result = test()
        if result:
            return result
    return False
