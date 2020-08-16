from spack import *

class Suil(WafPackage):

    homepage = "https://drobilla.net/software/suil"
    url = "http://download.drobilla.net/suil-0.10.6.tar.bz2"

    depends_on('lv2@1.16.0:')
    depends_on('gtkplus')

    version('0.10.6', sha256='06fc70abaa33bd7089dd1051af46f89d378e8465d170347a3190132e6f009b7c')

