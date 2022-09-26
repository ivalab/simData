cmake_minimum_required(VERSION 3.0.2)
project(warehouse)

find_package(catkin REQUIRED COMPONENTS gazebo_ros)
catkin_package(DEPENDS gazebo_ros)

# create the appropriate files for tools
set(BUILD_MODEL_DIR ${PROJECT_SOURCE_DIR}/models)

file(GLOB SUBDIRS ${PROJECT_SOURCE_DIR}/3Dwarehouse/tools/*)
foreach(SUBDIR ${SUBDIRS})
    get_filename_component(MODEL_NAME ${SUBDIR} NAME)
    set(MODEL_DIR ${BUILD_MODEL_DIR}/${MODEL_NAME})

    # create the description.sdf for the model
    configure_file(
        ${PROJECT_SOURCE_DIR}/description.sdf.template
        ${MODEL_DIR}/sdf/description.sdf
    )

    # move mesh files
    file(GLOB MESHES ${SUBDIR}/*.dae)
    file(COPY ${MESHES} DESTINATION ${MODEL_DIR}/mesh)

    # move texture folders into the mesh directory
    file(GLOB TEXTURES ${SUBDIR}/*)
    foreach(TEXTURE ${TEXTURES})
        if(IS_DIRECTORY ${TEXTURE})
            file(COPY ${TEXTURE} DESTINATION ${MODEL_DIR}/mesh)
        endif()
    endforeach()
endforeach()
