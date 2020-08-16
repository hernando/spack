from spack import *

class Lo(AutotoolsPackage):

    homepage = "http://liblo.sourceforge.net/"
    url = "http://downloads.sourceforge.net/liblo/liblo-0.31.tar.gz"

    version("0.31", sha256="2b4f446e1220dcd624ecd8405248b08b7601e9a0d87a0b94730c2907dbccc750")
