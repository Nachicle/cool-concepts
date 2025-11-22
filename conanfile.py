from conan import ConanFile
from conan.tools.layout import basic_layout
from conan.tools.files import copy

class CoolConceptsRecipe(ConanFile):
    name = "cool-concepts"
    version = "0.0.1"

    description = "Cool and modern C++ concepts"
    license = "MIT"
    author = "Nachicle (ping@nachicle.dev)"
    topics = ("cool", "concepts")
    url = "https://github.com/Nachicle/cool-concepts.git"

    exports_sources = "include/*"

    package_type = "header-library"

    implements = ["auto_header_only"]

    def layout(self):
        basic_layout(self)
    
    def package(self):
        copy(self, "include/*", self.source_folder, self.package_folder)

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.set_property("cmake_target_name", "cool::concepts")
