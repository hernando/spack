from spack import *

"""Packag for user space alsa libraries"""
class Alsa(AutotoolsPackage):

    homepage = "https://alsa-project.org/wiki/Main_Page"
    url = "ftp://ftp.alsa-project.org/pub/lib/alsa-lib-1.2.2.tar.bz2"

    version('1.2.2', sha256='d8e853d8805574777bbe40937812ad1419c9ea7210e176f0def3e6ed255ab3ec')
