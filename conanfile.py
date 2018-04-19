from conans import ConanFile, CMake


class BlinkAppConan(ConanFile):
    name = "BlinkApp"
    version = "0.1"
    license = "MIT"
    description = "Blink application"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/danimtb/conan-blink-app.git"
    exports_sources = "CMakeLists.txt", "main.cpp", "LICENSE"
    generators = "cmake"


    def build(self):
        cmake = CMake(self)
        if self.settings.arch == "armv7":
            cmake.definitions["WIRINGPI"] = True
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("blinkapp", src="bin", dst="bin")

    def requirements(self):
        if self.settings.arch == "armv7":
            self.requires("wiringpi/2.46@conan/stable")

    def deploy(self):
        self.copy("blinkapp", src="bin", dst="bin")
