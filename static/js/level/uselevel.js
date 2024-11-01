import Level from "./levelclass";

const level = new Level();

window.solveProblem = function() {
    const exp = 50;
    level.gainExperience(exp);
    
}