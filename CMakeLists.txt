cmake_minimum_required(VERSION 3.0.2)
project(warehouse)

find_package(catkin REQUIRED)
catkin_package()

## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

# create the appropriate files for tools
file(GLOB SUBDIRS ${PROJECT_SOURCE_DIR}/3Dwarehouse/tools/*)
foreach(SUBDIR ${SUBDIRS})
    get_filename_component(MODEL_NAME ${SUBDIR} NAME)
    set(MODEL_DIR ${CATKIN_PACKAGE_SHARE_DESTINATION}/models/${MODEL_NAME})

    # create the description.sdf for the model
    configure_file(
        ${PROJECT_SOURCE_DIR}/description.sdf.template
        ${MODEL_DIR}/sdf/description.sdf
    )

    # move the mesh files
    file(GLOB MESH ${SUBDIR}/*.dae)
    file(COPY ${MESH} DESTINATION ${MODEL_DIR}/mesh)

    # move the color files

endforeach()
