from spack import *

class Sratom(WafPackage):

    homepage = "https://drobilla.net/software/sratom"
    url = "http://download.drobilla.net/sratom-0.6.4.tar.bz2"

    depends_on('lv2@1.16.0:')
    depends_on('serd@0.30.0:')
    depends_on('sord@0.14.0:')

    version('0.6.4', sha256='146c8f14b8902ac3c8fa8c2e0a014eb8a38fab60090c5adbfbff3e3b7c5c006e')

