#pragma once
using namespace std;

template <class myType>
class Linked
{
protected:

    struct Node {
        myType data;
        Node* next;
        Node(myType value) : data(value), next(nullptr) {}
    };

    Node* root;
    
    Node* Search(myType value) {
		Node* temp = root;
		while (temp)
			if (temp->data == value) return temp;
			else temp = temp->next;
		return nullptr;
	}

public:

    int size = 0;

    Linked() : root(nullptr) {}

    void insert(myType value) {
        if (!root) root = new Node(value);
        else {
            Node* temp = root;
            while (temp->next) temp = temp->next;
            temp->next = new Node(value);
        }
        size++;
    }

    bool operator == (const Linked& List) {
        Node* temp1 = root;
        Node* temp2 = List.root;
        while (temp1 && temp2) {
            if (temp1->data != temp2->data) return false;
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        return !temp1 && !temp2;
    }

    bool operator != (const Linked& List) {
        return !((*this) == List);
    }

    myType& operator[] (int index) {
        if (index < 0 || index >= size)
            throw invalid_argument("index out of range");
        Node* temp = root;
        while (index--) temp = temp->next;
        return temp->data;
    }

    myType front() {
        return root->data;
    }

    void removeDuplicates() {
        Node* temp = root;
        while (temp != nullptr) {
            Node* store = temp->next;
            Node* previous = temp;
            while (store != nullptr) {
                if (store->data == temp->data) {
                    previous->next = store->next;
                    size--;
                    delete store;
                } else {
                    previous = store;
                }
                store = store->next;
            }
            temp = temp->next;
        }
    }

    void remove(myType value) {
        if (Search(value)) {
            if (root->data == value) root = root->next;
            else {
                Node* temp = root;
                while (temp->next->data != value)
                    temp = temp->next;
                temp->next = temp->next->next;
            }
            size--;
        }
    }

    void clear() {
        while (root) remove(front());
    }
};

class LinkedStr : public Linked<string>
{
public:

    bool hasCity(string city) {
        for (int i = 0; i < size; i++)
            if ((*this)[i] == city) return true;
        return false;
    }

    void replace(string oldValue, string newValue) {
        if (Search(oldValue))
            Search(oldValue)->data = newValue;
    }

    string giveValues() {
        Node* temp = root;
        string List;
        while (temp) {
            List += temp->data;
            temp = temp->next;
            if (temp) List += ", ";
        }
        return List;
    }

    string giveList() {
        Node* temp = root;
        string List = "[";
        while (temp) {
            List += "\"" + temp->data + "\"";
            temp = temp->next;
            if (temp) List += ", ";
        }
        List += "]";
        return List;
    }
};

#include "Traveller.h"

class LinkedTraveller : public Linked<traveller>
{
public:

    LinkedTraveller subtract(LinkedTraveller tours) {
        LinkedTraveller common;
        for (int i = 0; i < size; i++) {
            int count = 0;
            for (int j = 0; j < tours.size; j++)
                if ((*this)[i] == tours[j]) count++;
            if (count) common.insert((*this)[i]);
        }
        return common;
    }

    LinkedTraveller& operator+= (LinkedTraveller tours) {
        if (!root) root = tours.root;
        else {
            Node* temp = root;
            while (temp->next) temp = temp->next;
            temp->next = tours.root;
        }
        size += tours.size;
        return *this;
    }

    void print(bool header = true) {
        if (header) cout << "\x1B[93mname\t\tage\t\ttoVisit\n\x1B[0m";
        Node* temp = root;
        int count = 0;
        while (temp) {
            cout << temp->data.name << "\t\t" << temp->data.age
                << "\t\t" << temp->data.toVisit.giveValues() << endl;
            temp = temp->next;
        }
        if (header) cout << '\n' << size << " record(s) found\n";
    }

    void printJSON() {
        Node* temp = root;
        cout << "[\n";
        while (temp) {
            cout << temp->data.giveJSON();
            if (temp->next) cout << ",\n";
            temp = temp->next;
        }
        cout << "\n]\n";
    }

    LinkedTraveller SearchByName(vector<string> name) {
        LinkedTraveller people;
        for (int j = 0; j < name.size(); j++)
            for (int i = 0; i < size; i++)
                if ((*this)[i].name == name[j])
                    people.insert((*this)[i]);
        return people;
    }

    LinkedTraveller SearchByAge(vector<int> age) {
        LinkedTraveller people;
        for (int j = 0; j < age.size(); j++)
            for (int i = 0; i < size; i++)
                if ((*this)[i].age == age[j])
                    people.insert((*this)[i]);
        return people;
    }

    LinkedTraveller SearchByTour(vector<string> city) {
        LinkedTraveller people;
        for (int j = 0; j < city.size(); j++)
            for (int i = 0; i < size; i++)
                if ((*this)[i].toVisit.hasCity(city[j]))
                    people.insert((*this)[i]);
        removeDuplicates();
        return people;
    }
};