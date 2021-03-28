from spack import *


class Raptor(AutotoolsPackage):

    homepage = "https://www.example.com"
    url      = "http://download.librdf.org/source/raptor2-2.0.15.tar.gz"

    version('2.0.15', sha256='ada7f0ba54787b33485d090d3d2680533520cd4426d2f7fb4782dd4a6a1480ed')

    depends_on("libxml2")
