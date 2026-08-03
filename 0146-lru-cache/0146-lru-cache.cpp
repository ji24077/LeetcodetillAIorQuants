class LRUCache{
    int cap;
    list<pair<int,int>> dll;
    unordered_map<int, list<pair<int,int>>::iterator> mp;

public:
    LRUCache(int capacity) : cap(capacity) {}

    void put(int key, int value){
        auto it = mp.find(key);
        if (it != mp.end()){                      // 있으면 (== → !=)
            it->second->second = value;
            dll.splice(dll.begin(), dll, it->second);
            return;                               // ← 추가
        }
        if ((int)dll.size() == cap){
            mp.erase(dll.back().first);
            dll.pop_back();
        }
        dll.emplace_front(key, value);
        mp[key] = dll.begin();
    }

    int get(int key){
        auto it = mp.find(key);
        if (it == mp.end()) return -1;            // 없으면 -1 (!= → ==)
        dll.splice(dll.begin(), dll, it->second);
        return it->second->second;
    }
};                                                // ← 세미콜론