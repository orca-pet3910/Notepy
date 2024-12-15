var shortcutName = "Notepy.lnk";
var scriptDir = WScript.ScriptFullName.replace(/[^\\]+$/, "");
var targetPath = scriptDir + "notepy.pyw";
var iconPath = scriptDir + "fileicon.ico";
var desktopPath = WScript.CreateObject("WScript.Shell").SpecialFolders("Desktop");


function createShortcut() {
    var shell = WScript.CreateObject("WScript.Shell");
    var shortcut = shell.CreateShortcut(desktopPath + "\\" + shortcutName);
    shortcut.TargetPath = "pythonw.exe";
    shortcut.Arguments = targetPath;
    shortcut.WorkingDirectory = scriptDir;
    shortcut.IconLocation = iconPath;
    shortcut.Save();
}


var fso = new ActiveXObject("Scripting.FileSystemObject");
if (fso.FileExists(iconPath)) {
    createShortcut();
    
} else {
    WScript.Echo("Icon file not found: " + iconPath);
}

// MADE WITH HELP