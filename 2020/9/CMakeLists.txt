project(nine)

add_executable(${PROJECT_NAME} main.cpp)

target_include_directories(${PROJECT_NAME} PUBLIC ".")
target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_17)
