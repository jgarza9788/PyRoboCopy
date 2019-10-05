
$shareFolder = @("D:\Share","E:\Share","/S")
$musicFolder = @("D:\Music","E:\Music","/S")
$installersFolder = @("D:\Installers","E:\Installers","/S")
$unityFolder = @("D:\UnityProjects","E:\UnityProjects","/S")
$documentFolder = @("D:\Documents","E:\Documents","/S")
$scriptsFolder = @("D:\Scripts","E:\Scripts","/S")

robocopy $shareFolder
robocopy $musicFolder
robocopy $installersFolder
robocopy $unityFolder
robocopy $documentFolder
robocopy $scriptsFolder