import distro.debian
import distro.archlinux


def identify():
    # Make sure the distro is listed above its parent distro
    tests = [
        distro.debian.identify,
        distro.archlinux.identify
    ]
    for test in tests:
        result = test()
        if result:
            return result
    return False
