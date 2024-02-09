#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <windows.h>
#include <set>
#include "Linked.h"
#include "Traveller.h"
#include "Collection.h"
using namespace std;

Collection db;

void error(int index) {
    system("cls");
    string errors[] = {"Create/Read data in order to make changes to the database",
                    "Select a valid operation to perform",
                    "File could not found",
                    "Invalid attribute"};
    cerr << errors[index];
    Sleep(1500);
}

string askOperation() {
    string option;
    do {
        system("cls");
        if (db.size) {
            db.print();
            cout << "-------------------------------------------------------------\n";
        }
        cout << "Create    "
                  << "Read    "
                  << "Find    "
                  << "Write    "
                  << "Clear    "
                  << "Quit\n"
                  << "\nSelect an operation to perform: ";
        cin >> option;
        if (option == "create" || option == "read" || option == "find" || option == "quit" || option == "write" || option == "clear") {
            if ((option == "find" || option == "write" || option == "clear") && !db.size) {
                error(0);
                continue;
            }
            break;
        }
        error(1);
    } while (true);
    return option;
}

void readOperation() {
    if (db.size) {
        char confirm;
        do {
            system("cls");
            cout << "Do you want to append database? <y/n>: ";
            cin >> confirm;
            if (confirm == 'y' || confirm == 'n') break;
            error(1);
        } while (true);
        if (confirm == 'n') db.truncate();
    }
    try {
        system("cls");
        string file;
        cout << "Enter a file to read from: ";
        cin >> file;
        db.readJSON(file);
        system("cls");
        cout << "Reading data...";
        Sleep(1500);
    }
    catch (const invalid_argument& error) {
        system("cls");
        cout << "invalid argument :/ " << error.what() << endl;
        Sleep(1500);
    }
}

void nextPhase(LinkedTraveller people) {
    string option;
    while (true) {
        system("cls");
        people.print();
        cout << "-------------------------------------------------------------\n"
            << "Update   Delete\n"
            << "\nSelect an operation, <back> to go back: ";
        cin >> option;

        if (option == "delete") {
            db.remove(people);
            system("cls");
            cout << "Record(s) deleted successfully";
            Sleep(1500);
            break;
        }
        else if (option == "update") {
            string attribute;
            while (true) {
                system("cls");
                people.print();
                cout << "-------------------------------------------------------------\n"
                    << "Name    Age    City    None\n"
                    << "\nUpdate what? ";
                cin >> attribute;
                if (attribute == "name") {
                    string name;
                    cout << "\nEnter updated name: ";
                    cin >> name;
                    db.UpdateName(people, name);
                    break;
                }
                else if (attribute == "age") {
                    int age;
                    cout << "\nEnter updated age: ";
                    cin >> age;
                    db.UpdateAge(people, age);
                    break;
                }
                else if (attribute == "city") {
                    while (true) {
                        cout << "\nDo you want to <insert>, <replace> or <remove> any city? ";
                        cin >> option;
                        if (option == "insert") {
                            string city;
                            cout << "\nEnter a city to insert: ";
                            cin >> city;
                            db.InsertCity(people, city);
                            break;
                        }
                        else if (option == "remove") {
                            try {
                                string city;
                                cout << "\nEnter a city to remove: ";
                                cin >> city;
                                db.RemoveCity(people, city);
                            }
                            catch (const invalid_argument& error) {
                                system("cls");
                                cout << "invalid argument :/ " << error.what() << endl;
                                Sleep(1500);
                            }
                            break;
                        }
                        else if (option == "replace") {
                            string oldCity, newCity;
                            cout << "\nEnter the city to replace: ";
                            cin >> oldCity;
                            cout << "Enter a city to replace with: ";
                            cin >> newCity;
                            db.ReplaceCity(people, oldCity, newCity);
                            break;
                        }
                    }
                    break;
                }
                else if (attribute == "none") break;
                else error(3);
            }
            system("cls");
            cout << "Record(s) updated successfully";
            Sleep(1500);
            break;
        }
        else if (option == "back") break;
        error(1);
    }
}

void findOperation() {
    LinkedTraveller people;
    string attribute;
    while (true) {
        system("cls");
        people.print();
        cout << "-------------------------------------------------------------\n";
        cout << "Apply filter (type <done> to finish, <back> to go back)\n"
            << "\n   Name    Age    City\n"
            << "\nFind by ";
        cin >> attribute;
        if (attribute == "back") break;
        else if (attribute == "done") {
            nextPhase(people);
            break;
        }
        else if (attribute == "name") {
            vector<string> name;
            string value;
            cout << "\nTyping <done> exits\n\nName: ";
            do {
                cin >> value;
                cout << "   OR ";
                if (value == "done") break;
                name.push_back(value);
            } while (true);
            if (people.size) people = people.SearchByName(name);
            else people += db.SearchByName(name);
            people.removeDuplicates();
        }
        else if (attribute == "age") {
            vector<int> age;
            int value;
            cout << "\nAnything -ve exits\n\nAge: ";
            do {
                cin >> value;
                cout << "  OR ";
                if (value < 0) break;
                age.push_back(value);
            } while (true);
            if (people.size) people = people.SearchByAge(age);
            else people += db.SearchByAge(age);
            people.removeDuplicates();
        }
        else if (attribute == "city") {
            vector<string> city;
            string value;
            cout << "\nTyping <done> exits\n\nCity: ";
            do {
                cin >> value;
                cout << "   OR ";
                if (value == "done") break;
                city.push_back(value);
            } while (true);
            if (people.size) people = people.SearchByTour(city);
            else people += db.SearchByTour(city);
            people.removeDuplicates();
        }
    }
}

void writeOperation() {
    system("cls");
    try {
        system("cls");
        string file;
        cout << "Enter a file to write on: ";
        cin >> file;
        db.writeJSON(file);
        system("cls");
        cout << "File updated successfully";
        Sleep(1500);
    }
    catch (const invalid_argument& error) {
        system("cls");
        cout << "invalid argument :/ " << error.what() << endl;
        Sleep(1500);
    }
}

int main()
{
    cout << "Starting session...";
    Sleep(1500);
    while (true) {
        system("cls");
        if (db.size) {
            db.print();
            cout << endl;
        }
        string option = askOperation();
        if (option == "quit") {
            cout << "\nSigning out...";
            Sleep(1500);
            system("cls");
            cout << "Session ended\n";
            break;
        }
        else {
            if (option == "create") db.insert(giveTour());
            else if (option == "read") readOperation();
            else if (option == "find") findOperation();
            else if (option == "write") writeOperation();
            else if (option == "clear") db.truncate();
        }
    }
}