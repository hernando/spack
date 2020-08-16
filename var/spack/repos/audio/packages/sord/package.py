from spack import *

class Sord(WafPackage):

    homepage = "https://drobilla.net/software/sord"
    url = "http://download.drobilla.net/sord-0.16.4.tar.bz2"

    depends_on('serd@0.30.0:')

    version('0.16.4', sha256='b15998f4e7ad958201346009477d6696e90ee5d3e9aff25e7e9be074372690d7')

