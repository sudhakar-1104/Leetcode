/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    // Check if the array has any elements
    if (this.length === 0) {
        return -1;
    }
    
    // Return the element at the last index
    return this[this.length - 1];
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */