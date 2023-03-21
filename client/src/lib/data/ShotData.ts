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
    constructor(shots: Shot[]) {
        super(shots as SimpleShot[]);

    }
}
