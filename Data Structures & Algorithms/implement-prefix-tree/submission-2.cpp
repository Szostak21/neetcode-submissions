class PrefixTree {
    struct TrieNode{
        TrieNode* children[26] = {};
        bool isEnd = false;

        ~TrieNode(){
            for(int i = 0; i < 26; ++i){
                delete children[i];
            }
        }
    };

    TrieNode* root;

    TrieNode* findNode(const string& word) const {
        TrieNode* curr = root;
        for(char c : word){
            if(!curr->children[c - 'a']) return nullptr;
            curr = curr->children[c - 'a'];
        }
        return curr;
    }
public:
    PrefixTree(){
        root = new TrieNode();
    }

    ~PrefixTree(){
        delete root;
    }
    
    void insert(const string& word) {
        TrieNode* curr = root;
        for(char c : word){
            if(!curr->children[c - 'a']){
                curr->children[c - 'a'] = new TrieNode;
            }
            curr = curr->children[c - 'a'];
        }
        curr->isEnd = true;
    }
    
    bool search(const string& word) const {
        TrieNode* end = findNode(word);
        return end && end->isEnd;
    }
    
    bool startsWith(const string& prefix) const {
        return findNode(prefix) != nullptr;
    }
};
