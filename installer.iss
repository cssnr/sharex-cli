#define MyAppName "ShareX CLI"
#define MyAppPublisher "CSSNR"
#define MyAppURL "https://cssnr.github.io/sharex-cli/"
#define MyAppExeName "sharex.exe"
#ifndef MyAppVersion
  #define MyAppVersion "0.0.1"
#endif

[Setup]
AppId={{1FD9B94A-D2D2-40FA-81D5-A4B5BCD39A47}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
;Compression=lzma
;SolidCompression=yes
DefaultDirName={autopf}\sharex-cli
DefaultGroupName={#MyAppName}
;DisableDirPage=yes
;DisableProgramGroupPage=yes
DisableFinishedPage=yes
InfoBeforeFile=assets\pre-install.rtf
InfoAfterFile=assets\post-install.rtf

OutputBaseFilename=windows-installer
OutputDir=out
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
SetupIconFile=docs\favicon.ico
UninstallDisplayIcon={uninstallexe}
WizardStyle=modern dynamic

ChangesEnvironment=yes
;LicenseFile=LICENSE
;VersionInfoVersion={#MyAppVersion}

; "ArchitecturesAllowed=x64compatible" specifies that Setup cannot run
; on anything but x64 and Windows 11 on Arm.
;ArchitecturesAllowed=x64compatible
; "ArchitecturesInstallIn64BitMode=x64compatible" requests that the
; install be done in "64-bit mode" on x64 or Windows 11 on Arm,
; meaning it should use the native 64-bit Program Files directory and
; the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "dist\PathMgr\i386\PathMgr.dll"; DestDir: "{app}"; Flags: uninsneveruninstall
;Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\sharex\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#MyAppName} Folder"; Filename: "{app}"
Name: "{group}\{#MyAppName} Documentation"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"

[Tasks]
Name: modifypath; Description: "&Add to Path"

[Code]
const
  MODIFY_PATH_TASK_NAME = 'modifypath';  // Specify name of task

var
  PathIsModified: Boolean;          // Cache task selection from previous installs
  ApplicationUninstalled: Boolean;  // Has application been uninstalled?

// Import AddDirToPath() at setup time ('files:' prefix)
function DLLAddDirToPath(DirName: string; PathType, AddType: DWORD): DWORD;
  external 'AddDirToPath@files:PathMgr.dll stdcall setuponly';

// Import RemoveDirFromPath() at uninstall time ('{app}\' prefix)
function DLLRemoveDirFromPath(DirName: string; PathType: DWORD): DWORD;
  external 'RemoveDirFromPath@{app}\PathMgr.dll stdcall uninstallonly';

// Wrapper for AddDirToPath() DLL function
function AddDirToPath(const DirName: string): DWORD;
var
  PathType, AddType: DWORD;
begin
  // PathType = 0 - use system Path
  // PathType = 1 - use user Path
  // AddType = 0 - add to end of Path
  // AddType = 1 - add to beginning of Path
  if IsAdminInstallMode() then
    PathType := 0
  else
    PathType := 1;
  AddType := 0;
  result := DLLAddDirToPath(DirName, PathType, AddType);
end;

// Wrapper for RemoveDirFromPath() DLL function
function RemoveDirFromPath(const DirName: string): DWORD;
var
  PathType: DWORD;
begin
  // PathType = 0 - use system Path
  // PathType = 1 - use user Path
  if IsAdminInstallMode() then
    PathType := 0
  else
    PathType := 1;
  result := DLLRemoveDirFromPath(DirName, PathType);
end;

procedure RegisterPreviousData(PreviousDataKey: Integer);
begin
  // Store previous or current task selection as custom user setting
  if PathIsModified or WizardIsTaskSelected(MODIFY_PATH_TASK_NAME) then
    SetPreviousData(PreviousDataKey, MODIFY_PATH_TASK_NAME, 'true');
end;

function InitializeSetup(): Boolean;
begin
  result := true;
  // Was task selected during a previous install?
  PathIsModified := GetPreviousData(MODIFY_PATH_TASK_NAME, '') = 'true';
end;

function InitializeUninstall(): Boolean;
begin
  result := true;
  // Was task selected during a previous install?
  PathIsModified := GetPreviousData(MODIFY_PATH_TASK_NAME, '') = 'true';
  ApplicationUninstalled := false;
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    // Add app directory to Path at post-install step if task selected
    if PathIsModified or WizardIsTaskSelected(MODIFY_PATH_TASK_NAME) then
      AddDirToPath(ExpandConstant('{app}'));
  end;
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
  if CurUninstallStep = usUninstall then
  begin
    // Remove app directory from path during uninstall if task was selected;
    // use variable because we can't use WizardIsTaskSelected() at uninstall
    if PathIsModified then
      RemoveDirFromPath(ExpandConstant('{app}'));
  end
  else if CurUninstallStep = usPostUninstall then
  begin
    ApplicationUninstalled := true;
  end;
end;

procedure DeinitializeUninstall();
begin
  if ApplicationUninstalled then
  begin
    // Unload and delete PathMgr.dll and remove app dir when uninstalling
    UnloadDLL(ExpandConstant('{app}\PathMgr.dll'));
    DeleteFile(ExpandConstant('{app}\PathMgr.dll'));
    RemoveDir(ExpandConstant('{app}'));
  end;
end;
