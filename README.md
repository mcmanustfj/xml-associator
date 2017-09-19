# xml-associator
Associates different xml document types (doctypes) with different programs.

This Python script opens XML documents (given as command line inputs) with different programs.  Currently, the default program is Notepad++, and the score-partwise doctype is opened with MuseScore 2.  It's easy to extend this script to work with other doctypes and programs by adding to the programs dict in the script.  

In order to work with Windows file association, it may be necessary to either package the script as an executable or to have an intermediary program in C or some other compiled language open the script.  
