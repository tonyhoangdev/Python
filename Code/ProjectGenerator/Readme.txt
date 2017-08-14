================================================================================
                    S32 Design Studio Project generator
================================================================================
This application creates blank S32 DS project from a template. It will create the
following files:
    ProjectFolder
      - Debug_Configurations
        - JLink launch files for flash and ram configurations 
        - PEMicro launch files for flash and ram configurations 
      - Doxygen
        - Doxygen readme file - this file must be edited to include the application 
            description, prerequisites, hardware connections, boards supported, how to 
            run and additional notes
      - Sources
        - main.c file
      - Project descriptors - .project, .cproject and ProcessorExpert.pe
      - Readme.htm - a web page that redirects to the project's page from the doxygen 
        documentation

!!Note: start-up and linker files will be linked to the project after PROJECT_KSDK_PATH 
is defined. 
How to:
 - In S32 DS open Project Properties -> Resource -> Linked Resources -> Path Variables
 - Open PROJECT_KSDK_PATH and enter the absolute path to the S32 SDK 
 - Click OK
        
Usage: projectGenerator.exe project_name path_where_to_save 

    Example: projectGenerator.exe DemoProject C:\work  

To build the executable you need:
 - MinGW GCC
 - Make utility
 
Make targets:
    - all   - builds the application
    - clean - removes the application

For questions and support contact: rares.vasile@nxp.com

================================================================================