import sys, os

################################################################################
# Main function: Check if the parameters are correct and call the functions    #
# that create the project tree.                                                #
################################################################################
def main(argv):
    try:
        if argv[0] == '-h':
            error('Usage: projectGenerator.py project_name path_where_to_save')
        else:
            try:
                projectName = argv[0]
                projectPath = argv[1]
                if not os.path.exists(projectPath):
                    error('Path is not correct!')
                else:
                    print('-------------------------------------------------\r\n\tS32 Design Studio Project Generator\r\n\tNXP internal use only                     \r\n-------------------------------------------------')
                    print('\t- Project name: {0}\r\n\t- Path to project: {1}\r\n'.format(projectName, projectPath))
                    createProjectTree(projectName, projectPath)
                    createFiles(projectName, projectPath)
                    print('----Project generation completed!----')
            except:
                pass
    except:
        error('Usage: projectGenerator.py project_name path_where_to_save')

################################################################################
# Error function: Print an error message and exit                              #
################################################################################            
def error(errorDescription):
    print(errorDescription)
    exit(0)

################################################################################
# createProjectTree function: Create the necessary project folders             #
################################################################################
def createProjectTree(projectName, projectPath):
    try:
        os.mkdir('{0}\\{1}'.format(projectPath, projectName))
        os.mkdir('{0}\\{1}\\Debug_Configurations'.format(projectPath, projectName))
        os.mkdir('{0}\\{1}\\Sources'.format(projectPath, projectName))
        os.mkdir('{0}\\{1}\\Doxygen'.format(projectPath, projectName))
    except:
        error('Cannot create folders\r\nProject generation failed!')

################################################################################
# createFiles function: Create the files                                       #
################################################################################
def createFiles(projectName, projectPath):
    try:
        # Open the .project file template
        projFile = open(os.getcwd() + '\\template\\' + '.project', 'r')
        projFileStr = projFile.read()
        projFile.close()
        
        # Replace project name and copy the new file into the new project
        newProjFile = open('{0}\\{1}\\.project'.format(projectPath, projectName), 'w')
        newProjFile.write(projFileStr.replace('${ProjectName}', projectName))
        newProjFile.close()
        
        # Open the .cproject file template
        cprojFile = open(os.getcwd() + '\\template\\' + '.cproject', 'r')
        cprojFileStr = cprojFile.read()
        cprojFile.close()
        
        # Replace project name and copy the new file into the new project
        newcProjFile = open('{0}\\{1}\\.cproject'.format(projectPath, projectName), 'w')
        newcProjFile.write(cprojFileStr.replace('${ProjectName}', projectName))
        newcProjFile.close()
        
        # Open the main.c file template
        sourceFile = open(os.getcwd() + '\\template\\Sources\\' + 'main.c', 'r')
        sourceFileStr = sourceFile.read()
        sourceFile.close()
        
        # Replace project name and copy the new file into the new project
        newsourceFile = open('{0}\\{1}\\Sources\\main.c'.format(projectPath, projectName), 'w')
        newsourceFile.write(sourceFileStr.replace('${ProjectName}', projectName))
        newsourceFile.close()

        # Define debug configurations name
        debugConfNames = ['template Debug_FLASH JLink.launch', 'template Debug_RAM JLink.launch', 'template Debug_FLASH PEmicro.launch', 'template Debug_RAM PEmicro.launch']
        
        # Replace project names and copy files
        for i in range(0, (len(debugConfNames))):
            debugFile = open(os.getcwd() + '\\template\\Debug_Configurations\\' + debugConfNames[i], 'r')
            debugFileStr = debugFile.read()
            debugFile.close()
            
            newdebugFile = open('{0}\\{1}\\Debug_Configurations\\'.format(projectPath, projectName) + debugConfNames[i].replace('template', projectName) , 'w')
            newdebugFile.write(debugFileStr.replace('${ProjectName}', projectName))
            newdebugFile.close()
            
        # Open the ProcessorExpert.pe file template
        pexFile = open(os.getcwd() + '\\template\\' + 'ProcessorExpert.pe', 'r')
        pexFileStr = pexFile.read()
        pexFile.close()
        
        # Replace project name and copy the new file into the new project
        newpexFile = open('{0}\\{1}\\ProcessorExpert.pe'.format(projectPath, projectName), 'w')
        newpexFile.write(pexFileStr.replace('${ProjectName}', projectName))
        newpexFile.close()   

        # Open the doxygen documentation file template
        doxFile = open(os.getcwd() + '\\template\\Doxygen\\' + 'template.dox', 'r')
        doxFileStr = doxFile.read()
        doxFile.close()
        
        # Replace project name and copy the new file into the new project
        newDoxFile = open('{0}\\{1}\\Doxygen\\{2}.dox'.format(projectPath, projectName, projectName), 'w')
        newDoxFile.write(doxFileStr.replace('${ProjectName}', projectName))
        newDoxFile.close()            
    except IOError as e:
        error(e)
if __name__ == "__main__":
    main(sys.argv[1:])
    
    
 