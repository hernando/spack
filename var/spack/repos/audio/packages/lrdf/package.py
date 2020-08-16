from spack import *

import inspect

class Lrdf(AutotoolsPackage):

    homepage = "https://github.com/swh/LRDF"
    git = "https://github.com/swh/lrdf.git"

    version('0.6.1', tag="v0.6.1")
    version('0.6.0', tag="v0.6.0")
    version('0.5.0', tag="0.5.0")
    version('0.4.0', tag="0.4.0")

    depends_on('raptor@:2')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')

    force_autoreconf = True


    def autoreconf(self, spec, prefix):

        with working_dir(self.configure_directory):
            m = inspect.getmodule(self)
            m.libtoolize()
            m.aclocal()
            m.autoheader()
            m.automake('--add-missing', '--foreign')
            m.autoconf()
