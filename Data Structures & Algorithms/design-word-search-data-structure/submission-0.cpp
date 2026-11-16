class WordDictionary {
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

    bool dfs(const TrieNode* curr, const string& word, int i){
        if(!curr) return false;

        if(word.size() == i) return curr->isEnd;
        
        char c = word[i];

        if(c == '.'){
            for(int j = 0; j < 26; ++j){
                if(curr->children[j] && dfs(curr->children[j], word, i + 1)){
                    return true;
                }
            }
            return false;
        }

        if(!curr->children[c - 'a']){
            return false;
        }

        return dfs(curr->children[c - 'a'], word, i + 1);
    }

public:
    WordDictionary() {
        root = new TrieNode();        
    }
    
    ~WordDictionary(){
        delete root;
    }

    WordDictionary(const WordDictionary&) = delete;

    WordDictionary& operator=(const WordDictionary&) = delete;

    void addWord(const string& word) {
        TrieNode* curr = root;
        for(char c : word){
            int idx = c - 'a';
            if(!curr->children[idx]){
                curr->children[idx] = new TrieNode();
            }
            curr = curr->children[idx];
        }
        curr->isEnd = true;
    }
    
    bool search(string word) {
        return dfs(root, word, 0);
    }
};
