// correct.js

// 経験値と表示回数をローカルストレージから取得
let displayCount = parseInt(localStorage.getItem('displayCount')) || 0;
let currentExp = parseInt(localStorage.getItem('exp')) || 0;

// 表示回数を増加
displayCount++;
localStorage.setItem('displayCount', displayCount);

// 1回の表示で増加する経験値
const expPerDisplay = 10; 

// 経験値を増加
currentExp += expPerDisplay;
localStorage.setItem('exp', currentExp);
