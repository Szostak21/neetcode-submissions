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

    TrieNode* findNode(const string& word){
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
    
    void insert(string word) {
        TrieNode* curr = root;
        for(char c : word){
            if(!curr->children[c - 'a']){
                curr->children[c - 'a'] = new TrieNode;
            }
            curr = curr->children[c - 'a'];
        }
        curr->isEnd = true;
    }
    
    bool search(string word) {
        TrieNode* end = findNode(word);
        return end && end->isEnd;
    }
    
    bool startsWith(string prefix) {
        return findNode(prefix) != nullptr;
    }
};
