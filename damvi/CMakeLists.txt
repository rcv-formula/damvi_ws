cmake_minimum_required(VERSION 3.8)
project(damvi)

# ament_cmake를 찾습니다.
find_package(ament_cmake REQUIRED)

# 런치 파일 디렉토리를 설치합니다.
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()