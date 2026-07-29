// Last updated: 7/29/2026, 10:13:16 AM
class TimeMap {
public:
    map<int,vector<string>>m;
    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        if(m.find(timestamp)!=m.end()){
            m.erase(timestamp);
        }
        m[timestamp].push_back(key);
        m[timestamp].push_back(value);
    }
    
    string get(string key, int timestamp) {
        if((m.find(timestamp)!=m.end()) && (m[timestamp][0]==key)){
            return m[timestamp][1];
        }
        for(auto it=m.rbegin();it!=m.rend();it++){
            if(it->second[0]==key && it->first<timestamp){
                return it->second[1];
            }
        }
        return "";
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */