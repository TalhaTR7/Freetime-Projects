#pragma once
#include "Linked.h"
using namespace std;

const int tableSize = 7;

class Collection
{
private:

    LinkedTraveller Table[tableSize];

    int hashValue(string name) {
        int bucket = 0;
        for (int i = 0; i < name.size(); i++)
            bucket += name[i];
        return bucket % tableSize;
    }
    
public:

    int size = 0;

    void insert(traveller tour) {
        int index = hashValue(tour.name);
        Table[index].insert(tour);
        size++;
    }

    LinkedTraveller& copy(LinkedTraveller& List) {
        for (int i = 0; i < tableSize; i++)
            List += Table[i];
        return List;
    }

    void truncate() {
        for (int i = 0; i < tableSize; i++)
            Table[i].clear();
        size = 0;
    }

    void print() {
        system("cls");
        cout << "\x1B[93mname\t\tage\t\ttoVisit\n\x1B[0m";
        for (int i = 0; i < tableSize; i++)
            Table[i].print(false);
        cout << '\n' << size << " record(s) showing up\n";
    }


    void readJSON(const string& file) {
        ifstream in;
        in.open(file);
        if (in.fail()) throw invalid_argument("file could not open");
        while (1) {
            traveller tour;
            bool finish = tour.readJSON(in);
            insert(tour);
            if (finish) break;
        }
        in.close();
    }

    void writeJSON(const string& file) {
        ofstream out;
        out.open(file, ios::trunc);
        if (!out) throw invalid_argument("file could not open");
        int tempSize = size;
        out << "[\n";
        for (int i = 0; i < tableSize; i++) {
            for (int j = 0; j < Table[i].size; j++) {
                out << Table[i][j].giveJSON();
                tempSize--;
                if (tempSize > 0) out << ",\n";
                else out << "\n";
            }
        }
        out << ']';
        out.close();
    }

    LinkedTraveller SearchByName(vector<string> name) {
        LinkedTraveller people;
        for (int i = 0; i < name.size(); i++)
            people += Table[hashValue(name[i])].SearchByName(vector<string>{name[i]});
        return people;
    }

    LinkedTraveller SearchByAge(vector<int> age) {
        LinkedTraveller people;
        for (int k = 0; k < age.size(); k++) {
            for (int i = 0; i < tableSize; i++) {
                LinkedTraveller temp = Table[i].SearchByAge(vector<int>{age[k]});
                if (temp.size) {
                    for (int j = 0; j < temp.size; j++)
                        people.insert(temp[j]);
                }
            }
        }
        return people;
    }

    LinkedTraveller SearchByTour(vector<string> city) {
        LinkedTraveller people;
        for (int j = 0; j < city.size(); j++)
            for (int i = 0; i < tableSize; i++)
                people += Table[i].SearchByTour(vector<string>{city[j]});
        return people;
    }

    void UpdateName(LinkedTraveller tours, string name) {
        for (int k = 0; k < tours.size; k++)
            for (int i = 0; i < tableSize; i++)
                for (int j = 0; j < Table[i].size; j++)
                    if (Table[i][j] == tours[k])
                        Table[i][j].name = name;
    }

    void UpdateAge(LinkedTraveller tours, int age) {
        for (int k = 0; k < tours.size; k++)
            for (int i = 0; i < tableSize; i++)
                for (int j = 0; j < Table[i].size; j++)
                    if (Table[i][j] == tours[k])
                        Table[i][j].age = age;
    }

    void InsertCity(LinkedTraveller tours, string city) {
        for (int k = 0; k < tours.size; k++)
            for (int i = 0; i < tableSize; i++)
                for (int j = 0; j < Table[i].size; j++)
                    if (Table[i][j] == tours[k])
                        Table[i][j].toVisit.insert(city);
    }

    void RemoveCity(LinkedTraveller tours, string city) {
        for (int k = 0; k < tours.size; k++)
            for (int i = 0; i < tableSize; i++)
                for (int j = 0; j < Table[i].size; j++)
                    if (Table[i][j] == tours[k])
                        Table[i][j].toVisit.remove(city);
    }

    void ReplaceCity(LinkedTraveller tours, string oldCity, string newCity) {
        for (int k = 0; k < tours.size; k++)
            for (int i = 0; i < tableSize; i++)
                for (int j = 0; j < Table[i].size; j++)
                    if (Table[i][j] == tours[k])
                        Table[i][j].toVisit.replace(oldCity, newCity);
    }

    void remove(LinkedTraveller tours) {       
        for (int j = 0; j < tours.size; j++)
            for (int i = 0; i < tableSize; i++)
                for (int k = 0; k < Table[i].size; k++)
                    if (Table[i][k] == tours[j])
                        Table[i].remove(Table[i][k]);
        size -= tours.size;
    }
};