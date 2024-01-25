# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "teamwork: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iteamwork:/home/jetson/catkin_ws/src/teamwork/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(teamwork_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/jetson/catkin_ws/src/teamwork/msg/KeyData.msg" NAME_WE)
add_custom_target(_teamwork_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "teamwork" "/home/jetson/catkin_ws/src/teamwork/msg/KeyData.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(teamwork
  "/home/jetson/catkin_ws/src/teamwork/msg/KeyData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/teamwork
)

### Generating Services

### Generating Module File
_generate_module_cpp(teamwork
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/teamwork
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(teamwork_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(teamwork_generate_messages teamwork_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jetson/catkin_ws/src/teamwork/msg/KeyData.msg" NAME_WE)
add_dependencies(teamwork_generate_messages_cpp _teamwork_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(teamwork_gencpp)
add_dependencies(teamwork_gencpp teamwork_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS teamwork_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(teamwork
  "/home/jetson/catkin_ws/src/teamwork/msg/KeyData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/teamwork
)

### Generating Services

### Generating Module File
_generate_module_eus(teamwork
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/teamwork
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(teamwork_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(teamwork_generate_messages teamwork_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jetson/catkin_ws/src/teamwork/msg/KeyData.msg" NAME_WE)
add_dependencies(teamwork_generate_messages_eus _teamwork_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(teamwork_geneus)
add_dependencies(teamwork_geneus teamwork_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS teamwork_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(teamwork
  "/home/jetson/catkin_ws/src/teamwork/msg/KeyData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/teamwork
)

### Generating Services

### Generating Module File
_generate_module_lisp(teamwork
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/teamwork
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(teamwork_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(teamwork_generate_messages teamwork_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jetson/catkin_ws/src/teamwork/msg/KeyData.msg" NAME_WE)
add_dependencies(teamwork_generate_messages_lisp _teamwork_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(teamwork_genlisp)
add_dependencies(teamwork_genlisp teamwork_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS teamwork_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(teamwork
  "/home/jetson/catkin_ws/src/teamwork/msg/KeyData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/teamwork
)

### Generating Services

### Generating Module File
_generate_module_nodejs(teamwork
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/teamwork
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(teamwork_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(teamwork_generate_messages teamwork_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jetson/catkin_ws/src/teamwork/msg/KeyData.msg" NAME_WE)
add_dependencies(teamwork_generate_messages_nodejs _teamwork_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(teamwork_gennodejs)
add_dependencies(teamwork_gennodejs teamwork_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS teamwork_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(teamwork
  "/home/jetson/catkin_ws/src/teamwork/msg/KeyData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/teamwork
)

### Generating Services

### Generating Module File
_generate_module_py(teamwork
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/teamwork
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(teamwork_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(teamwork_generate_messages teamwork_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jetson/catkin_ws/src/teamwork/msg/KeyData.msg" NAME_WE)
add_dependencies(teamwork_generate_messages_py _teamwork_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(teamwork_genpy)
add_dependencies(teamwork_genpy teamwork_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS teamwork_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/teamwork)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/teamwork
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(teamwork_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/teamwork)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/teamwork
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(teamwork_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/teamwork)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/teamwork
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(teamwork_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/teamwork)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/teamwork
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(teamwork_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/teamwork)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/teamwork\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/teamwork
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(teamwork_generate_messages_py std_msgs_generate_messages_py)
endif()
