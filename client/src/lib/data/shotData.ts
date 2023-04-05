import type { Shot, SimpleShot } from '$client';
import { sum } from './utils';

export class SimpleShotData {
    shots: number;
    xG: number;

    insideBox: number;
    outsideBox: number;

    left: number;
    right: number;
    xgLeft: number;
    xgRight: number;

    firstHalf: number;
    secondHalf: number;

    home: number;
    away: number;
    xgHome: number;
    xgAway: number;

    binnedY: SimpleShot[][];

    constructor(shots: SimpleShot[]) {
        this.shots = shots.length;
        this.xG = SimpleShotData.xGsum(shots);

        this.insideBox = shots.filter(SimpleShotData.isInBox).length;
        this.outsideBox = this.shots - this.insideBox;

        this.left = shots.filter(SimpleShotData.isLeft).length;
        this.right = this.shots - this.left;
        this.xgLeft = SimpleShotData.xGsum(shots.filter(SimpleShotData.isLeft));
        this.xgRight = this.xG - this.xgLeft;

        this.firstHalf = shots.filter(SimpleShotData.isFirstHalf).length;
        this.secondHalf = this.shots - this.firstHalf;

        this.home = shots.filter(SimpleShotData.isHome).length;
        this.away = this.shots - this.home;
        this.xgHome = SimpleShotData.xGsum(shots.filter(SimpleShotData.isHome));
        this.xgAway = this.xG - this.xgHome;

        this.binnedY = SimpleShotData.pitchYBins(shots);
    }

    strPercent(nShots: number, dp: number = 2, totalShots: number | null = null) {
        return ((nShots / (totalShots || this.shots)) * 100).toFixed(dp);
    }

    static minuteBins(shots: SimpleShot[]): SimpleShotData[] {
        return [...Array(6).keys()]
            .map((i) => shots.filter((shot) => shot.minute >= i * 15 && (i == 5 || shot.minute < (i + 1) * 15)))
            .map((shots) => new SimpleShotData(shots));
    }

    static pitchYBins(shots: SimpleShot[]): SimpleShot[][] {
        return [
            shots.filter(SimpleShotData.isWideLeft),
            shots.filter(SimpleShotData.isInsideLeft),
            shots.filter(SimpleShotData.isCentral),
            shots.filter(SimpleShotData.isInsideRight),
            shots.filter(SimpleShotData.isWideRight),
        ];
    }

    static isInBox(shot: SimpleShot) {
        return shot.Y > 15 / 74 && shot.Y < 59 / 74 && shot.X > 97 / 115;
    }

    static isWideLeft(shot: SimpleShot) {
        return shot.Y >= 59 / 74;
    }

    static isWideRight(shot: SimpleShot) {
        return shot.Y < 15 / 74;
    }

    static isInsideLeft(shot: SimpleShot) {
        return shot.Y < 59 / 74 && shot.Y >= 41 / 74;
    }

    static isInsideRight(shot: SimpleShot) {
        return shot.Y >= 15 / 74 && shot.Y < 33 / 74;
    }

    static isCentral(shot: SimpleShot) {
        return shot.Y >= 33 / 74 && shot.Y < 41 / 74;
    }

    private static isLeft(shot: SimpleShot) {
        return shot.Y > 0.5;
    }

    private static isFirstHalf(shot: SimpleShot) {
        return shot.minute <= 45;
    }

    private static isHome(shot: SimpleShot) {
        return shot.h_a === 'h';
    }

    static xGsum(shots: SimpleShot[]) {
        return shots.map((x) => x.xG).reduce(sum, 0);
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
