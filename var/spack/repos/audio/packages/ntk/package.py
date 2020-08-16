from spack import *

class Ntk(WafPackage):

    homepage = "https://non.tuxfamily.org/wiki/NTK"
    git = "git://git.tuxfamily.org/gitroot/non/fltk.git"

    version('develop', commit='dae177189b12f74ea01ac2389b76326c06d9be78')

    depends_on('cairo +X')
    depends_on('fontconfig')
    depends_on('libxft')
