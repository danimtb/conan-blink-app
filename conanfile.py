from conans import ConanFile, CMake


class HelloAppConan(ConanFile):
    name = "HelloApp"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/danimtb/conan-hello-app.git"
    exports_sources = "CMakeLists.txt", "main.cpp", "LICENSE"
    generators = "cmake"


    def build(self):
        cmake = CMake(self)
        if self.settings.arch == "armv7":
            cmake.definitions["WIRINGPI"] = True
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*helloapp*", src="bin", dst="bin")

    def requirements(self):
        if self.settings.arch == "armv7":
            self.requirements.add("wiringpi/2.46@danimtb/testing")

    def deploy(self):
        self.copy("*helloapp*", src="bin", dst="bin")
