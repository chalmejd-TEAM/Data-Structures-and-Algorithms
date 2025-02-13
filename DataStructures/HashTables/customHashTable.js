class HashTable {
    constructor(size) {
        this.data = new Array(size);
    }

    // Simple Hash Function
    _hash(key) {
        let hash = 0;
        for (let i=0; i < key.length; i++){
            hash = (hash + key.charCodeAt(i) * i) % this.data.length;
        }
        return hash;
    }

    // Set Method
    set(key, value) {
        let address = this._hash(key);
        if (!this.data[address]) {
            this.data[address] = [];
        } 
        this.data[address].push([key, value]);
        return this.data;
    }

    // Get Method
    get(key) {
        let address = this._hash(key);
        const currentBucket = this.data[address];
        if (currentBucket) {
            for(let i=0; i<currentBucket.length; i++) {
                if (currentBucket[i][0] === key) {
                    return currentBucket[i][1];
                }
            }
        }
        return undefined
    }

    // Keys Method
    keys() {
        if (!this.data.length) {
            return undefined
        }
        let result = []
        for (let i=0; i<this.data.length; i++) {
            if (this.data[i] && this.data[i].length) {
                if (this.data[i].length > 1) {
                    for (let j=0; j<this.data[i].length; j++) {
                        result.push(this.data[i][j][0])
                    }
                } else {
                    result.push(this.data[i][0])
                }
            }
        }
        return result;
    }
}

const myHashTable = new HashTable(50);
myHashTable.set('grapes', 10000)
myHashTable.set('apples', 54);
myHashTable.set('oranges', 97);
myHashTable.set('kiwis', 2);
myHashTable.get('grapes');
myHashTable.keys();
