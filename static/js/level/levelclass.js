console.log("Hello js");

class Level {

    constructor() {
        this.level = 1;
        this.experience = 0;
        this.needNextLevel = 100;
    }
    
    // 経験値を獲得するメソッド。
    gainExperience(exp) {
        this.experience += exp;
        console.log(`経験値${exp}獲得`)
        this.updateUI();

        while (this.experience >= this.needNextLevel) {
            this.levelUp();
        }
    }

    // レベルアップメソッド。
    levelUp() {
        this.experience -= this.needNextLevel;
        this.level++;
        // 次のレベルアップに必要な経験値を上げる。
        this.needNextLevel = Math.floor(this.needNextLevel * 1.1);
        console.log(`レベルアップ。現在のレベル:${this.level}`)
        this.updateUI();

    }

    // レベルアップ後のUI更新
    updateUI() {
        const characterStatus = document.getElementById('characterStatus');
        const progressBar = document.getElementById('progressBar');

        if(characterStatus) {
            characterStatus.textContent = `Level: ${this.level}, exp: ${this.experience / this.needNextLevel}`;
        }

        if(progressBar) {
            const progress = (this.experience / this.needNextLevel) * 100;
            progressBar.style.width = `${progress}%`
        }
    }
}

export default Level;