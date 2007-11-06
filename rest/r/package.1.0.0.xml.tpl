<?xml version="1.0" encoding="UTF-8"?>
<package packagerversion="1.7.0" 
		version="2.0" 
		xmlns="http://pear.php.net/dtd/package-2.0" 
		xmlns:tasks="http://pear.php.net/dtd/tasks-1.0" 
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
		xsi:schemaLocation="http://pear.php.net/dtd/tasks-1.0 http://pear.php.net/dtd/tasks-1.0.xsd 
		http://pear.php.net/dtd/package-2.0 http://pear.php.net/dtd/package-2.0.xsd">

 <name>$packageH</name>
 <channel>jldupont.googlecode.com/svn</channel>
 <summary>Summary...</summary>
 <description>Description...</description>

 <lead>
  <name>Jean-Lou Dupont</name>
  <user>jldupont</user>
  <email>jldupont@jldupont.com</email>
  <active>yes</active>
 </lead>

 <date>2007-10-10</date>
 <time>02:44:41</time>

 <version>
  <release>1.0.0</release>
  <api>1.0.0</api>
 </version>
 
 <stability>
  <release>stable</release>
  <api>stable</api>
 </stability>

 <license uri="http://www.php.net/license">PHP License</license>

 <notes>$notes</notes>

 <contents>
  <dir name="/">

	<!-- file list begin {{ -->
	<!-- baseinstalldir: the target directory on the target machine -->
   <file baseinstalldir="JLD" name="$packageH/$packageH.php" role="php" />
    <!-- }} -->

  </dir>
 </contents>
 
 <dependencies>
  <required>

   <php>
    <min>5.0.0</min>
    <max>6.0.0</max>
   </php>

   <pearinstaller>
    <min>1.4.0a2</min>
   </pearinstaller>
 
  </required>
 </dependencies>

 <phprelease>
  <installconditions>
   <os>
    <name>*</name>
   </os>
  </installconditions>
 </phprelease>

<changelog>
 <release>
   <license uri="http://www.php.net/license">PHP License</license>
   <notes></notes>
  </release>
</changelog>

</package>
