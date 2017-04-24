#include <iostream>

using namespace std;

class a {
	int t;

public:
	void add(a other){
		t += other.t;
	}
};

int main(){
	return 0;
}