from spack import *

class Lilv(WafPackage):

    homepage = "https://drobilla.net/software/lilv"
    url = "http://download.drobilla.net/lilv-0.24.8.tar.bz2"

    depends_on('lv2@1.16.0:')
    depends_on('serd@0.30.0:')
    depends_on('sord@0.14.0:')
    depends_on('sratom@0.4.0:')

    version('0.24.8', sha256='cadc3654c481aec6a6db504439cf8c0572c06128a6fbca1953a30df77e89c300')

