const isEmptyObject = (obj) => (Object.keys(obj).length === 0 && obj.constructor === Object && Object.getOwnPropertySymbols(obj).length === 0);