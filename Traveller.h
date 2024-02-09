#pragma once
#include "Linked.h"
using namespace std;


struct traveller
{
    string name;
    int age;
    LinkedStr toVisit;

    traveller() : toVisit() {}

    bool operator == (traveller& tour) {
        return name == tour.name
            && age == tour.age
            && toVisit == tour.toVisit;
    }

    bool operator != (traveller& tour) {
        return !((*this) == tour);
    }

    string giveJSON() {
        string json = "\t{\n";
        json += tab(2) + R"("name" : ")" + name + "\",\n";
        json += tab(2) + R"("age" : )" + to_string(age) + ",\n";
        json += tab(2) + R"("toVisit" : )" + toVisit.giveList() + "\n";
        json += "\t}";
        return json;
    }

    bool readJSON(ifstream& in) {
        string line, word;
        // read name from json
        while (in.get() != '"') in.ignore();
        getline(in, line, '\n');
        stringstream extraction1(line);
        while (getline(extraction1, word, '"'))
            if (word != "name" && word != " : " && word != ",")
                name += word;
        // read age from json
        while (in.get() != '"') in.ignore();
        getline(in, line, '\n');
        word = line.substr(line.find(':') + 2, line.find(',') - line.find(':') + 2);
        age = stoi(word);
        // read cities to visit from json
        while (in.get() != '"') in.ignore();
        getline(in, line, '\n');
        stringstream extraction3(line);
        while (getline(extraction3, word, '"'))
            if (word != "toVisit" && word != " : [" && word != ", " && word != "]")
                toVisit.insert(word);
        in >> line;
        return line == "}" ? true : false;
    }

    private: string tab(int limit = 1) {
        string space;
        for (int i = 0; i < limit; i++) space += '\t';
        return space;
    }
};

traveller giveTour() {
    traveller tour;
    system("cls");
    cout << "Enter your name: ";
    cin >> tour.name;
    system("cls");
    cout << "Enter your age: ";
    cin >> tour.age;
    system("cls");
    cout << "Start entering your future tours\n(type <done> to finish)\n";
    string city;
    while (true) {
        cin >> city;
        if (city == "done") break;
        tour.toVisit.insert(city);
    }
    system("cls");
    return tour;
}