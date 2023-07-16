from conans import ConanFile

class ConanPackage(ConanFile):
    name = "OptiRoute-live-transport-network-monitor"
    version = "0.1.0"

    generators = "cmake_find_package"

    requires = [
    ]