from spack import *

import shutil

class Zynaddsubfx(CMakePackage):

    homepage = "https://zynaddsubfx.sourceforge.io/"
    git = "https://github.com/zynaddsubfx/zynaddsubfx"

    version("develop", submodules=True)

    depends_on('fftw +openmp ~mpi')
    depends_on("jack")
    depends_on("libxpm")
    depends_on("lo@0.28:")
    depends_on("mruby-zest")
    depends_on("mxml")
    depends_on("ntk")
    depends_on("zlib")

    def cmake_args(self):
        src = self.spec['mruby-zest'].prefix
        dst = self.prefix
        print(src, dst)

        return ["-DGuiModule=zest", "-DDemoMode=release", "-DZYN_DATADIR=" + self.prefix + "/share/zynaddsubfx"]

    @run_after('install')
    def copy_zest_artifacts(self):
        src = self.spec['mruby-zest'].prefix
        dst = self.prefix
        print(src, dst)
        shutil.copy(src + '/libzest.so', dst + '/lib')
        shutil.copy(src + '/zest', dst + '/bin/zyn-fusion')
        shutil.copytree(src + '/qml', dst + '/lib/qml')
        shutil.copytree(src + '/schema', dst + '/lib/schema')
        shutil.copytree(src + '/font', dst + '/lib/font')
