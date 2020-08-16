from spack import *
from spack import compilers

import inspect
import os
import shutil

class Yabridge(MesonPackage):

    homepage = "https://github.com/robbert-vdh/yabridge"
    git = "https://github.com/robbert-vdh/yabridge.git"

    version('1.6.0', tag='1.6.0')
    version('1.5.0', tag='1.5.0')

    depends_on('wine', type=('build', 'run'))
    depends_on('boost @1.66.0:')
    depends_on('libxcb')

    depends_on('meson @0.55.0', type='build')
    depends_on('ninja', type='build')

    def setup_build_environment(self, env):
        env.set('BOOST_ROOT', self.spec['boost'].prefix)

    def meson_args(self):
        return ['--cross-file', 'cross-wine.conf']

    def meson(self, spec, prefix):
        print(os.path.abspath(self.root_mesonlists_dir))
        with working_dir(os.path.abspath(self.root_mesonlists_dir)):
            options = ['setup']
            options += self.std_meson_args
            options += self.meson_args()
            options += [self.build_directory]
            print(options)
            inspect.getmodule(self).meson(*options)

    def install(self, spec, prefix):
        with working_dir(self.build_directory):

            os.mkdir(prefix + '/bin')
            for f in ['yabridge-host.exe', 'yabridge-group.exe',
                      'yabridge-host.exe.so', 'yabridge-group.exe.so', 'libyabridge.so']:
                shutil.copyfile(f, prefix + '/bin/' + f)

