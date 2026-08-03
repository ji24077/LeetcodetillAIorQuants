class LRUCache{
    int cap; // for cap

    list<pair<int, int>> dll; // list that contains list of pair.

    unordered_map<int, list<pair<int, int>> :: iterator> mp; // to store the pointer of list.

    public:
        LRUCache(int capacity) : cap(capacity) {}

        int get(int key){
            auto it = mp.find(key);
            if(it == mp.end()){
                return -1;
            }
            dll.splice(dll.begin(), dll, it->second);
            return it->second->second;
        }
        void put(int key, int value){
            auto it = mp.find(key);

            if (it != mp.end()){
                //if key exists,
                it->second->second = value;
                dll.splice(dll.begin(), dll, it->second);
                return;
            }
            if ((int)dll.size() == cap){
                mp.erase(dll.back().first);
                dll.pop_back();
            } 
            dll.emplace_front(key,value);

            mp[key]= dll.begin();
        }
    
};