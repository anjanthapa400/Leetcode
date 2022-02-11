const sumarr = (arr) => {
    let sum = 0;
    if (arr.length == 1) {
        return arr[0];
    }

    let val = sumarr(arr.splice(0,(arr.length-1)));
    val = val + arr[0];
    console.log(arr[0]);
    return val;
}

console.log(sumarr([1,2,3,4,5,5]));