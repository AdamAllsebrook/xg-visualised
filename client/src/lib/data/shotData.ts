import type { Shot, SimpleShot } from '$client';

function sum(x: number, y: number) {
    return x + y;
}

export class SimpleShotData {
    shots: number;
    xG: number;

    insideBox: number;
    outsideBox: number;

    left: number;
    right: number;

    firstHalf: number;
    secondHalf: number;

    constructor(shots: SimpleShot[]) {
        this.shots = shots.length;
        this.xG = SimpleShotData.xGsum(shots);

        this.insideBox = shots.filter(SimpleShotData.isInBox).length;
        this.outsideBox = this.shots - this.insideBox;

        this.left = shots.filter(SimpleShotData.isLeft).length;
        this.right = this.shots - this.left;

        this.firstHalf = shots.filter(SimpleShotData.isFirstHalf).length;
        this.secondHalf = this.shots - this.firstHalf;
    }

    private static isInBox(shot: SimpleShot) {
        return shot.Y > 15 / 74 && shot.Y < 59 / 74 && shot.X > 97 / 115;
    }

    private static isLeft(shot: SimpleShot) {
        return shot.Y > 0.5;
    }

    private static isFirstHalf(shot: SimpleShot) {
        return shot.minute <= 45;
    }

    protected static xGsum(shots: SimpleShot[]) {
        return shots.map((x) => x.xG).reduce(sum);
    }
}

export class ShotData extends SimpleShotData {
    scored: number;

    penalties: number;
    penaltiesScored: number;
    npxG: number;

    isOverperforming: boolean;
    overperformance: number;
    underperformance: number;

    constructor(shots: Shot[]) {
        super(shots as SimpleShot[]);

        this.scored = shots.filter(ShotData.isGoal).length;

        let penalties = shots.filter(ShotData.isPenalty);
        this.penalties = penalties.length;
        this.penaltiesScored = penalties.filter(ShotData.isGoal).length;
        this.npxG = SimpleShotData.xGsum(shots.filter((x) => !ShotData.isPenalty(x)));

        this.isOverperforming = this.scored > this.xG;
        this.overperformance = this.scored - this.xG;
        this.underperformance = -this.overperformance;
    }

    private static isGoal(shot: Shot) {
        return shot.result === 'Goal';
    }

    private static isPenalty(shot: Shot) {
        return shot.situation === 'Penalty';
    }
}
