// Lambda.cpp : 定义控制台应用程序的入口点。
//
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <thread>

using namespace std;

void foo(std::function<void(int)> callback) {
	for (int i = 0; i < 100; i+=5) {
		callback(i);
		std::this_thread::sleep_for(std::chrono::seconds(1));
	}
}

int main()
{
	foo([](int x) {
		std::cout << x << " ";
	});
}

