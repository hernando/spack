from spack import *

import shutil

class Surge(CMakePackage):
    """Surge is an open source digital synthesizer"""

    homepage = 'https://surge-synthesizer.github.io/'
    git = 'https://github.com/surge-synthesizer/surge'

    generator='Ninja'
    build_targets = ['Surge-LV2-Packaged']

    version('develop', submodules=True)
    version('1.7.1', tag='release_1.7.1', submodules=True)

    depends_on("cairo +X +ft")
    depends_on("freetype")
    depends_on("fontconfig")
    depends_on("libsndfile")
    depends_on("libxcb")
    depends_on("libxkbcommon")
    depends_on("xcb-util")
    depends_on("xcb-util-cursor")
    depends_on("xcb-util-keysyms")
    depends_on('ninja', type='build')

    patch('release_vars.patch')
    patch('compilation_fixes.patch')

    def setup_build_environment(self, env):
        env.set('SPACK_HASH', self.spec.full_hash(7))
        env.set('SPACK_GIT_BRANCH',
                "main" if str(self.spec.version) == "develop" else "release_" + str(self.spec.version))

    def install(self, spec, prefix):

        lv2_path = prefix.lib + "/lv2/Surge.lv2"
        share_path = prefix.share + "/surge"
        shutil.copytree('resources/data', share_path)
        shutil.copytree(self.build_directory + '/surge_products/Surge.lv2', lv2_path)
