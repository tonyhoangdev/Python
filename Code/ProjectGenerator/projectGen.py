import sys, os
from datetime import time, datetime, date

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
        os.mkdir('{0}\\{1}\\doxygen'.format(projectPath, projectName))
    except:
        error('Cannot create folders\r\nProject generation failed!')

################################################################################
# createFiles function: Create the files                                       #
################################################################################
def createFiles(projectName, projectPath, cpuName, cpuPins):
    try:
        projectName2 = projectName + "_" + cpuName.lower()
        dt = datetime.now()
        dtStr = dt.strftime("%Y-%m-%d, %H:%m")
        dateStr = dt.strftime("%Y-%m-%d")

        # Open the .project file template
        projFile = open(os.getcwd() + '\\template\\' + 'ppc.project', 'r')
        projFileStr = projFile.read()
        projFile.close()

        # Replace project name and copy the new file into the new project
        newProjFile = open('{0}\\{1}\\.project'.format(projectPath, projectName), 'w')
        projFileStr = projFileStr.replace('${ProjectName}', projectName2)
        projFileStr = projFileStr.replace('${CPU}', cpuName)
        projFileStr = projFileStr.replace('${PINS}', cpuPins)
        newProjFile.write(projFileStr)
        newProjFile.close()

        # Open the .cproject file template
        cprojFile = open(os.getcwd() + '\\template\\' + 'ppc.cproject', 'r')
        cprojFileStr = cprojFile.read()
        cprojFile.close()

        # Replace project name and copy the new file into the new project
        newcProjFile = open('{0}\\{1}\\.cproject'.format(projectPath, projectName), 'w')
        cprojFileStr = cprojFileStr.replace('${ProjectName}', projectName2)
        cprojFileStr = cprojFileStr.replace('${CPU}', cpuName)
        cprojFileStr = cprojFileStr.replace('${PINS}', cpuPins)
        newcProjFile.write(cprojFileStr)
        newcProjFile.close()

        # Open the main.c file template
        sourceFile = open(os.getcwd() + '\\template\\Sources\\' + 'main_ppc.c', 'r')
        sourceFileStr = sourceFile.read()
        sourceFile.close()

        # Replace project name and copy the new file into the new project
        newsourceFile = open('{0}\\{1}\\Sources\\main.c'.format(projectPath, projectName), 'w')
        sourceFileStr = sourceFileStr.replace('${ProjectName}', projectName2)
        sourceFileStr = sourceFileStr.replace('${CPU}', cpuName)
        sourceFileStr = sourceFileStr.replace('${PINS}', cpuPins)
        sourceFileStr = sourceFileStr.replace('${DateTime}', dtStr)
        newsourceFile.write(sourceFileStr)
        newsourceFile.close()

        # Define debug configurations name
        debugConfNames = ['template Debug_FLASH JLink.launch', 'template Debug_RAM JLink.launch', 'template Debug_FLASH PEmicro.launch', 'template Debug_RAM PEmicro.launch']
        debugConfNames_PPC = ['template_ppc_Debug_FLASH PEmicro.launch', 'template_ppc_Debug_RAM PEmicro.launch']

        # Replace project names and copy files
        for i in range(0, (len(debugConfNames_PPC))):
            debugFile = open(os.getcwd() + '\\template\\Debug_Configurations\\' + debugConfNames_PPC[i], 'r')
            debugFileStr = debugFile.read()
            debugFile.close()

            newdebugFile = open('{0}\\{1}\\Debug_Configurations\\'.format(projectPath, projectName) + debugConfNames_PPC[i].replace('template_ppc', projectName2) , 'w')
            debugFileStr = debugFileStr.replace('${ProjectName}', projectName2)
            debugFileStr = debugFileStr.replace('${CPU}', cpuName)
            newdebugFile.write(debugFileStr)
            newdebugFile.close()

        # Open the ProcessorExpert.pe file template
        pexFile = open(os.getcwd() + '\\template\\' + 'ProcessorExpert_ppc.pe', 'r')
        pexFileStr = pexFile.read()
        pexFile.close()

        # Replace project name and copy the new file into the new project
        newpexFile = open('{0}\\{1}\\ProcessorExpert.pe'.format(projectPath, projectName), 'w')
        pexFileStr = pexFileStr.replace('${ProjectName}', projectName2)
        pexFileStr = pexFileStr.replace('${CPU}', cpuName)
        pexFileStr = pexFileStr.replace('${PINS}', cpuPins)
        pexFileStr = pexFileStr.replace('${Date}', dateStr)
        newpexFile.write(pexFileStr)
        newpexFile.close()

        # Open the description.txt file template
        desFile = open(os.getcwd() + '\\template\\' + 'description.txt', 'r')
        desFileStr = desFile.read()
        desFile.close()

        # Replace description and copy the new file into the new project
        newDesFile = open('{0}\\{1}\\description.txt'.format(projectPath, projectName), 'w')
        desFileStr = desFileStr.replace('${ProjectName}', projectName2)
        desFileStr = desFileStr.replace('${CPU}', cpuName)
        desFileStr = desFileStr.replace('${PINS}', cpuPins)
        newDesFile.write(desFileStr)
        newDesFile.close()

        # Open the doxygen documentation file template
        doxFile = open(os.getcwd() + '\\template\\Doxygen\\' + 'template_ppc.dox', 'r')
        doxFileStr = doxFile.read()
        doxFile.close()

        # Replace project name and copy the new file into the new project
        newDoxFile = open('{0}\\{1}\\Doxygen\\{2}.dox'.format(projectPath, projectName, projectName), 'w')
        newDoxFile.write(doxFileStr.replace('${ProjectName}', projectName2))
        newDoxFile.close()
    except IOError as e:
        error(e)

################################################################################
# Main function: Check if the parameters are correct and call the functions    #
# that create the project tree.                                                #
################################################################################
def main(argv):
    projectName = argv[1]
    projectPath = argv[2]
    cpuName = argv[3]
    cpuPins = argv[4]
    print(projectName)
    print(projectPath)
    print(cpuName)
    print(cpuPins)

    if not os.path.exists(projectPath):
        error('Path is not correct!')
    else:
        print('-------------------------------------------------\r\n\tS32 Design Studio Project Generator\r\n\tNXP internal use only                     \r\n-------------------------------------------------')
        print('\t- Project name: {0}\r\n\t- Path to project: {1}\r\n'.format(projectName, projectPath))
        createProjectTree(projectName, projectPath)
        createFiles(projectName, projectPath,cpuName, cpuPins)
        print('----Project generation completed!----')

main(sys.argv)