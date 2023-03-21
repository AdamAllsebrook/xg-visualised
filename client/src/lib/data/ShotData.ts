import type { Shot, SimpleShot } from '$client';


export class SimpleShotData {
    shots: number
    insideBox: number
    outsideBox: number
    
    constructor(shots: SimpleShot[]) {
        this.shots = shots.length;
        this.insideBox = shots.filter(SimpleShotData.isInBox).length;
        this.outsideBox= this.shots - this.insideBox;
    }

    private static isInBox(shot: SimpleShot) {
        return shot.Y > 15/74 && shot.Y < 59/74 && shot.X > 97/115;
    }
}


export class ShotData extends SimpleShotData {
    penalties: number;
    penaltiesScored: number;

    constructor(shots: Shot[]) {
        super(shots as SimpleShot[]);

        let penalties = shots.filter(ShotData.isPenalty);
        this.penalties = penalties.length;
        this.penaltiesScored = penalties.filter(ShotData.isGoal).length;
    }

    private static isGoal(shot: Shot) {
        return shot.result === 'Goal';
    }

    private static isPenalty(shot: Shot) {
        return shot.situation === 'Penalty';
    }
}

