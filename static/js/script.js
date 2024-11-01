// main.js

// 初期データをローカルストレージから取得
let currentLevel = parseInt(localStorage.getItem('level')) || 1;
let currentExp = parseInt(localStorage.getItem('exp')) || 0;
let expToNextLevel = 50 + (currentLevel - 1) * 25; // 初期値100に、レベルごとに50追加

// 必要な要素を取得
const levelElement = document.getElementById('level');
const expElement = document.getElementById('exp');
const progressElement = document.getElementById('progress');
const solveProblemButton = document.getElementById('solve-problem');

// 経験値を増加させる関数
function gainExp(exp) {
    currentExp += exp;
    if (currentExp >= expToNextLevel) {
        levelUp();
    }
    localStorage.setItem('exp', currentExp);
    updateDisplay();
}

// レベルアップの処理
function levelUp() {
    currentLevel++;
    currentExp -= expToNextLevel;
    expToNextLevel += 25; // レベルアップごとに必要経験値を増加させる
    alert(`レベルアップ！現在のレベル: ${currentLevel}`);
    
    // 更新された値をローカルストレージに保存
    localStorage.setItem('level', currentLevel);
    localStorage.setItem('exp', currentExp);
    localStorage.setItem('expToNextLevel', expToNextLevel);
}

// 画面の表示を更新
function updateDisplay() {
    levelElement.textContent = currentLevel;
    expElement.textContent = `${currentExp}/${expToNextLevel}`;
    const progressPercentage = (currentExp / expToNextLevel) * 100;
    progressElement.style.width = `${progressPercentage}%`;
}

// ボタンのクリックイベントを設定
solveProblemButton.addEventListener('click', () => {
    gainExp(25); // 1回の問題で10経験値を増加させる
});

// 初期状態を表示
updateDisplay();
