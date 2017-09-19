#include <stdlib.h>
#include <unistd.h>
#include <string>
#include <iostream>

using namespace std;

int main(int argc, char** argv) {
	string cmd = "python \"C:\\path\\to\\xml-associator.py\" ";
	if(argc != 2) {
		return 1;
  }
	string file = string("\"")+argv[1]+"\"";
	cmd += file;
	cout << cmd << std::endl;
	system(cmd.c_str());
}
