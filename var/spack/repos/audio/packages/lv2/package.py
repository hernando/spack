from spack import *

class Lv2(WafPackage):

    homepage = "https://gitlab.com/lv2/lv2"
    git = "https://gitlab.com/lv2/lv2.git"

    version('1.18.0', tag='v1.18.0', submodules=True)
    version('1.16.0', tag='v1.16.0', submodules=True)

