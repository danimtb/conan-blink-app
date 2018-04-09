CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
PROJECT(HelloApp)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
  include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
  conan_basic_setup()
endif()

if(WIRINGPI)
  add_definitions(-DWIRINGPI)
endif()

message("LIBS: ${CONAN_LIBS}")

ADD_EXECUTABLE(helloapp main.cpp)
target_link_libraries(helloapp ${CONAN_LIBS})
