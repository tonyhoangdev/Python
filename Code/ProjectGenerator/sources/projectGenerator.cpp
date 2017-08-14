#include <iostream>
#include <fstream>
#include <String.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <ctime>

#define WELCOME_TEXT "-------------------------------------------------\r\n\tS32 Design Studio Project Generator\r\n\tNXP internal use only                     \r\n-------------------------------------------------"
#define SEPARATOR    "-------------------------------------------------\r\n"

using namespace std;

/* Function Declarations */
void CreateFolder(const string folderName, const string projectPath);
void CreateProjectTree(const string projectName, const string projectPath);
void GenerateFile(const string projectName, const string projectPath, const string destinationPath, const string sourceFileName, const string destFileName );
void ReplaceStringInPlace(std::string& subject, const std::string& search, const std::string& replace);
void CreateProject(const string projectName, const string projectPath);
bool DirExists(string path);

/* Global variable where the current working directory is stored */
string g_cwd;

/*******************************************************************************
* Main function: Check if the parameters are correct and call the function     *
* that generates the project.                                                  *
*******************************************************************************/
int main(int argc, char ** argv)
{	
	char * tempPath = new char[255];
	getcwd(tempPath, 255);
	g_cwd.assign(tempPath);
	delete tempPath;

	if(argc > 1)
	{
		if(strcmp(argv[1], "-h") == 0)
		{
			cout<<"Usage: projectGenerator.exe project_name path_where_to_save"<<endl;	
		}
		else if(argc != 3)
		{
			cout<<"Invalid arguments. Use -h to get help"<<endl;
		} 
		else
		{
            cout<<WELCOME_TEXT<<endl;
            cout<<"\t- Project Name: "<<argv[1]<<endl<<"\t- Project Location: "<<argv[2]<<endl;
            cout<<SEPARATOR;
			CreateProject(argv[1], argv[2]);
			cout<<"Project Generation succedeed!"<<endl;
		}
	}
	else
	{
		cout<<"Invalid arguments. Use -h to get help"<<endl;
	}

	return 0;
}

void CreateProject(const string projectName, string projectPath)
{
	const string sourceDebugCnfNames[4] =  {"template Debug_FLASH JLink.launch", \
			   							    "template Debug_RAM JLink.launch", \
									        "template Debug_FLASH PEmicro.launch",\
									        "template Debug_RAM PEmicro.launch"};
									  
	string destDebugCnfNames[4] = sourceDebugCnfNames;
    
    const string sourceDoxyDocName = "template.dox";
    string destDoxyDocName = sourceDoxyDocName;

	if(!DirExists(projectPath))
	{
		cerr<<"Destination directory cannot be opened. Please check permissions or the path!"<<endl;
		exit(-2);
	}
	
	if((projectPath.c_str()[projectPath.size() - 1] != '\\'))
	{
		projectPath.append("\\");
	}
	
	CreateProjectTree(projectName, projectPath);
	GenerateFile(projectName, projectPath, "", ".project", ".project");
	GenerateFile(projectName, projectPath, "", ".cproject", ".cproject");
	GenerateFile(projectName, projectPath, "", "ProcessorExpert.pe", "ProcessorExpert.pe");
	GenerateFile(projectName, projectPath, "Sources", "main.c", "main.c");
	GenerateFile(projectName, projectPath, "", "Readme.htm", "Readme.htm");

    ReplaceStringInPlace(destDoxyDocName, "template", projectName);
    GenerateFile(projectName, projectPath, "Doxygen", sourceDoxyDocName, destDoxyDocName);
    
	for(int i = 0; i < 4; i++)
	{
		ReplaceStringInPlace(destDebugCnfNames[i], "template", projectName);
		GenerateFile(projectName, projectPath, "Debug_Configurations", sourceDebugCnfNames[i], destDebugCnfNames[i]);
	}
}

void CreateFolder(const string folderName, const string projectPath)
{
	string tempPath;
	tempPath = "mkdir";
	tempPath.append(" ");
	tempPath.append(projectPath);
	tempPath.append(folderName);

	system(tempPath.c_str());
}

void CreateProjectTree(const string projectName, const string projectPath)
{
	CreateFolder(projectName, projectPath);
	CreateFolder("Sources", projectPath+projectName+"\\");
	CreateFolder("Doxygen", projectPath+projectName+"\\");
	CreateFolder("Debug_Configurations", projectPath+projectName+"\\");

}

void GenerateFile(const string projectName, const string projectPath, const string destinationPath, const string sourceFileName, const string destFileName )
{
	ifstream fileBuf;
	ofstream outFile;
	string fileText;
	string filePath;
	string line;
    string prjNameBeautified = projectName;
    string * strTime;
    string * strDate;
	time_t rawTime;
    struct tm * timeInfo;
    char fmtTime[100];
    
    time(&rawTime);
    timeInfo = localtime(&rawTime);
    strftime(fmtTime, 100, "%Y-%m-%d, %H:%M", timeInfo);
    strTime = new string(fmtTime);
    
    strftime(fmtTime, 100, "%Y-%m-%d", timeInfo);
    strDate = new string(fmtTime);
    
    ReplaceStringInPlace(prjNameBeautified, "_", " ");
    
	try
		{
			filePath = g_cwd + "\\" + "template\\" + destinationPath + "\\" + sourceFileName;
			fileBuf.open(filePath.c_str());
			if(!fileBuf.is_open())
			{
				cerr<<"An error has occured during generation. Please check the paths and template directory!"<<endl;
				exit(-1);
			}
			while(!fileBuf.eof())
				{
					getline(fileBuf, line);
					fileText.append(line + "\n");
				}
			fileBuf.close();
			ReplaceStringInPlace(fileText, "${ProjectName}", projectName);
			ReplaceStringInPlace(fileText, "${ProjectName_Beautified}", prjNameBeautified);
			ReplaceStringInPlace(fileText, "${DateTime}", *strTime);
			ReplaceStringInPlace(fileText, "${Date}", *strDate);
			filePath = (projectPath + projectName + "\\" + destinationPath + "\\" + destFileName);
			outFile.open(filePath.c_str());
			if(!outFile.is_open())
			{
				cerr<<"An error has occured during generation. Please check the paths and template directory!"<<endl;
				exit(-1);
			}
			outFile.write(fileText.c_str(), fileText.size());
			outFile.close();
			delete strTime;
			delete strDate;
		}
	catch(int e)
		{
			cerr<<"An error has occured during generation. Please check the paths and template directory!"<<endl<<"Error code:"<<e<<endl;
		}
}

void ReplaceStringInPlace(std::string& subject, const std::string& search,
                          const std::string& replace)
{
	size_t pos = 0;
	while ((pos = subject.find(search, pos)) != std::string::npos)
		{
			subject.replace(pos, search.length(), replace);
			pos += replace.length();
		}
}

bool DirExists(const string path)
{
    struct stat info;

    if(stat( path.c_str(), &info ) != 0 )
        return false;
    else if(info.st_mode & S_IFDIR)
        return true;
    else
        return false;
}
