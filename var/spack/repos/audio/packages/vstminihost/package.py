from spack import *

import inspect
import os

class Vstminihost(Package):

    phases = ['build', 'install']

    homepage = 'https://github.com/ekenberg/vstminihost'
    git = 'https://github.com/ekenberg/vstminihost'

    version('develop')

    depends_on('vst@2.4.2')

    patch('build_fixes.patch')

    def setup_build_environment(self, env):
        env.set('VST_SDK', self.spec['vst'].prefix)

    def build(self, spec, prefix):
        with working_dir(join_path(self.stage.source_path, 'source')):
            inspect.getmodule(self).make()

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('source/vstminihost', prefix.bin)
