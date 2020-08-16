from spack import *


class Ladspa(Package):

    homepage = "https://www.ladspa.org"
    url      = "http://www.ladspa.org/download/ladspa_sdk_1.15.tgz"

    version('1.15', sha256='4229959b09d20c88c8c86f4aa76427843011705df22d9c28b38359fd1829fded')

    def install(self, spec, prefix):
        # Ladspa doesn't have a build system.
        # We have to do our own install here.
        install_tree('src', prefix.include)
