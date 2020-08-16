from spack import *

class Nonsessionmanager(WafPackage):

    homepage = "https://non.tuxfamily.org/wiki/About"
    git = "git://git.tuxfamily.org/gitroot/non/non.git"

    version('develop')

    depends_on('cairo +X')
    depends_on('ntk')
    depends_on('lo')
    depends_on('jack')

    depends_on('python@3.6:', type='build')

    def configure_args(self):

        return ["--project=session-manager"]
