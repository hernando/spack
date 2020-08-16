import inspect
import os
import shutil

from spack import *

class MrubyZest(Package):

    phases = ['setup', 'build', 'install']

    homepage = "http://log.fundamental-code.com/2018/06/16/mruby-zest.html"
    git = "https://github.com/mruby-zest/mruby-zest-build"

    depends_on('bison', type='build')
    depends_on('ruby', type=('build', 'run'))

    version("develop", submodules=True)

    def setup_build_environment(self, env):
        env.set('BUILD_MODE', 'release')

    def setup(self, spec, prefix):
        inspect.getmodule(self).ruby('rebuild-fcache.rb')
        inspect.getmodule(self).gem('install', 'rake')
        inspect.getmodule(self).make('setup')

    def build(self, spec, prefix):
        inspect.getmodule(self).make('builddep')
        inspect.getmodule(self).make()

    def install(self, spec, prefix):
        inspect.getmodule(self).make('pack')
        for f in os.listdir('package'):
            shutil.move('package/' + f, prefix)
