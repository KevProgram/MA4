#include <cstdlib>
// Person class 

// class Person{
// 	public:
// 		Person(int);
// 		int get();
// 		void set(int);
// 		int fib();
// 	private:
// 		int age;
// 		int n;
// 		int fib_private();
// 	};
 
// Person::Person(int n){
// 	age = n;
// 	}
 
// int Person::get(){
// 	return age;
// 	}
 
// void Person::set(int n){
// 	age = n;
// 	}

// int Person::fib(){
// 	return fib_private();
// 	}
// int fib_private(int age){
// 	if (age <=1){
// 	return age;
// 	}
// 	else {
// 	return  fib_private(age-1) + fib_private(age-2);
// 	}
// 	}



// extern "C"{
// 	Person* Person_new(int n) {return new Person(n);}
// 	int Person_get(Person* person) {return person->get();}
// 	void Person_set(Person* person, int n) {person->set(n);}
// 	void Person_delete(Person* person){
// 		if (person){
// 			delete person;
// 			person = nullptr;
// 			}
// 		}
// 	}







class Person{
	public:
		Person(int);
		int get();
		int fib();
		void set(int);
	private:
		int age;
		int fib(int);
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}

int Person::fib(){
	return fib(age);
}

int Person::fib(int n){
	if (n <= 1){
	return (n);

	return (fib(n-1) + fib(n-2));
}


//hejsan

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	int Person_fib(Person* person) {return person->fib();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
