#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <ostream>
using namespace std;

#define S_INITIALIZE			(0x0)
#define S_ADD_HOUSE				(0x1)
#define S_REFUND				(0x2)
#define S_QUERY_RENT			(0x3)
#define S_RENT_HOUSE			(0x4)

#define E_INVALID_PARAM			(0x1000001)
#define E_REPEAT_RENT			(0x1000002)
#define E_ILLEAGAL_REFUND		(0x1000003)
#define E_RENT_HOUSE			(0x1000004)
#define E_TOO_MANY_HOUSE		(0x1000005)
#define E_NO_RENTED_HOUSE		(0x1000006)


void output_result(int code) 
{
	static bool result_map_inited = false;
	map<int, string> result_map;
	if (!result_map_inited) {
		result_map[S_INITIALIZE] = "S000:初始化成功";
		result_map[S_ADD_HOUSE] = "S001:";
		result_map[S_REFUND] = "S002:";
		result_map[S_QUERY_RENT] = "S003:";
		result_map[S_RENT_HOUSE] = "S004:";
		result_map[E_INVALID_PARAM] = "E000:";
		result_map[E_REPEAT_RENT] = "E001:";
		result_map[E_ILLEAGAL_REFUND] = "E002:";
		result_map[E_RENT_HOUSE] = "E003:";
		result_map[E_TOO_MANY_HOUSE] = "E004:";
		result_map[E_NO_RENTED_HOUSE] = "E005:";
		result_map_inited = true;
	}
	if (result_map.find(code) != result_map.end())
		cout << result_map[code] << endl;
}

class House;

class Tenant
{
public:
	Tenant(string name = string(), int type = 0, int area = 0,
		int orientation = 0, int elevator = 0, int rent_month = 0)
	{
		this->name = name;
		this->type = type;
		this->area = area;
		this->orientation = orientation;
		this->elevator = elevator;
		this->rent_month = rent_month;
		this->house_index = -1;
	}
	void rent_house(const House& house);

public:
	string	name;				// 姓名，长度[1,20]
	int		type;				// 要求户型[1,4]
	int		area;				// 要求面积[1,200]
	int		orientation;		// 要求朝向[0,1]
	int		elevator;			// 要求是否有电梯[0,1]
	int		house_index;		// 所租房屋序号，没有租到为-1
	int		rent_month;			// 租房月数
};



class House
{
public:
	House(int area = 0, int type = 0, int orientation = 0, 
		int elevator = 0, int month_rental = 0)
	{
		this->area = area;
		this->type = type;
		this->orientation = orientation;
		this->elevator = elevator;
		this->month_rental = month_rental;
		this->total_rental = 0;
		this->rented = 0;
		this->index = -1;
	}

	bool satisfy(const Tenant& tenant) 
	{
		if (this->rented)
			return false;
		bool s_area = area >= tenant.area;
		bool s_type = type >= tenant.type;
		bool s_orientation = (tenant.orientation == 0) || 
			(tenant.orientation == 1 && orientation == 3);
		bool s_elevator = (tenant.elevator == 0) || 
			(tenant.elevator == 1 && elevator == 1);
		return 	s_area && s_type && s_orientation && s_elevator;
	}

	void rent_to_tenant(const Tenant& tenant) 
	{
		this->total_rental += this->month_rental * tenant.rent_month;
		this->rented = 1;
	}

	void refund(const Tenant& tenant) 
	{
		this->total_rental -= (this->month_rental-1) * tenant.rent_month;
		this->rented = 0;
	}

	static bool compare_by_satify(const House& h1, const House& h2) 
	{
		if (h1.area < h2.area)
			return true;
		if (h1.area > h2.area)
			return false;

		if (h1.type > h2.type)
			return true;
		if (h1.type < h2.type)
			return false;

		if (h1.month_rental < h2.month_rental)
			return true;
		if (h1.month_rental > h2.month_rental)
			return false;

		return h1.index < h2.index;
	}

	static bool compare_by_rental(const House& h1, const House& h2) 
	{
		if (h1.total_rental > h2.total_rental)
			return true;
		if (h1.total_rental < h2.total_rental)
			return false;

		int orient_weigh[] = { 2, 3, 4, 1 };
		if (orient_weigh[h1.orientation-1] > orient_weigh[h2.orientation-1])
			return true;
		if (orient_weigh[h1.orientation-1] < orient_weigh[h2.orientation-1])
			return false;

		if (h1.elevator > h2.elevator)
			return true;
		if (h1.elevator < h2.elevator)
			return false;

		return h1.type < h2.type;
	}

	friend ostream& operator<< (ostream &os, const House& house)
	{
		cout << house.total_rental << " "
			 << house.orientation << " "
			 << house.elevator << " "
			 << house.type << " "
			 << house.index;
		return os;
	}
public:
	int		area;				// 面积[1,200]
	int		type;				// 户型[1,4]
	int		orientation;		// 朝向[1,4]
	int		elevator;			// 是否有电梯[0,1]
	int		month_rental;		// 每月租金[100,20000]
	int		total_rental;		// 当前已收的总租金
	int		rented;				// 是否已出租[0,1]
	int		index;				// 最初录入顺序
};

void Tenant::rent_house(const House& house) 
{
	this->house_index = house.index;
}

class Tenants : public vector<Tenant>
{
public:
	Tenants::iterator find(const string& name) 
	{
		for (Tenants::iterator it = this->begin(); 
			it != this->end(); ++it)
			if (it->name == name) {
				return it;
			}
		return this->end();
	}
};
typedef vector<House>		Houses;

class RentManager 
{
public:
	static int add_house(House& house) {
		house.index = RentManager::houses.size();
		RentManager::houses.push_back(house);
		return S_ADD_HOUSE;
	}

	static void get_satisfy_houses(Houses& satisfy_houses, const Tenant& tenant) 
	{
		for (Houses::iterator it = RentManager::houses.begin();
			it != RentManager::houses.end(); ++it) {
			if (it->satisfy(tenant)) {
				satisfy_houses.push_back(*it);
			}
		}
	}

	static void get_rented_houses(Houses& rented_houses)
	{
		for (Houses::iterator it = RentManager::houses.begin();
			it != RentManager::houses.end(); ++it) {
			if (it->total_rental > 0) {
				rented_houses.push_back(*it);
			}
		}
	}

	static int rent(int house_index, Tenant& tenant) 
	{
		House& house = RentManager::houses[house_index];
		house.rent_to_tenant(tenant);

		tenant.rent_house(house);
		RentManager::tenants.push_back(tenant);

		return S_RENT_HOUSE;
	}

	static int refund(string name) 
	{
		Tenants::iterator it = RentManager::tenants.find(name);
		if (it == RentManager::tenants.end())
			return E_ILLEAGAL_REFUND;
		RentManager::houses[it->house_index].refund(*it);
		RentManager::tenants.erase(it);
		return S_REFUND;
	}
public:
	static Houses	houses;			// 系统中录入的所有房屋
	static Tenants	tenants;		// 租到房的租户
};

Houses RentManager::houses;
Tenants RentManager::tenants;

int init() 
{
	return S_INITIALIZE;
}

int add_house(int area, int type, int orientation,
	int elevator, int month_rental) 
{
	// TODO:check param
	House house = House(area, type, orientation, 
						elevator, month_rental);
	RentManager::add_house(house);
	return 0;
}

int add_tenant(string name, int type, int area, 
	int orientation, int elevator, int rent_month) 
{
	// todo:check param
	if (RentManager::tenants.find(name) != RentManager::tenants.end()) {
		return E_REPEAT_RENT;
	}
	Tenant tenant = Tenant(name, type, area, 
						   orientation, elevator, rent_month);

	Houses satified_houses;
	RentManager::get_satisfy_houses(satified_houses, tenant);
	
	if (satified_houses.empty())
		return E_NO_RENTED_HOUSE;

	sort(satified_houses.begin(), satified_houses.end(), 
		House::compare_by_satify);
	
	return RentManager::rent(satified_houses[0].index, tenant);
}

int query() 
{
	Houses rented_houses;
	RentManager::get_rented_houses(rented_houses);
	if (rented_houses.empty())
		return E_NO_RENTED_HOUSE;

	sort(rented_houses.begin(), rented_houses.end(), House::compare_by_rental);
	for (Houses::iterator it = rented_houses.begin();
		it != rented_houses.end(); ++it) {
		cout << *it << endl;
	}
	return S_QUERY_RENT;
}

int refund(string name) 
{
	return RentManager::refund(name);
}

int main(int argc, char* argv) 
{
	add_house(140, 2, 1, 1, 800);
	add_house(120, 2, 1, 1, 800);
	add_house(100, 2, 1, 1, 800);
	add_house(100, 3, 1, 1, 800);
	add_house(100, 3, 3, 1, 800);
	add_house(100, 3, 3, 1, 600);
	add_tenant("1", 2, 80, 0, 1, 10);
	add_tenant("2", 2, 80, 0, 0, 10);
	add_tenant("3", 2, 80, 0, 0, 10);
	add_tenant("4", 2, 80, 0, 0, 10);
	add_tenant("5", 2, 80, 0, 0, 10);
	add_tenant("6", 2, 80, 0, 0, 10);
	int code = query();
	output_result(code);
	output_result(code);
}