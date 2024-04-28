

/*
    @param key: string
    @param value: string
    @desc: set local storage value by key
*/
export const setStorage = (key,value) => {
    return window.localStorage.setItem(key,value);
}

/*
    @param key: string
    @desc: get local storage by key
*/
export const getStorage = (key) => {
    return window.localStorage.getItem(key);
}


/*
    @param key: string
    @desc: remove local storage by key if key exists
*/
export const removeStorage = (key) => {
    return window.localStorage.removeItem(key);
}