from spack import *

class Qsynth(CMakePackage):

    homepage = "https://qsynth.sourceforge.io/"
    url = "https://download.sourceforge.net/qsynth/qsynth-0.6.3.tar.gz"

    generator='Ninja'

    version('0.6.3', sha256="1b5733d35b4b24679d59812cf9a5f3152ac0c78046ba1db71870cb7effad3876")

    depends_on('ninja', type='build')

    depends_on("fluidsynth")
    depends_on("qt@5.12: +dbus +opengl")

