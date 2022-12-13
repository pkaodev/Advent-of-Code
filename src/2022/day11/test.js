// //returns remainder
// function modBigNumber(num, m)
// {
//     let vec = [];
//     let x = 0;
//     let mod = 0;
 
//     for (let i = 0;
//          i < num.length; i++)
//     {
//         digit = num[i] - '0';
 
//         mod = mod * 10 + digit;
 
//         quo = parseInt(mod / m);
//         vec[x++] = quo;
 
//         mod = mod % m;
//     }

//     const quotient = []
 
//     let zeroflag = 0;
//     for (let i = 0; i < x; i++)
//     {
//         if (vec[i] == 0 &&
//             zeroflag == 0)
//             continue;
//         zeroflag = 1;
//         quotient.push(vec[i]);
//     }
//     return mod;
// }

// //returns quotient
// // console.log(modBigNumber('12', 12))

// // if (this.operation[1] === 'old') {
// //     if (this.operation[0] === '*') {
// //         this.items[0] = BigInt(this.items[0]) * BigInt(this.items[0])
// //     } else {
// //         this.items[0] = BigInt(this.items[0]) + BigInt(this.items[0])
// //     }

// // } else {
// //     if (this.operation[0] === '*') {
// //         this.items[0] = BigInt(this.items[0]) * BigInt(this.operation[1])
// //     } else {
// //         this.items[0] = BigInt(this.items[0]) + BigInt(this.operation[1])
// //     }
// // }

// function primeFactors(n) {
//     const factors = [];
//     let divisor = 2;
  
//     while (n >= 2) {
//       if (n % divisor == 0) {
//         factors.push(divisor);
//         n = n / divisor;
//       } else {
//         divisor++;
//       }
//     }
//     return factors;
//   }

// console.log(primeFactors(17))

console.log(8%7)