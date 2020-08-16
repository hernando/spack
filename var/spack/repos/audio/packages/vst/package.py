from spack import *
import shutil
import os

class Vst(Package):

    homepage = "https://www.steinberg.net/en/company/developers.html"

    version('3.7.0', sha256='d926742480b62d246b18972ff6d61f9b1b894b91e1a33e00f98a8627a61775ba', extension='zip')
    version('2.4.2', sha256='795c81c998d71203367ef11f5101f5b8c71384f453bc1258720a402e8a4b9734', extension='zip')

    def install(self, spec, prefix):
        if self.spec.version < Version('3'):
            shutil.copytree(os.getcwd() + "/pluginterfaces", prefix + "/pluginterfaces")
        else:
            shutil.copytree(os.getcwd() + "/VST3_SDK", prefix + "/VST3_SDK")

    def url_for_version(self, version):
        if self.spec.version < Version('3'):
            return "https://archive.org/download/VST2SDK/vst_sdk2_4_rev2.zip"
        else:
            return "https://www.steinberg.net/vst3sdk"
